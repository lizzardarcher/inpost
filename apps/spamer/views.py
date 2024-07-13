from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.spamer.models import *
from spamer.forms import *


class AccountListView(LoginRequiredMixin, ListView):
    extra_context = {'segment': 'account'}
    model = Account
    context_object_name = 'account'
    template_name = 'spamer/home/account.html'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AccountListView, self).get_context_data(**kwargs)
        context.update({
            'account': Account.objects.filter(user=self.request.user),
        })
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
    success_url = 'account'
    success_message = 'Аккаунт успешно создан!'
    template_name = 'spamer/crud/account_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'spamer/crud/account_update.html'
    success_url = '/account'
    success_message = 'Аккаунт успешно обновлен!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = '/account'
    template_name = 'spamer/crud/account_delete.html'
