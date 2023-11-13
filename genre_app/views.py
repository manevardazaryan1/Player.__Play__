from django.views.generic import DetailView, ListView
from .models import Genre
# music_app views classes and functions.

class GenreView(ListView):
    """All genres template class - GenreView"""

    model = Genre
    template_name = '../templates/genre_app/genres.html'
    context_object_name = 'genres'

class GenreDetailView(DetailView):
    """Genre detail page view"""

    queryset = Genre.objects.all()
    template_name = '../templates/genre_app/genre_detail_page.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        obj = kwargs['object']
        pk = obj.pk

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

        recently_viewed = Genre.objects.filter(pk__in=self.request.session["recently_viewed"])
        context['recently_viewed'] = sorted(recently_viewed, key=lambda x: self.request.session["recently_viewed"].index(x.pk))

        return context

    