from django.db import models
from django.urls import reverse

class News(models.Model):
    # id - INT пропускаем т.к. джанго сам создает id
    title = models.CharField(max_length = 150, verbose_name = 'Наименование')# title - Varchar
    content = models.TextField(blank = True, verbose_name = 'Контент')# content - Text. blank = True - необъязательно к заполнению
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')# created_at - DateTime. auto_now_add - Сохраняет дату тольк один раз
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Обновлено')# updated_at - DateTime. auto_now - Сохраняет дату при каждом редактирвании
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name = 'Фото', blank = True)# photo - Image
    is_published = models.BooleanField(default = True, verbose_name = 'Опубликовано')# is_published - Boolean
    category = models.ForeignKey('Category', on_delete = models.PROTECT,  verbose_name = 'Категория') #Связываем модели
    views = models.IntegerField(default = 0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs = {"pk": self.pk})

    def __str__(self):
        return self.title

    #Эти настройки будут применены и в пользовательскую часть
    class Meta:
        verbose_name = 'Новость' #Наименование модели в единственном числе
        verbose_name_plural = 'Новости' #Наименование модели во множественном числе
        ordering = ['-created_at', '-title']#Сортировка по дате, если дата будет идентична, то по тайтлу



class Category(models.Model):
    title = models.CharField(max_length = 150, db_index = True, verbose_name = 'Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs = {"category_id": self.pk})

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория' #Наименование модели в единственном числе
        verbose_name_plural = 'Категории' #Наименование модели во множественном числе
        ordering = ['title']#Сортировка по дате, если дата будет идентична, то по тайтлу
