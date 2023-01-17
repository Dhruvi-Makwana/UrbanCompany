from django import forms
from .models import User, Address, Store, SetWeekDays
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    pass


class AddUser(forms.ModelForm):
    user_profile = forms.ImageField()

    class Meta:
        model = User
        fields = ["username", "password", "mobile_number", "email", "user_profile"]


class AddUserAddress(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["address_line1", "city_name"]


class AddMerchant(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "mobile_number", "email", "role"]


class AddMerchantAddress(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["address_line1","city_name"]


class AddStore(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Store
        fields = ["name", "latitude", "longitude", "merchant_address", "image","category"]


class GetWeekday(forms.ModelForm):
    class Meta:
        model = SetWeekDays
        fields = ["name"]
