from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment, Profile, Post, PostImages


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='Meno používateľa',
        min_length=3,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zadaj svoje nové používateľské meno'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Zadaj svoj e-mail'}),
    )
    password1 = forms.CharField(
        required=True,
        label='Heslo',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Zadaj heslo'}),
    )
    password2 = forms.CharField(
        required=True,
        label='Potvrdiť heslo',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Znovu napíš zadané heslo'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Meno používateľa',
        min_length=3,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zadaj svoje používateľské meno'})
    )
    password = forms.CharField(
        required=True,
        label='Heslo',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Zadaj heslo'}),
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'country', 'bio']

class PostAddPostSideForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'icon', 'category']

class PostAddImageSideForm(forms.ModelForm):
    class Meta:
        model = PostImages
        fields = ['image']