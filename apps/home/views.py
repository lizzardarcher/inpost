# -*- encoding: utf-8 -*-

from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView, DeleteView, UpdateView, CreateView, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (Post, Bot, Chat, Media, Button, User, PostSchedule, PostPhoto, UserStatus, PostDocument, PostVideo,
                     PostMusic)
from .forms import (PostForm, PostPhotoForm, PostCreationMultiForm, PostScheduleForm, PostScheduleMultiForm,
                    PostVideoForm, PostDocumentForm, PostMusicForm, BotForm, ChatForm)
from .calendar import PostCalendar
from .calendar_mini import PostCalendarMini

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
            'photos': PostPhoto.objects.filter(post__user=self.request.user),
            'videos': PostVideo.objects.filter(post__user=self.request.user),
            'musics': PostMusic.objects.filter(post__user=self.request.user),
            'documents': PostDocument.objects.filter(post__user=self.request.user),
            'cal': PostCalendar().formatmonth(theyear=int(datetime.now().year), themonth=int(datetime.now().month)),
        })
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'crud/test_post.html'
    success_url = 'post'

    def form_valid(self, form):
        print(form.instance.user)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, request):
        extra = 10
        ImageFormSet = modelformset_factory(PostPhoto, form=PostPhotoForm, extra=extra)
        MusicFormSet = modelformset_factory(PostMusic, form=PostMusicForm, extra=extra)
        VideoFormSet = modelformset_factory(PostVideo, form=PostVideoForm, extra=extra)
        DocumentFormSet = modelformset_factory(PostDocument, form=PostDocumentForm, extra=extra)
        postForm = PostForm()
        formsetI = ImageFormSet(queryset=PostPhoto.objects.none())
        formsetV = MusicFormSet(queryset=PostMusic.objects.none())
        formsetM = VideoFormSet(queryset=PostVideo.objects.none())
        formsetD = DocumentFormSet(queryset=PostDocument.objects.none())
        return render(request, 'crud/post_create.html', {
            'postForm': postForm,
            'formsetI': formsetI,
            'formsetV': formsetV,
            'formsetM': formsetM,
            'formsetD': formsetD,
        })

    def post(self, request):
        """
        Пример взят отсюда:
        https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
        """
        extra = 10
        ImageFormSet = modelformset_factory(PostPhoto, form=PostPhotoForm, extra=extra)
        MusicFormSet = modelformset_factory(PostMusic, form=PostMusicForm, extra=extra)
        VideoFormSet = modelformset_factory(PostVideo, form=PostVideoForm, extra=extra)
        DocumentFormSet = modelformset_factory(PostDocument, form=PostDocumentForm, extra=extra)

        if request.method == 'POST':

            postForm = PostForm(request.POST)

            formsetI = ImageFormSet(request.POST, request.FILES, queryset=PostPhoto.objects.none())
            formsetV = VideoFormSet(request.POST, request.FILES, queryset=PostVideo.objects.none())
            formsetM = MusicFormSet(request.POST, request.FILES, queryset=PostMusic.objects.none())
            formsetD = DocumentFormSet(request.POST, request.FILES, queryset=PostMusic.objects.none())

            if postForm.is_valid():
                post_form = postForm.save(commit=False)
                post_form.user = request.user
                post_form.save()

                for form in formsetI.cleaned_data:
                    if form:
                        image = form['photos']
                        photo = PostPhoto(post=post_form, photos=image)
                        photo.save()

                for form in formsetV.cleaned_data:
                    if form:
                        video_file = form['video']
                        video = PostVideo(post=post_form, video=video_file)
                        video.save()

                for form in formsetM.cleaned_data:
                    if form:
                        music_file = form['music']
                        music = PostMusic(post=post_form, music=music_file)
                        music.save()

                for form in formsetD.cleaned_data:
                    if form:
                        doc_file = form['document']
                        doc = PostDocument(post=post_form, document=doc_file)
                        doc.save()

                # use django messages framework
                messages.success(request, "Пост успешно добавлен!")
                return HttpResponseRedirect("/post")
            else:
                print(postForm.errors)
        else:
            postForm = PostForm()
            formsetI = ImageFormSet(queryset=PostPhoto.objects.none())
            formsetV = MusicFormSet(queryset=PostMusic.objects.none())
            formsetM = VideoFormSet(queryset=PostVideo.objects.none())
            formsetD = DocumentFormSet(queryset=PostDocument.objects.none())
        return render(request, 'crud/post_create.html', {
            'postForm': postForm,
            'formsetI': formsetI,
            'formsetV': formsetV,
            'formsetM': formsetM,
            'formsetD': formsetD,
        })


