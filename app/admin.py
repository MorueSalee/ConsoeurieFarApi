from django.contrib import admin

from app.models import Category, Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'category', 'active')


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'active')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
