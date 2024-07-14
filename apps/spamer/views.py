from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from apps.spamer.models import Account
from apps.spamer.models import Chat
from apps.spamer.models import ChannelToSubscribe

from apps.spamer.forms import AccountForm
from apps.spamer.forms import ChatForm
from apps.spamer.forms import ChannelToSubscribeForm


class BaseSpamerView(LoginRequiredMixin, TemplateView):
    template_name = "spamer/home/index.html"

    def get_context_data(self, **kwargs):
        context = super(BaseSpamerView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm'})
        return context


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    context_object_name = 'accounts'
    template_name = 'spamer/home/account.html'

    def get_context_data(self, **kwargs):
        context = super(AccountListView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'account'})
        return context


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    context_object_name = 'account'
    template_name = 'spamer/home/account_details.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'account'})
        return context


class AccountCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = AccountForm
    success_url = '/spm/account'
    template_name = 'spamer/crud/create.html'
    success_message = 'Аккаунт успешно добавлен!'

    def get_context_data(self, **kwargs):
        context = super(AccountCreateView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'account'})
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'spamer/crud/create.html'
    success_url = '/spm/account'
    success_message = 'Аккаунт успешно обновлен!'

    def get_context_data(self, **kwargs):
        context = super(AccountUpdateView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'account'})
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = '/spm/account'
    template_name = 'spamer/crud/delete.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDeleteView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'account'})
        return context


class ChatListView(LoginRequiredMixin, ListView):
    model = Chat
    context_object_name = 'chats'
    template_name = 'spamer/home/chat.html'

    def get_context_data(self, **kwargs):
        context = super(ChatListView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context


class ChatDetailView(LoginRequiredMixin, DetailView):
    model = Chat
    context_object_name = 'chat'
    template_name = 'spamer/home/chat_details.html'

    def get_context_data(self, **kwargs):
        context = super(ChatDetailView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context


class ChatCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = ChatForm
    success_url = '/spm/chat'
    template_name = 'spamer/crud/create.html'
    success_message = 'Чат успешно создан!'

    def get_context_data(self, **kwargs):
        context = super(ChatCreateView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Chat
    form_class = ChatForm
    template_name = 'spamer/crud/create.html'
    success_url = '/spm/chat'
    success_message = 'Чат успешно обновлен!'

    def get_context_data(self, **kwargs):
        context = super(ChatUpdateView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatDeleteView(LoginRequiredMixin, DeleteView):
    model = Chat
    success_url = '/spm/chat'
    template_name = 'spamer/crud/delete.html'
    success_message = 'Чат успешно удалён!'

    def get_context_data(self, **kwargs):
        context = super(ChatDeleteView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context


class ChannelToSubscribeListView(LoginRequiredMixin, ListView):
    model = ChannelToSubscribe
    context_object_name = 'channels'
    template_name = 'spamer/home/channels_to_sub.html'

    def get_context_data(self, **kwargs):
        context = super(ChannelToSubscribeListView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context


class ChannelToSubscribeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = ChannelToSubscribeForm
    success_url = '/spm/chat'
    template_name = 'spamer/crud/create.html'
    success_message = 'Канал успешно добавлен!'

    def get_context_data(self, **kwargs):
        context = super(ChannelToSubscribeCreateView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChannelToSubscribeUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = ChannelToSubscribe
    form_class = ChannelToSubscribeForm
    template_name = 'spamer/crud/create.html'
    success_url = '/spm/chat'
    success_message = 'Канал успешно обновлен!'

    def get_context_data(self, **kwargs):
        context = super(ChannelToSubscribeUpdateView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChannelToSubscribeDeleteView(LoginRequiredMixin, DeleteView):
    model = ChannelToSubscribe
    success_url = '/spm/chat'
    template_name = 'spamer/crud/delete.html'
    success_message = 'Канал успешно удалён!'

    def get_context_data(self, **kwargs):
        context = super(ChannelToSubscribeDeleteView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'chat'})
        return context


class StatisticsDetailView(LoginRequiredMixin, TemplateView):
    template_name = "spamer/home/statistics.html"

    def get_context_data(self, **kwargs):
        context = super(StatisticsDetailView, self).get_context_data(**kwargs)
        context.update({'segment': 'spm', 'spm_segment': 'stats'})
        return context
