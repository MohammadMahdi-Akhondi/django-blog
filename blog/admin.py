from django.contrib import admin
from .models import Article, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Category, CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['-status', '-publish']

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.published_categories()])
    category_to_str.short_description = "دسته بندی"

admin.site.register(Article, ArticleAdmin)