from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from apps.spamer.models import Account
from apps.spamer.models import Chat
from apps.spamer.forms import AccountForm
from apps.spamer.forms import ChatForm


class BaseSpamerView(LoginRequiredMixin, TemplateView):
    template_name = "spamer/home/index.html"


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    context_object_name = 'accounts'
    template_name = 'spamer/home/account.html'

    def get_context_data(self, **kwargs):
        context = super(AccountListView, self).get_context_data(**kwargs)
        context.update({'segment': 'account'})
        return context


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    context_object_name = 'account'
    template_name = 'spamer/home/account_details.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        return context


class AccountCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = AccountForm
    success_url = '/spm'
    template_name = 'spamer/crud/account_create.html'
    success_message = 'Аккаунт успешно создан!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'spamer/crud/account_create.html'
    success_url = '/spm'
    success_message = 'Аккаунт успешно обновлен!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = '/spm'
    template_name = 'spamer/crud/account_delete.html'


class ChatListView(LoginRequiredMixin, ListView):
    model = Chat
    context_object_name = 'chats'
    template_name = 'spamer/home/chat.html'

    def get_context_data(self, **kwargs):
        context = super(ChatListView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm-chats'})
        return context


class ChatDetailView(LoginRequiredMixin, DetailView):
    model = Chat
    context_object_name = 'chat'
    template_name = 'spamer/home/chat_details.html'

    def get_context_data(self, **kwargs):
        context = super(ChatDetailView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm-chats'})
        return context


class ChatCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = ChatForm
    success_url = '/spm'
    template_name = 'spamer/crud/chat_create.html'
    success_message = 'Чат успешно создан!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Chat
    form_class = ChatForm
    template_name = 'spamer/crud/chat_create.html'
    success_url = '/spm'
    success_message = 'Чат успешно обновлен!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatDeleteView(LoginRequiredMixin, DeleteView):
    model = Chat
    success_url = '/spm'
    template_name = 'spamer/crud/chat_delete.html'
