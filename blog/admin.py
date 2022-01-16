from django.contrib import admin
from .models import Article, Category

# Admid header & admin title
admin.site.site_header = "مدیریت وبلاگ"
admin.site.site_title = "مدیریت وبلاگ"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}
    actions = ['make_publish', 'make_draft']

    def make_publish(self, request, queryset):
        rows_updated = queryset.update(status = True)
        if rows_updated == 1:
            message_bit = '.با موفقیت نمایش داده شد'
        else:
            message_bit = '.با موفقیت نمایش داده شدند'
        self.message_user(request, "{} دسته بندی {}".format(rows_updated, message_bit))
    make_publish.short_description = "نشان دادن دسته بندی های انتخاب شده"

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status = False)
        if rows_updated == 1:
            message_bit = '.با موفقیت مخفی شد'
        else:
            message_bit = '.با موفقیت مخفی شدند'
        self.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
    make_draft.short_description = "مخفی کردن دسته بندی های انتخاب شده"

admin.site.register(Category, CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'author', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['-status', '-publish']
    actions = ['make_publish', 'make_draft']

    def make_publish(self, request, queryset):
        rows_updated = queryset.update(status = 'p')
        if rows_updated == 1:
            message_bit = 'با موفقیت منتشر شد.'
        else:
            message_bit = 'با موفقیت منتشر شدند.'
        self.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
    make_publish.short_description = "منتشر کردن مقالات انتخاب شده"

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status = 'd')
        if rows_updated == 1:
            message_bit = 'با موفقیت پیش‌نویش شد.'
        else:
            message_bit = 'با موفقیت پیش‌نویس شدند.'
        self.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))
    make_draft.short_description = "پیش‌نویس کردن مقالات انتخاب شده"


admin.site.register(Article, ArticleAdmin)