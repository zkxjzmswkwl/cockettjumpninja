from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from reviews.views import MouseViewset, KeyboardViewset, MouseReviewViewset, KeyboardReviewViewset
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'mice', MouseViewset)
router.register(r'keyboards', KeyboardViewset)
router.register(r'mousereviews', MouseReviewViewset)
router.register(r'keyboardreviews', KeyboardReviewViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
