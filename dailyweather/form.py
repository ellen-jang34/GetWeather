from django import forms

from .models import GPSPosition, Map

class PostForm(forms.ModelForm):

    class Meta:
        model = GPSPosition
        fields = ('longitude', 'latitude',)

#display map
class MapForm(forms.ModelForm):

    class Meta:
        model = Map
        fields = ('map_name', 'description', 'picture',)
        geom = forms.PolygonField()