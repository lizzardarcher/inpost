from django import forms

from betterforms.multiform import MultiModelForm

from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_type', 'name', 'text', 'bot']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}, ),
        }


class PostPhotoForm(forms.ModelForm):
    class Meta:
        model = PostPhoto
        fields = ['photos']
        widgets = {
            'photos': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        }


class PostMusicForm(forms.ModelForm):
    class Meta:
        model = PostMusic
        fields = ['music']
        widgets = {
            'music': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        }


class PostVideoForm(forms.ModelForm):
    class Meta:
        model = PostVideo
        fields = ['video']
        widgets = {
            'video': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        }


class PostDocumentForm(forms.ModelForm):
    class Meta:
        model = PostDocument
        fields = ['document']
        widgets = {
            'document': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        }


class PostCreationMultiForm(MultiModelForm):
    form_classes = {
        'post': PostForm,
        'photo': PostPhotoForm,
    }


class PostScheduleForm(forms.ModelForm):
    class Meta:
        model = PostSchedule
        fields = ['post', 'schedule']
        widgets = {
            'schedule': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


class PostScheduleMultiForm(MultiModelForm):
    form_classes = {
        'post': PostScheduleForm,
    }


class BotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ['name', 'token']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'token': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['chat_type', 'ref']
        widgets = {
            'chat_type': forms.TextInput(attrs={'class': 'form-control'}),
            'ref': forms.TextInput(attrs={'class': 'form-control'}),
        }
