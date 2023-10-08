from django import forms
from .models import ImageWithCharField

class ImageWithCharFieldForm(forms.ModelForm):
    class Meta:
        model = ImageWithCharField
        fields = ['latitude', 'longitude', 'context','image']
