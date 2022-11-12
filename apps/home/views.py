# -*- encoding: utf-8 -*-
import math
from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView, DeleteView, UpdateView, CreateView, TemplateView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .calendar import PostCalendar
from .calendar_mini import PostCalendarMini
from .utils import get_chat_info, get_bot_info
from apps.middleware import current_user

from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


# USER ##############################################

class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'home/user_profile.html'
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = '/user_profile'
    extra_context = {'segment': 'user'}
    success_message = 'Профиль успешно обновлён'

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

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'posts': Post.objects.filter(user=self.request.user),
            # 'photos': PostPhoto.objects.filter(post__user=self.request.user),
            # 'videos': PostVideo.objects.filter(post__user=self.request.user),
            # 'musics': PostMusic.objects.filter(post__user=self.request.user),
            # 'documents': PostDocument.objects.filter(post__user=self.request.user),
            # 'buttons': Button.objects.filter(post__user=self.request.user),
            # 'references': PostReference.objects.filter(post__user=self.request.user),
            'cal_mini': PostCalendarMini().formatmonth(theyear=int(datetime.now().year),
                                                       themonth=int(datetime.now().month)),
        })
        return context


class PostDetailsView(LoginRequiredMixin, DetailView):
    model = Post

    context_object_name = 'post'
    template_name = 'home/post_details.html'

    # def get_queryset(self, pk):
    #     return Post.objects.get(id=pk)
    #
    def get_context_data(self, **kwargs):
        context = super(PostDetailsView, self).get_context_data(**kwargs)
        context.update({
            'photos': PostPhoto.objects.filter(post__user=self.request.user),
            'videos': PostVideo.objects.filter(post__user=self.request.user),
            'musics': PostMusic.objects.filter(post__user=self.request.user),
            'documents': PostDocument.objects.filter(post__user=self.request.user),
            'buttons': Button.objects.filter(post__user=self.request.user),
            'references': PostReference.objects.filter(post__user=self.request.user),
        })
        return context


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = PostForm
    success_url = 'post'
    success_message = 'Пост успешно создан!'
    template_name = 'crud/post_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'crud/post_update.html'
    success_url = '/post'
    success_message = 'Пост успешно обновлен!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/post'
    template_name = 'crud/post_delete.html'


class PostPhotoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PostPhoto
    # form_class = PostPhotoForm
    template_name = 'crud/post_photo_update.html'
    success_url = '/post'
    success_message = 'Фото успешно обновлено'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostPhotoDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PostPhoto
    success_url = '/post'
    template_name = 'crud/post_photo_delete.html'
    success_message = 'Фото успешно удалено'


class PostVideoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PostVideo
    form_class = PostVideoForm
    template_name = 'crud/post_video_update.html'
    success_url = '/post'
    success_message = 'Видео успешно обновлено'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostVideoDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PostVideo
    success_url = '/post'
    template_name = 'crud/post_video_delete.html'


class PostMusicUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PostMusic
    form_class = PostMusicForm
    template_name = 'crud/post_music_update.html'
    success_url = '/post'
    success_message = 'Трек успешно обновлен'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostMusicDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PostMusic
    success_url = '/post'
    template_name = 'crud/post_music_delete.html'


class PostDocumentUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PostDocument
    form_class = PostDocumentForm
    template_name = 'crud/post_document_update.html'
    success_url = '/post'
    success_message = 'Документ успешно обновлен'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDocumentDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PostDocument
    success_url = '/post'
    template_name = 'crud/post_document_delete.html'


# BOT ###############################################


class BotListView(LoginRequiredMixin, ListView):
    extra_context = {'segment': 'bot'}
    model = Bot
    context_object_name = 'bots'
    template_name = 'home/bot.html'

    def get_queryset(self):
        return Bot.objects.filter(user=self.request.user)


class BotCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Bot
    form_class = BotForm
    template_name = 'crud/bot_create.html'
    success_url = 'bot'
    success_message = 'Бот успешно создан'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Парсим данные бота с помощью requests
        bot_data = get_bot_info(form.instance.ref)
        form.instance.title = bot_data
        return super().form_valid(form)


class BotUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Bot
    form_class = BotForm
    template_name = 'crud/bot_create.html'
    success_url = '/bot'
    success_message = 'Бот успешно обновлен'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BotDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Bot
    success_url = '/bot'
    template_name = 'crud/bot_delete.html'
    success_message = 'Бот успешно удалён'


# CHANNEL ###############################################

class ChatListView(LoginRequiredMixin, ListView):
    extra_context = {'segment': 'chat'}
    model = Chat
    context_object_name = 'chats'
    template_name = 'home/chat.html'

    def get_queryset(self):
        return Chat.objects.filter(user=self.request.user)


class ChatCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Chat
    form_class = ChatForm
    template_name = 'crud/chat_create.html'
    success_url = '/chat'
    success_message = 'Чат успешно создан'

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Парсим данные чата с помощью requests
        chat_data = get_chat_info(form.instance.ref)
        form.instance.subscribers = chat_data[2]
        form.instance.title = chat_data[1]
        form.instance.image = chat_data[0]
        return super().form_valid(form)


class ChatUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Chat
    form_class = ChatForm
    template_name = 'crud/chat_create.html'
    success_url = '/chat'
    success_message = 'Чат успешно обновлён'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChatDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Chat
    success_url = '/chat'
    template_name = 'crud/chat_delete.html'
    success_message = 'Чат успешно удалён'


# CALENDAR ###############################################

class CalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'crud/calendar.html'

    def get(self, request, year, month, *args, **kwargs):
        cal = PostCalendar().formatmonth(theyear=int(year), themonth=int(month))
        cal_mini = PostCalendarMini().formatmonth(theyear=int(year), themonth=int(month))
        context = {'cal': cal, 'cal_mini': cal_mini, 'segment': 'calendar'}
        return render(request, 'home/calendar.html', context=context)

    def post(self, request, year, month, *args, **kwargs):
        cal = PostCalendar().formatmonth(theyear=int(year), themonth=int(month))
        cal_mini = PostCalendarMini().formatmonth(theyear=int(year), themonth=int(month))
        context = {'cal': cal, 'cal_mini': cal_mini, 'segment': 'calendar'}
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
        messages.success(request, "Успешно обновлено")
        # return redirect(f"/calendar/{datetime.now().year}/{datetime.now().month}/")
    return render(request, 'home/calendar_event.html', context={
        'posts': post,
        'year': year,
        'month': month,
        'day': day
    })


class CalendarEventCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = PostSchedule
    form_class = PostScheduleForm
    template_name = 'crud/calendar_event_create.html'
    success_url = f'/calendar/{datetime.now().year}/{datetime.now().month}/'
    success_message = 'Распиание обновлено'

    # extra_context = {'sch': PostSchedule.objects.filter(user=)}

    def get_context_data(self, **kwargs):
        context = super(CalendarEventCreate, self).get_context_data(**kwargs)
        context['sch'] = PostSchedule.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ScheduleUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PostSchedule
    template_name = 'crud/schedule_update.html'
    form_class = PostScheduleForm
    success_url = f'/calendar/{datetime.now().year}/{datetime.now().month}/'
    success_message = 'Расписание обновлено'


class ScheduleDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PostSchedule
    success_url = f'/calendar/{datetime.now().year}/{datetime.now().month}/'
    template_name = 'crud/schedule_delete.html'
    success_message = 'Пост удален из расписания'


@login_required(login_url="/login/")
def index(request):
    subs = 0
    chats = Chat.objects.filter(user=request.user)
    for chat in chats:
        subs += chat.subscribers
    if subs > 10000:
        subs = math.floor(subs / 1000)
    all_users = len(User.objects.all())
    context = {
        'segment': 'index',
        'year': datetime.now().year,
        'month': datetime.now().month,
        'subs': subs,
        'all_users': all_users,
        'bots': Bot.objects.filter(user=request.user),
        'posts': Post.objects.filter(user=request.user),
        'chats': Chat.objects.filter(user=request.user),
        'user_stats': UserStats.objects.filter(user=request.user)[0],
        'user_status': UserStatus.objects.filter(user=request.user),
        'cal': PostCalendar().formatmonth(theyear=int(datetime.now().year), themonth=int(datetime.now().month)),

    }
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))
