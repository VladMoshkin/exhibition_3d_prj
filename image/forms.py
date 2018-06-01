from django import forms
from image.models import Image

class AddImage(forms.ModelForm):
    title = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Image
        fields = ('title', 'image',)
