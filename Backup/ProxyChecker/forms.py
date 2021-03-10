from django import forms





class InputForm(forms.Form):
    #FileUpload = forms.FileUpload()
    Textfield = forms.CharField(widget=forms.Textarea)
