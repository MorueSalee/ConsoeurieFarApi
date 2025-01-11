from rest_framework.viewsets import ReadOnlyModelViewSet

from app.models import Category, Post
from app.serializer import CategorySerializer, PostSerializer


# Create your views here.

class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)

class PostViewset(ReadOnlyModelViewSet):

    serializer_class = PostSerializer

    def get_queryset(self):

        queryset = Post.objects.filter(active=True)

        category_id = self.request.GET.get('category_id')

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        return queryset
