from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter

class Category(models.Model):
    title    = models.CharField(max_length=100, verbose_name='عنوان دسته‌بندی')
    slug     = models.SlugField(max_length=50, unique=True, verbose_name='آدرس دسته‌بندی')
    status   = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ ها"
        ordering = ["position"]

    def __str__(self):
        return self.title




class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', 'منتشرشده')
    )
    title       = models.CharField(max_length=100, verbose_name='عنوان مقاله')
    slug        = models.SlugField(max_length=50, unique=True, verbose_name='آدرس مقاله')
    Category    = models.ManyToManyField(Category, verbose_name="دسته‌بندی")
    description = models.TextField(verbose_name='توضیحات')
    thumbnail   = models.ImageField(upload_to="images",verbose_name='تصویر مقاله')
    publish     = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    status      = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "تاریخ انتشار"