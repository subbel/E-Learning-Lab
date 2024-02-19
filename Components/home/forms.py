from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.Form):
    first_name = forms.CharField(label='', min_length=4, max_length=20, widget=forms.TextInput(attrs={'class': "fname", "placeholder":"Firstname" }))
    last_name = forms.CharField(label='', min_length=4, max_length=20, widget=forms.TextInput(attrs={'class': "lname", "placeholder":"Lastname"}))
    # gradelevel = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class': "input-box grade"}))
    username = forms.CharField(label='', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class': "uname", "placeholder":"Username"}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': "email", "placeholder":"Email"}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "p1", "placeholder":"Enter Password"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "p2", "placeholder":"Re-Enter Password"}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_firstname(self):
        first_name = self.cleaned_data['first_name']

        return first_name

    def clean_lastname(self):
        last_name = self.cleaned_data['last_name']

        return last_name

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
        self.cleaned_data['username'],
        first_name = self.cleaned_data['first_name'],
        last_name = self.cleaned_data['last_name'],
        email = self.cleaned_data['email'],
        password = self.cleaned_data['password2'],
            # grade_level = self.cleaned_data['gradelevel'],
        )
        return user