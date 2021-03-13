from django import forms
from .models import ProxyStringUrl



class InputCsvForm(forms.Form):
    #FileUpload = forms.FileUpload()
    Textfield = forms.CharField(widget=forms.Textarea)

class UrlStringFormView(forms.ModelForm):
    class Meta:
        model = ProxyStringUrl
        fields = '__all__'
