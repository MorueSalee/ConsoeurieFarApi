from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import Category, Post, Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'likes', 'date_posted', 'date_updated', 'active']

class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'author', 'content', 'likes', 'date_posted', 'date_updated', 'active']

    def validate_name(self, value):
        if Post.objects.filter(title=value).exists():
            raise serializers.ValidationError('Post title already exists')
        return value

class PostDetailSerializer(ModelSerializer):

    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields =  ['id', 'title', 'category', 'author', 'content', 'likes', 'date_posted', 'date_updated', 'active', 'comments']

    def get_comments(self, instance):

        queryset = instance.comments.filter(active=True)

        serializer = CommentSerializer(queryset, many=True)

        return serializer.data

class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'active']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError('Category name already exists')
        return value

class CategoryDetailSerializer(ModelSerializer):

    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'active', 'posts']

    def get_posts(self, instance):

        queryset = instance.posts.filter(active=True)

        serializer = PostListSerializer(queryset, many=True)

        return serializer.data
