from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import CategoryViewset, PostViewset

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')
router.register('post', PostViewset, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
