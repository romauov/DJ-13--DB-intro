from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    # id;name;image;price;release_date;lte_exists
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='Модель телефона')
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(unique=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)