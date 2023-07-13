from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.urls import re_path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base_app.urls")),
    path("", include("music_app.urls")),
    path("", include("singer_app.urls")),
    path("", include("genre_app.urls")),
    path("", include("user_app.urls")),
    path('accounts/', include('allauth.urls')),

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

urlpatterns += staticfiles_urlpatterns()