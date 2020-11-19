from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from reviews.views import MouseViewset, KeyboardViewset
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'mice', MouseViewset)
router.register(r'keyboards', KeyboardViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
