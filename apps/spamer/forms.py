from django import forms

# from betterforms.multiform import MultiModelForm
# from django_quill.forms import QuillFormField

from apps.spamer.models import *
from ..middleware import current_user
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account

