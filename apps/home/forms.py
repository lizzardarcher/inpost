from django import forms

from betterforms.multiform import MultiModelForm

from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_type', 'name', 'text', 'bot']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Озаглавьте ваш пост, для более удобного управления'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}, ),
        }


class PostPhotoForm(forms.ModelForm):
    class Meta:
        model = PostPhoto
        fields = ['photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5']
        widgets = {
            'photo_1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo_2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo_3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo_4': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo_5': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PostMusicForm(forms.ModelForm):
    class Meta:
        model = PostMusic
        fields = ['music']
        widgets = {
            'music': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PostVideoForm(forms.ModelForm):
    class Meta:
        model = PostVideo
        fields = ['video']
        widgets = {
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PostDocumentForm(forms.ModelForm):
    class Meta:
        model = PostDocument
        fields = ['document']
        widgets = {
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PostReferenceForm(forms.ModelForm):
    class Meta:
        model = PostReference
        fields = ['reference', 'text']
        widgets = {
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://t.me/your_group'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '...'}),
        }


class PostButtonForm(forms.ModelForm):
    class Meta:
        model = Button
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'text-align: center;'}),
        }


class PostScheduleForm(forms.ModelForm):
    class Meta:
        model = PostSchedule
        fields = ['post', 'schedule']
        widgets = {
            # 'post': forms.Input(attrs={'class': 'form-control'}),
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


class PostCreationMultiForm(MultiModelForm):
    form_classes = {
        'post': PostForm,
        'photo': PostPhotoForm,
        'video': PostVideoForm,
        'music': PostMusicForm,
        'document': PostDocumentForm,
        'reference': PostReferenceForm,
        'button': PostButtonForm,
    }