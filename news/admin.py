from django.contrib import admin
from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'is_featured') 
    search_fields = ('title', 'summary', 'content')
    list_filter = ('is_featured', 'date_posted')