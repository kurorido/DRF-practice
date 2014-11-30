from django.contrib import admin
from blog.models import Article, Tag

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'author']
    list_display = ('title', 'author', 'created')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)