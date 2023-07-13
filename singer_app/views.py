from typing import Any, Dict
from django.db.models import Q
from django.views.generic import DetailView, ListView

from .models import Singer

# singer app view.py

class SingerView(ListView):
    """Singer view class"""

    model = Singer
    template_name = '../templates/singer_app/all_artists.html'
    context_object_name = 'singers'
    paginate_by = 32


class SingerDetailView(DetailView):
    """Singer detail page view"""
    model = Singer
    template_name = '../templates/singer_app/artist_detail_page.html'
    context_object_name = 'singer'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        obj = kwargs['object']
        pk = obj.pk

        artists_dict = Singer.objects.all().exclude(pk=pk)
        if artists_dict:
            data = dict([(Singer.objects.get(pk=item.pk), 0) for item in artists_dict])
            for key,value in data.items():
                data[key] += int(obj.genre.name == key.genre.name)

            data = sorted(data.items(), key=lambda x:-x[1])[:5]

            related_artists = [i[0] for i in data]
            
            context['related_artists'] = related_artists

        if not "recently_viewed" in self.request.session:
            self.request.session["recently_viewed"] = []
            self.request.session["recently_viewed"].append(pk)
        else:
            if pk in self.request.session["recently_viewed"]:
                self.request.session["recently_viewed"].remove(pk)
            self.request.session["recently_viewed"].insert(0, pk)
            if len(self.request.session["recently_viewed"]) > 5:
                self.request.session["recently_viewed"].pop()
        self.request.session.modified =True

        recently_viewed = Singer.objects.filter(pk__in=self.request.session["recently_viewed"])
        context['recently_viewed'] = sorted(recently_viewed, key=lambda x: self.request.session["recently_viewed"].index(x.pk))

        return context
