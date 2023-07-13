menu = [
    {'title': 'Home', 'url_name': 'base_app:index'},
    {'title': 'Music', 'url_name': 'music_app:music'},
    {'title': 'Artists', 'url_name': 'singer_app:singer'},
    {'title': 'Genre', 'url_name': 'genre_app:genre'},
    {'title': 'Player', 'url_name': 'music_app:player'},
    {'title': 'Playlists', 'url_name': 'music_app:playlists'},
    {'title': 'About', 'url_name': 'base_app:about'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['selected'] = 0
        return context