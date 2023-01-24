from django.urls import path
from .views import HomePage, SelectUser, UserRegister,StoreDetail, Login,\
        ShopDetail, TimeDetail, UserStoreUpdate,SetShopTime


urlpatterns = [
        path("", HomePage.as_view(), name="homepage"),
        path("<pk>/update", UserStoreUpdate.as_view(), name='update'),
        # path("logout", Logout.as_view(), name='logout'),
        # re_path(r'^stores/(?P<category>[0-9])/$', StoreDetail.as_view(), name='stores'),
        path('stores/category=<int:pk>', StoreDetail.as_view(), name='stores'),
        path('shop/shop=<int:pk>', ShopDetail.as_view(), name='shop'),
        path('time/time=<int:pk>', TimeDetail.as_view(), name='time'),
        path('<pk>/update/shoptime/', SetShopTime.as_view(), name='shoptime'),
]
