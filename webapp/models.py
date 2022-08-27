from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

categories = [
    ('cat1', 'Категория 1'),
    ('cat2', 'Категория 2'),
    ('cat3', 'Категория 3'),
    ('cat4', 'Категория 4'),
    ('other', 'Разное')

]

stars = [
    ('1', '*'),
    ('2', '**'),
    ('3', '***'),
    ('4', '****'),
    ('5', '*****')
]


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование товара')
    category = models.CharField(choices=categories, default='other', max_length=5, verbose_name='Категория товара')
    description = models.TextField(blank=True, max_length=2000, verbose_name='Описание товара')
    image = models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение товара')

    def get_global_ratings(self):
        ratings = 0
        for i in self.reviews.all():
            ratings += int(i.rating)
        return '*' * int(ratings / self.reviews.all().count())

    def __str__(self):
        return f'{self.id} {self.name} {self.category}'

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Товар')
    text = models.TextField(max_length=3000, verbose_name='Отзыв о товаре')
    rating = models.CharField(choices=stars, default=1, max_length=1, verbose_name='Оценка')
    moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    def __str__(self):
        return f'{self.author} {self.product.name} {self.rating}'

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
