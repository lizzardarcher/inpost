from django import forms

from betterforms.multiform import MultiModelForm

from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'post_type', 'text',
                  'photo',
                  # 'user',
                  'video', 'document', 'bot', 'is_active']
        # widgets = {
        #     'user': forms.TextInput(attrs={'value': user}),
        # }
        # #     'video': forms.ClearableFileInput(attrs={'multiple': True}),
        # #     'document': forms.ClearableFileInput(attrs={'multiple': True}),
        # # }


class PostPhotoForm(forms.ModelForm):
    class Meta:
        model = PostPhoto
        fields = ['photos']
        widgets = {
            'photos': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class PostCreationMultiForm(MultiModelForm):

    form_classes = {
        'post': PostForm,
        'photo': PostPhotoForm,
    }
