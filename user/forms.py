from django import forms
from .models import User, Address, Store, SetWeekDays,Category
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    pass


class AddUser(forms.ModelForm):
    user_profile = forms.ImageField()

    class Meta:
        model = User
        fields = ["username", "password", "mobile_number", "email", "user_profile", "user_address", "role"]


class AddUserAddress(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["address_line1", "city_name"]


class AddMerchant(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "mobile_number", "email", "role"]


class AddStore(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Store
        fields = ["name", "merchant_address", "add_prefix", "image", "category"]


class GetWeekday(forms.ModelForm):
    class Meta:
        model = SetWeekDays
        fields = ["code", "store_name", "start_time", "end_time"]
