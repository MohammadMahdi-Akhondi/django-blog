from django.db import models
from account.models import User
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from django.urls import reverse

    


# My managers

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status = 'p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status = True)


class Category(models.Model):
    title    = models.CharField(max_length=100, verbose_name='عنوان دسته‌بندی')
    slug     = models.SlugField(max_length=50, unique=True, verbose_name='آدرس دسته‌بندی')
    parent   = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیر‌دسته')
    status   = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ ها"
        ordering = ["parent__id","position"]

    def __str__(self):
        return self.title
    
    objects = CategoryManager()




class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', 'منتشرشده')
    )
    title       = models.CharField(max_length=100, verbose_name='عنوان مقاله')
    slug        = models.SlugField(max_length=50, unique=True, verbose_name='آدرس مقاله')
    author      = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    category    = models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="articles")
    description = models.TextField(verbose_name='محتوا')
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

    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])
    category_to_str.short_description = "دسته بندی"

    def published_categories(self):
        return self.category.filter(status = True)

    def thumbnail_tag(self):
        return format_html("<img width=150 height=100 style='border-radius: 5px' src={}>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "تصویر"

    def get_absolute_url(self):
        return reverse("account:home")

    objects = ArticleManager()