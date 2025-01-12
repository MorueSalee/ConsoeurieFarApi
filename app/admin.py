from django.contrib import admin

from app.models import Category, Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'author', 'category', 'likes', 'active')


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'active')

class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'post', 'likes', 'active')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