class PostUpdateView(LoginRequiredMixin, UpdateView):
    extra = 1

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, request, pk):
        obj = get_object_or_404(Post, id=pk)
        form = PostForm(request.POST or None, instance=obj)
        ImageFormSet = modelformset_factory(PostPhoto, form=PostPhotoForm, extra=self.extra)
        VideoFormSet = modelformset_factory(PostVideo, form=PostVideoForm, extra=self.extra)
        MusicFormSet = modelformset_factory(PostMusic, form=PostMusicForm, extra=self.extra)
        DocumentFormSet = modelformset_factory(PostDocument, form=PostDocumentForm, extra=self.extra)

        formsetI = ImageFormSet(queryset=PostPhoto.objects.filter(post__id=pk))
        formsetV = VideoFormSet(queryset=PostVideo.objects.filter(post__id=pk))
        formsetM = MusicFormSet(queryset=PostMusic.objects.filter(post__id=pk))
        formsetD = DocumentFormSet(queryset=PostDocument.objects.filter(post__id=pk))
        return render(request, 'crud/post_update.html', {
            'postForm': form,
            'formsetI': formsetI,
            'formsetV': formsetV,
            'formsetM': formsetM,
            'formsetD': formsetD,
        })

    def post(self, request, pk):
        ImageFormSet = modelformset_factory(PostPhoto, form=PostPhotoForm, extra=self.extra)
        VideoFormSet = modelformset_factory(PostVideo, form=PostVideoForm, extra=self.extra)
        MusicFormSet = modelformset_factory(PostMusic, form=PostMusicForm, extra=self.extra)
        DocumentFormSet = modelformset_factory(PostDocument, form=PostDocumentForm, extra=self.extra)

        formsetI = ImageFormSet(request.POST, request.FILES, queryset=PostPhoto.objects.filter(post__id=pk))
        formsetV = VideoFormSet(request.POST, request.FILES, queryset=PostVideo.objects.filter(post__id=pk))
        formsetM = MusicFormSet(request.POST, request.FILES, queryset=PostMusic.objects.filter(post__id=pk))
        formsetD = DocumentFormSet(request.POST, request.FILES, queryset=PostDocument.objects.filter(post__id=pk))

        obj = get_object_or_404(Post, id=pk)
        form = PostForm(data=request.POST or None, files=request.FILES or None, instance=obj)

        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formsetI.cleaned_data:
                if form:
                    image = form['photos']
                    photo = PostPhoto(post=post_form, photos=image)
                    photo.save()

            for form in formsetV.cleaned_data:
                if form:
                    video_file = form['video']
                    video = PostVideo(post=post_form, video=video_file)
                    video.save()

            for form in formsetM.cleaned_data:
                if form:
                    music_file = form['music']
                    music = PostMusic(post=post_form, music=music_file)
                    music.save()

            for form in formsetD.cleaned_data:
                if form:
                    doc_file = form['document']
                    doc = PostDocument(post=post_form, document=doc_file)
                    doc.save()

            messages.success(request, "Пост успешно обновлен!")
            return HttpResponseRedirect(f"/post_update/{pk}")
        else:
            print(form.errors)
        return render(request, 'crud/post_update.html', {'postForm': form, 'formsetI': formsetI, })


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/post'
    template_name = 'crud/post_delete.html'


class PostPhotoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PostPhoto
    form_class = PostPhotoForm
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
    context = {
        'segment': 'index',
        'year': datetime.now().year,
        'month': datetime.now().month,
        'bots': Bot.objects.filter(user=request.user),
        'chats': Chat.objects.filter(user=request.user),
        'cal': PostCalendar().formatmonth(theyear=int(datetime.now().year), themonth=int(datetime.now().month)),

    }
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))
