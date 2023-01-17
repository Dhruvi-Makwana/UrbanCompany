from django.contrib import admin

# Register your models here.
from .models import User,Store,SetWeekDays,Category,Address


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'mobile_number', 'role', 'user_address', 'user_profile')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active','add_prefix','merchant_address','category','image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category','photo','is_deleted')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_diaply = ('id','address_line1','city_name','state_name','zipcode')


@admin.register(SetWeekDays)
class SetWeekDaysAdmin(admin.ModelAdmin):
    list_display = ('id','code','name','store_name')

