from django.shortcuts import render
from .models import User, Category, Store, SetWeekDays
from django.contrib.auth.views import (
    LoginView,
   )

from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView
from .forms import (
    AddUser,
    AddUserAddress,
    AddMerchant,
    AddStore,
    GetWeekday,
    UserLoginForm,
)


class HomePage(ListView):
    template_name = "user/homepage.html"
    model = Category

    def get_queryset(self):
        return self.model.objects.filter(categorychoice__isnull=False)


class StoreDetail(ListView):
    template_name = "user/store_detail.html"
    model = Store
    context_object_name = 'store'

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.kwargs.get('pk')).all()


class ShopDetail(DetailView):

    template_name = "user/shop_detail.html"
    model = Store


class TimeDetail(DetailView):

    template_name = "user/time_detail.html"
    model = SetWeekDays
    context_object_name = 'settime'

    def get_queryset(self):
        return self.objects.model.filter(store_name_id=self.kwargs.get('pk')).all()


class SelectUser(TemplateView):
    template_name = "user/userchoice.html"


class UserUpdate(UpdateView):
    model = User
    template_name = "user/userregister.html"
    fields = ['username', 'password', 'email', 'mobile_number', 'user_address']


class UserRegister(CreateView):
    form_class = AddUser, AddUserAddress

    def get(self, request, *args, **kwargs):
        return render(request, "user/userregister.html", {})

    def post(self, request, *args, **kwargs):
        adduser = AddUser(request.POST, request.FILES)
        adduser_address = AddUserAddress(request.POST)

        if adduser.is_valid() and adduser_address.is_valid():
            adduser = adduser.save()
            adduser.set_password(adduser.password)
            adduser.save()

            adduser_address = adduser_address.save()

        return render(
            request,
            "user/homepage.html",
            {"userform": adduser, "addressform": adduser_address},
        )


class MerchantRegister(CreateView):
    template_name = 'user/merchant.html'

    form_class = AddMerchant, AddStore, GetWeekday

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "user/merchant.html",
            {
                "merchantform": AddMerchant(),
                "addstore": AddStore(),
                "getweekday": GetWeekday(),

            },
        )

    def post(self, request, *args, **kwargs):

        merchant = AddMerchant(
            request.POST, initial={"role": "MERCHANT"})
        addstore = AddStore(request.POST, request.FILES)
        getweekday = GetWeekday(request.POST)

        if merchant.is_valid():
            merchant.save()
        breakpoint()
        if addstore.is_valid() and getweekday.is_valid():
            addstore.save()
            getweekday.save()

        return render(
            request,
            "user/homepage.html",
            {
                "merchantform": merchant,
                "addstore": addstore,
                "getweekday": getweekday,
            },
        )


class Login(LoginView):
    template_name = 'user/user_login.html'
    authentication_form = UserLoginForm
