# -*- encoding: utf-8 -*-

from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import (ListView, DeleteView, UpdateView, CreateView, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Bot, Chat, Media, Button, User, PostSchedule, PostPhoto
from .forms import PostForm, PostPhotoForm, PostCreationMultiForm, PostScheduleForm, PostScheduleMultiForm
from .calendar import PostCalendar

from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


@login_required
def post(request):
    ImageFormSet = modelformset_factory(PostPhoto,
                                        form=PostPhotoForm, extra=3)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=PostPhoto.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['photos']
                    photo = PostPhoto(post=post_form, photos=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=PostPhoto.objects.none())
    return render(request, 'crud/test_post.html', {'postForm': postForm, 'formset': formset})


# USER ##############################################

class UserUpdateView(UpdateView):
    template_name = 'home/user_profile.html'
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = '/user_profile'

    def user_profile(request):
        return redirect('/user_profile/1')


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
    success_url = '/bot'

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


# CALENDAR ###############################################

class CalendarView(TemplateView):
    template_name = 'crud/calendar.html'

    def get(self, request, year, month, *args, **kwargs):
        cal = PostCalendar().formatmonth(theyear=int(year), themonth=int(month))
        context = {'cal': cal}
        return render(request, 'home/calendar.html', context=context)

    def post(self, request, year, month, *args, **kwargs):
        cal = PostCalendar().formatmonth(theyear=int(year), themonth=int(month))
        context = {'cal': cal}
        return render(request, 'home/calendar.html', context=context)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def calendar_event(request, year, month, day):
    post = Post.objects.filter(user=request.user).last()
    form = PostScheduleForm(request.POST, instance=post)
    if form.is_valid():
        print(form)
        form.save()
        # return redirect(f"/calendar/{datetime.now().year}/{datetime.now().month}/")
    return render(request, 'home/calendar_event.html', context={
        'posts': post,
        'year': year,
        'month': month,
        'day': day
    })


class CalendarEventCreate(CreateView):
    model = PostSchedule
    form_class = PostScheduleForm
    template_name = 'crud/calendar_event_create.html'
    success_url = f'/calendar/{datetime.now().year}/{datetime.now().month}/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ScheduleUpdateView(UpdateView):
    model = PostSchedule
    template_name = 'crud/schedule_update.html'
    form_class = PostScheduleForm
    success_url = f'/calendar/{datetime.now().year}/{datetime.now().month}/'


class ScheduleDeleteView(LoginRequiredMixin, DeleteView):
    model = PostSchedule
    success_url = f'/calendar/{datetime.now().year}/{datetime.now().month}/'
    template_name = 'crud/schedule_delete.html'


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index',
               'year': datetime.now().year,
               'month': datetime.now().month}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

