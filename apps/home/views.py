# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import (ListView, DeleteView, UpdateView, CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin

from betterforms.multiform import MultiModelForm

from .models import Post, Bot, Chat, Media, Button, User
from .forms import PostForm, PostPhotoForm,PostCreationMultiForm


# POST ##############################################

class PostListView(LoginRequiredMixin, ListView):
    extra_context = {'segment': 'post'}
    model = Post
    context_object_name = 'posts'
    template_name = 'home/post.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'crud/post_create.html'
    success_url = 'post'

    def form_valid(self, form):
        print(form.instance.user)
        form.instance.user = self.request.user
        return super().form_valid(form)

# class PostCreateView(CreateView):
#     form_class = PostCreationMultiForm
#     template_name = 'crud/post_create.html'
#     success_url = 'post'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         post = form['post'].save()
#         photo = form['photo'].save(commit=False)
#         photo.post = post
#         photo.save()
#         if self.request.FILES:
#             for f in self.request.FILES.getlist('photo'):
#                 photo = self.model.objects.create(photo=f)
#         return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     files = request.FILES.getlist('photo')
    #     if form.is_valid():
    #         for f in files:
    #             ...  # Do something with each file.
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'crud/post_create.html'
    success_url = '/post'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/post'
    template_name = 'crud/post_delete.html'


# BOT ###############################################


class BotListView(LoginRequiredMixin, ListView):
    extra_context = {'segment': 'bot'}
    model = Bot
    context_object_name = 'bots'
    template_name = 'home/bot.html'

    def get_queryset(self):
        return Bot.objects.filter(user=self.request.user)


class BotCreateView(LoginRequiredMixin, CreateView):
    model = Bot
    fields = ['name', 'token']
    template_name = 'crud/bot_create.html'
    success_url = 'bot'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BotUpdateView(LoginRequiredMixin, UpdateView):
    model = Bot
    fields = ['name', 'token']
    template_name = 'crud/bot_create.html'
    success_url = 'bot'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BotDeleteView(LoginRequiredMixin, DeleteView):
    model = Bot
    success_url = '/bot'
    template_name = 'crud/bot_delete.html'


# CHANNEL ###############################################

class ChatListView(LoginRequiredMixin, ListView):
    extra_context = {'segment': 'chat'}
    model = Chat
    context_object_name = 'chats'
    template_name = 'home/chat.html'

    def get_queryset(self):
        return Chat.objects.filter(user=self.request.user)


class ChatCreateView(LoginRequiredMixin, CreateView):
    model = Chat
    fields = ['chat_type', 'ref']
    template_name = 'crud/chat_create.html'
    success_url = '/chat'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatUpdateView(LoginRequiredMixin, UpdateView):
    model = Chat
    fields = '__all__'
    template_name = 'crud/chat_create.html'
    success_url = '/chat'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatDeleteView(LoginRequiredMixin, DeleteView):
    model = Chat
    success_url = '/chat'
    template_name = 'crud/chat_delete.html'


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
