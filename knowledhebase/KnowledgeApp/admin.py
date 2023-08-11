from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title','text','created_at','author')
    list_display =('title','text','created_at','author')
    
# Register your models here.
admin.site.register(Article,ArticleAdmin)
