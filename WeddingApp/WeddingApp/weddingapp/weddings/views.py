from rest_framework.parsers import MultiPartParser
from .models import WeddingHall, Service, Menu, User
from .serializers import WeddingHallSerializer,ServiceSerializer, MenuSerializer, UserSerializer
from rest_framework import viewsets, permissions, generics
from django.http import HttpResponse


# Create your views here.


class WeddingHallViewSet(viewsets.ModelViewSet):
    queryset = WeddingHall.objects.filter(active=True)
    serializer_class = WeddingHallSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(active=True)
    serializer_class = ServiceSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.exclude(dishes_and_drink__isnull=False)
    serializer_class = MenuSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]


def index(request):
    return HttpResponse("weddings app")
