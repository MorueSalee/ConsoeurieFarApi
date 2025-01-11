from rest_framework.serializers import ModelSerializer

from app.models import Category, Post


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'active']

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'active', 'date_posted', 'date_updated']