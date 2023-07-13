from django import forms
from .models import Playlist

class CreatePlaylistForm(forms.ModelForm):
    """Form for creating playlist"""

    class Meta:

        """CreatePlaylistForm class Meta class"""

        model = Playlist
        fields = ('name',)