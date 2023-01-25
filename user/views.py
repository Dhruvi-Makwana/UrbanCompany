from django.shortcuts import render
from .models import User, Category, Store, SetWeekDays
from django.contrib.auth.views import (
    LoginView,
   )
from django.http import JsonResponse
from django.core import serializers

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
        # return self.model.objects.filter(store_category__isnull=False)
        return self.model.objects.prefetch_related('store_category').filter(store_category__isnull=False)


class StoreDetail(ListView):
    template_name = "user/store_detail.html"
    model = Store
    context_object_name = 'store'

    def get_queryset(self):
        return super().get_queryset().filter(category_id=self.kwargs.get('pk')).all()


class ShopDetail(DetailView):

    template_name = "user/shop_detail.html"
    model = Store


class TimeDetail(ListView):

    template_name = "user/time_detail.html"
    model = SetWeekDays

    def get_queryset(self):
        return SetWeekDays.objects.filter(store_name_id=self.kwargs.get('pk')).all()


class SelectUser(TemplateView):
    template_name = "user/userchoice.html"


class SetShopTime(CreateView):
    template_name = "user/managetime.html"
    model = SetWeekDays
    form_class = GetWeekday

    def get(self, request, *args, **kwargs):
        return render(
            request,"user/managetime.html",{
                "getweekday": GetWeekday(),
            },
        )

    def post(self, request, *args, **kwargs):
        getweekday = GetWeekday(request.POST)
        if getweekday.is_valid():
            getweekday.save()
        return render(
            request,"user/managetime.html", {
                "getweekday": getweekday,
            },
        )


class UserStoreUpdate(CreateView):
    model = Store
    template_name = "user/merchant.html"
    form_class = AddStore

    def get_cities(request):
        get_category = Category.objects.all()
        json_data = serializers.serialize("json", get_category)
        return JsonResponse(json_data, safe=False)

    def get(self, request, *args, **kwargs):
        return render(request, "user/merchant.html", {
                "addstore": AddStore(),
            },
        )

    def post(self, request, *args, **kwargs):
        breakpoint()
        addstore = AddStore(request.POST, request.FILES)

        if addstore.is_valid():
            addstore.save()

        return render(request, "user/homepage.html", {
                "addstore": addstore,
            },
        )


class UserRegister(CreateView):
    form_class = AddUser, AddUserAddress

    def get(self, request, *args, **kwargs):
        adduser = AddUser()
        return render(request, "user/userregister.html", {"userform": adduser})

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

    form_class = AddStore, GetWeekday

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "user/merchant.html",
            {
                "addstore": AddStore(),
                "getweekday": GetWeekday(),
            },
        )

    def post(self, request, *args, **kwargs):
        addstore = AddStore(request.POST, request.FILES)
        getweekday = GetWeekday(request.POST)

        if addstore.is_valid() and getweekday.is_valid():
            addstore.save()
            getweekday.save()

        return render(
            request,
            "user/homepage.html",
            {
                "addstore": addstore,
                "getweekday": getweekday,
            },
        )


class Login(LoginView):
    template_name = 'user/user_login.html'
    authentication_form = UserLoginForm
