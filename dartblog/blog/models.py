from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Модель категории поста"""
    title = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, verbose_name='Category URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    """Модель тега"""
    title = models.CharField(max_length=100, verbose_name='Название тега')
    slug = models.SlugField(max_length=100, verbose_name='Tag URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    """Модель поста"""
    title = models.CharField(max_length=100, verbose_name='Заголовок поста')
    content = models.TextField(blank=True, verbose_name='Содержание')
    author = models.CharField(max_length=100, verbose_name='Автор')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Отредактировано')
    views = models.IntegerField(verbose_name='Количество просмотрров', default=0)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField(to=Tag, blank=True, verbose_name='Теги')
    slug = models.SlugField(max_length=100, verbose_name='Post URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-updated_at']
