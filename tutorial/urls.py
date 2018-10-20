from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api_auth/', include('rest_framework.urls',
        namespace='rest_framework'))

]
