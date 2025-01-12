from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action

from app.models import Category, Post, Comment
from app.serializer import CategoryListSerializer, PostListSerializer, CategoryDetailSerializer, CommentSerializer, \
    PostDetailSerializer


# Create your views here.

class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

class CategoryViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)

class PostViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = PostListSerializer
    detail_serializer_class = PostDetailSerializer

    def get_queryset(self):

        queryset = Post.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    @action(detail=True, methods=['post'])
    def like(self, request, pk):
        self.get_object().like()
        return Response()

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk):
        self.get_object().dislike()
        return Response()


class CommentViewset(ReadOnlyModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):

        queryset = Comment.objects.filter(active=True)

        post_id = self.request.GET.get('post_id')

        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)

        return queryset

class AdminCategoryViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.all()

class AdminPostViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = PostListSerializer
    detail_serializer_class = PostDetailSerializer

    def get_queryset(self):
        return Post.objects.all()