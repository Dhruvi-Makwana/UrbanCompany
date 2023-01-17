from django.urls import path
from .views import HomePage, SelectUser, UserRegister, MerchantRegister, StoreDetail, Login, ShopDetail,TimeDetail


urlpatterns = [
        path("", HomePage.as_view(), name="homepage"),
        path("login", Login.as_view(), name='login'),
        # path("logout", Logout.as_view(), name='logout'),
        path("select_user/", SelectUser.as_view(), name="selectuser"),
        path("select_user/user_register", UserRegister.as_view(), name="userregister"),
        path(
            "select_user/merchant_register",
            MerchantRegister.as_view(),
            name="merchantregister",
        ),
        # re_path(r'^stores/(?P<category>[0-9])/$', StoreDetail.as_view(), name='stores'),
        path('stores/?category=<int:pk>', StoreDetail.as_view(), name='stores'),
        path('shop/?shop=<int:pk>', ShopDetail.as_view(), name='shop'),
        path('time/?time=<int:pk>', TimeDetail.as_view(), name='time'),
]
