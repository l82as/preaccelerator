from django.db import models

# Create your models here.
class TopMenu(models.Model):

    choes = models.OneToOneField('Page', null=True, on_delete=models.PROTECT, verbose_name='Верхнее меню')
    menu_item = models.CharField(max_length=125, verbose_name='пункт меню')

    class Meta:
        verbose_name = "Верхнее меню"
        verbose_name_plural = "Верхнее меню"
    def __str__(self):
        return self.menu_item


class Page(models.Model):
    STATUS_CHOICES = (
        ('draft', 'В проекте'),
        ('published', 'Опубликовано'),
    )
    """
    STATUS_MENU = (
        ('top_menu', 'Верхнее меню'),
        ('bottom_menu', 'Нижнее меню'),
    )
    """
    title = models.CharField(max_length=255, verbose_name='название')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    body = models.TextField(blank=True, verbose_name='Содержимое')
    photo = models.ImageField(blank=True, upload_to="photos/%Y-%m-%d", verbose_name='фото')
    create = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    update = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    published = models.BooleanField(default=True, verbose_name='опубликовано')

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
    def __str__(self):
        return self.title