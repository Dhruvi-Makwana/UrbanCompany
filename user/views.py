from django.shortcuts import render
from .models import User, Category, Store, SetWeekDays
from django.contrib.auth.views import (
    LoginView,
   )

from django.views.generic import ListView, TemplateView, CreateView, DetailView
from .forms import (
    AddUser,
    AddUserAddress,
    AddMerchant,
    AddMerchantAddress,
    AddStore,
    GetWeekday,
    UserLoginForm,
)


class HomePage(ListView):
    template_name = "user/homepage.html"

    def get_queryset(self):
        return Category.objects.filter(is_deleted=False)


class StoreDetail(ListView):
    template_name = "user/store_detail.html"
    model = Store
    context_object_name = 'store'

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.kwargs.get('pk'))


class ShopDetail(DetailView):

    template_name = "user/shop_detail.html"
    model = Store


class TimeDetail(DetailView):

    template_name = "user/time_detail.html"
    model = SetWeekDays
    context_object_name = 'settime'
    # extra_context = {'settime': SetWeekDays.objects.all()}

    def get_queryset(self):

        return super().get_queryset().filter(store_name_id=self.kwargs.get('pk'))


class SelectUser(TemplateView):
    template_name = "user/userchoice.html"


class UserRegister(CreateView):
    form_class = AddUser, AddUserAddress

    def get(self, request, *args, **kwargs):
        return render(request, "user/userregister.html", {})

    def post(self, request, *args, **kwargs):
        adduser = AddUser(request.POST, request.FILES)
        adduser_address = AddUserAddress(request.POST)

        if adduser.is_valid() and adduser_address.is_valid():
            adduser = adduser.save()
            adduser_address = adduser_address.save()

        return render(
            request,
            "user/homepage.html",
            {"userform": adduser, "addressform": adduser_address},
        )


class MerchantRegister(CreateView):
    template_name = 'user/merchant.html'

    form_class = AddMerchant, AddMerchantAddress, AddStore, GetWeekday

    def get(self, request, *args, **kwargs):
        addmerchant_address = AddMerchantAddress()
        addstore = AddStore()
        getweekday = GetWeekday()

        return render(
            request,
            "user/merchant.html",
            {
                "merchantform": AddMerchant(),
                "addmerchantressform": addmerchant_address,
                "addstore": addstore,
                "getweekday": getweekday,

            },
        )

    def post(self, request, *args, **kwargs):
        cat = User.objects.all()
        merchant = AddMerchant(
            request.POST, request.FILES, initial={"role": "merchant"}
        )
        addmerchant_address = AddMerchantAddress(request.POST)
        addstore = AddStore(request.POST)
        getweekday = GetWeekday(request.POST)

        # breakpoint()
        if (
            merchant.is_valid()
            and addmerchant_address.is_valid()
            and addstore.is_valid()
        ):
            breakpoint()
            merchant.save()
            addmerchant_address.save()
            addstore.save()
        return render(
            request,
            "user/merchant.html",
            {
                "merchantform": merchant,
                "addmerchantaddressform": addmerchant_address,
                "addstore": addstore,
                "cat": cat,
                "getweekday": getweekday,
            },
        )


class Login(LoginView):
    template_name = 'user/user_login.html'
    authentication_form = UserLoginForm
