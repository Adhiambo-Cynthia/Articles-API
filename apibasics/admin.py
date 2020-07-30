from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','title', 'author', 'created')
    list_display_links=('id', 'title')

admin.site.register(Article, ArticleAdmin)


