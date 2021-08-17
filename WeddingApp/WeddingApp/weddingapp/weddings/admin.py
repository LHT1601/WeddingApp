from django.utils.html import mark_safe
from django.contrib import admin
from .models import User, WeddingHall, Service, DishesAndDrink, Menu


# Register your models here.

class WeddingHallAdmin(admin.ModelAdmin):
    list_display = ['name', 'time_wedding', 'active']
    search_fields = ['name', 'time_wedding']
    readonly_fields = ['image']

    def image(self, obj):
        if obj:
            return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120' />".format(img_url=obj.wedding_hall_images.name, alt=obj.name))


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    search_fields = ['name']
    readonly_fields = ['image']

    def image(self, obj):
        if obj:
            return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120' />".format(img_url=obj.service_images.name, alt=obj.name))


class DishesAndDrinkMenuInlineAdmin(admin.TabularInline):
    model = Menu.dishes_and_drink.through


class DishesAndDrinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount']
    search_fields = ['name']
    inlines = [DishesAndDrinkMenuInlineAdmin, ]
    readonly_fields = ['image']

    def image(self, obj):
        if obj:
            return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120' />".format(img_url=obj.dishes_drinks_images.name, alt=obj.name))


class MenuAdmin(admin.ModelAdmin):
    inlines = [DishesAndDrinkMenuInlineAdmin, ]


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['image']

    def image(self, obj):
        if obj:
            return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120' />".format(img_url=obj.avatar.name, alt=obj.last_name))


admin.site.register(User, UserAdmin)
admin.site.register(WeddingHall, WeddingHallAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(DishesAndDrink, DishesAndDrinkAdmin)
admin.site.register(Menu, MenuAdmin)
