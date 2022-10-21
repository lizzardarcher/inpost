# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from . import validators


class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exp_date = models.DateField(null=True, blank=True, verbose_name='Оплачено по:')
    is_vip = models.BooleanField(default=False, blank=True, verbose_name='VIP')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статус оплаты'


class Bot(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Название бота', validators=[validators.validate_post_name])
    token = models.CharField(max_length=300, null=False, blank=False, verbose_name='Телеграм Токен')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "Бот"
        verbose_name_plural = "Боты"


class Post(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Название поста', validators=[validators.validate_post_name])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Бот')
    post_type = models.CharField(max_length=20, choices=[('Пост', 'Пост'), ('Опрос', 'Опрос')], null=True, blank=False, verbose_name='Тип поста')
    text = models.TextField(max_length=5000, null=True, blank=True, verbose_name='Текст')
    is_active = models.BooleanField(null=True, blank=True, default=False, verbose_name='Активно')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class PostSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=False, verbose_name='Пост')
    schedule = models.DateTimeField(null=True, blank=False, verbose_name='Расписание')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.post.name

    class Meta:
        ordering = ['id']
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пост')
    photos = models.ImageField(verbose_name='Фото')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.post.name + ' - ' + str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class PostMusic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пост')
    music = models.FileField(verbose_name='Музыкальный Трек')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.post.name + ' - ' + str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = "Муз Трек"
        verbose_name_plural = "Муз Треки"


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пост')
    video = models.FileField(verbose_name='Видео Запись')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.post.name + ' - ' + str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = "Видео Запись"
        verbose_name_plural = "Видео Записи"


class PostDocument(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пост')
    document = models.FileField(verbose_name='Документ')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.post.name + ' - ' + str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class Button(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название кнопки')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пост')
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "Кнопка"
        verbose_name_plural = "Кнопки"


class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пост')
    media = models.FileField(null=True, blank=True, verbose_name='Медиа файл')
    id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'

    def __str__(self):
        return str(self.media)


class Chat(models.Model):
    chat_type = models.CharField(max_length=20, choices=[('Группа', 'Группа'), ('Канал', 'Канал')], null=True, blank=False, verbose_name='Тип Чата')
    # name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название')
    ref = models.CharField(max_length=200, null=True, unique=True, validators=[validators.validate_contains_https], verbose_name='Ссылка на чат')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['id']

    def __str__(self):
        return self.ref
