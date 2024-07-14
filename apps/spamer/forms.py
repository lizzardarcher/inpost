from django import forms
from django.contrib.auth import get_user_model

from apps.spamer.models import *
from ..middleware import current_user

User = get_user_model()


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['id_account', 'username', 'api_id', 'api_hash', 'phone', 'sms_code', 'signed_in', 'status',
                  'report', 'session', 'session_for_chat', 'session_for_lk', 'common_text', 'auto_answering_text',
                  'is_auto_answering_active', 'is_spam_active', 'is_spam_lk_active', 'delay', 'master_to_forward',
                  'account_enabled'
                  ]
        widgets = {
            'id_account': forms.NumberInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'api_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'api_hash': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'sms_code': forms.TextInput(attrs={'class': 'form-control'}),
            'signed_in': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'report': forms.TextInput(attrs={'class': 'form-control'}),
            'session_for_chat': forms.TextInput(attrs={'class': 'form-control'}),
            'session_for_lk': forms.TextInput(attrs={'class': 'form-control'}),
            'common_text': forms.Textarea(attrs={'class': 'form-control'}),
            'auto_answering_text': forms.Textarea(attrs={'class': 'form-control'}),
            'is_auto_answering_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_spam_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_spam_lk_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'delay': forms.TextInput(attrs={'class': 'form-control'}),
            'master_to_forward': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'account_enabled': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['category', 'title', 'subscribers', 'username', 'text', 'delay', 'is_user_banned', 'is_emoji_allowed',
                  'is_del_mes_available', 'is_active', 'comment', 'worked_out'
                  ]
        widgets = {
            'category': forms.ChoiceField(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subscribers': forms.NumberInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'delay': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_user_banned': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_emoji_allowed': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_del_mes_available': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'worked_out': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
