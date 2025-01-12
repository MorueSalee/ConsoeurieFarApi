from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import CategoryViewset, PostViewset, CommentViewset, AdminCategoryViewset, AdminPostViewset

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')
router.register('post', PostViewset, basename='post')
router.register('comment', CommentViewset, basename='comment')
router.register('admin/category', AdminCategoryViewset, basename='admin-category')
router.register('admin/post', AdminPostViewset, basename='admin-post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
