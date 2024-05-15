from django import forms
from .models import medkit
from .models import searchb

class ProductForm(forms.ModelForm):
    class Meta:
        model = medkit
        fields = '__all__'


class sear(forms.ModelForm):
    class meta:
        model = searchb
        fields = '__all__'