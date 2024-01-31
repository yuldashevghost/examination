from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from xojimuhammad.models import Post


class UserRegisterModelForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    def save(self, commit=True):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1==password2:
            user = super().save(commit)
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Passwords must match")

    class Meta:
        model = Post
        fields = ["username",  "email", "first_name", "last_name", "password1", "password2"]