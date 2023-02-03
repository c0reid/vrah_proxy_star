from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from MainArea.models import UserProfileInfo
from .models import Contact



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ['portfolio_site','profile_pic']
