from django import forms
from app1.models import Concern

class ImageForm(forms.ModelForm):
    class Meta:
        model = Concern
        fields = ('image','context','latitude', 'longitude', )
        
