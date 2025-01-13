from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.views import CategoryViewset, PostViewset, CommentViewset, AdminCategoryViewset, AdminPostViewset
from register.views import RegisterView

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')
router.register('post', PostViewset, basename='post')
router.register('comment', CommentViewset, basename='comment')
router.register('admin/category', AdminCategoryViewset, basename='admin-category')
router.register('admin/post', AdminPostViewset, basename='admin-post')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
]
