from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('weddinghalls', views.WeddingHallViewSet)
router.register('services', views.ServiceViewSet)
router.register('menus', views.MenuViewSet)
router.register('users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
