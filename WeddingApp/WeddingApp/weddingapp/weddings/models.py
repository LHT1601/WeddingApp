from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# Người dùng
class User(AbstractUser):  # AbstractUser sẽ có thông tin chứng thực sẵn
    avatar = models.ImageField(upload_to='images/%Y/%m', default=None)


# Sảnh cưới
class WeddingHall(models.Model):
    name = models.CharField(max_length=100, null=False)
    time_wedding = models.CharField(max_length=10, null=True)
    wedding_hall_images = models.ImageField(upload_to='images/%Y/%m', default=None)
    location = models.CharField(max_length=100, null=True)
    capacity = models.CharField(max_length=30, null=True)
    date_time_rent = models.DateTimeField(auto_now_add=True)
    wedding_hall_price = models.BigIntegerField()
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Dịch vụ
class Service(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    service_images = models.ImageField(upload_to='images/%Y/%m', default=None)
    price = models.BigIntegerField(null=False)
    time_rent = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # lưu luôn giờ tạo, auto_now_add: lưu thời gian tại thời điểm tạo lần đầu tiên
    # auto_add luôn thay đổi lại thời gian tại lúc được cập nhật

    def __str__(self):
        return self.name


# Đồ ăn uống
class DishesAndDrink(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    dishes_drinks_images = models.ImageField(upload_to='images/%Y/%m', default=None)
    price = models.BigIntegerField(null=False)
    amount = models.IntegerField()

    def __str__(self):
        return self.name


# Menu
class Menu(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, default=None)
    total_money = models.BigIntegerField(null=True)
    dishes_and_drink = models.ManyToManyField('DishesAndDrink', related_name='dishes_and_drink', blank=True)

    def __str__(self):
        return self.name


# Hóa đơn
class Receipt(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


# Tiệc Cưới
class Wedding(models.Model):
    wedding_name = models.CharField(max_length=50, null=False)
    number_desk = models.IntegerField()
    menu_price = models.BigIntegerField()
    service_price = models.BigIntegerField()
    price_rent = models.BigIntegerField()
    total_price = models.BigIntegerField()
    services = models.ManyToManyField('Service', blank=True, related_name='services')
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    wedding_hall = models.ForeignKey(WeddingHall, on_delete=models.SET_NULL, related_name='wedding_hall', null=True)

    def __str__(self):
        return self.wedding_name
