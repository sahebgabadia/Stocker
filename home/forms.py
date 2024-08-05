from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fname = forms.CharField(label='First Name', required=True)
    lname = forms.CharField(label='Last Name',required=True)

    class Meta:
        model = User
        fields = ("username", "fname", "lname", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.fname = self.cleaned_data["fname"]
        user.lname = self.cleaned_data["lname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user