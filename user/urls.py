from django.urls import path
from .views import HomePage, SelectUser, UserRegister,StoreDetail,\
        ShopDetail, TimeDetail, UserStoreUpdate,SetShopTime


urlpatterns = [
        path("", HomePage.as_view(), name="homepage"),
        path("<pk>/update", UserStoreUpdate.as_view(), name='update'),
        path('stores/category=<int:pk>', StoreDetail.as_view(), name='stores'),
        path('shop/shop=<int:pk>', ShopDetail.as_view(), name='shop'),
        path('time/time=<int:pk>', TimeDetail.as_view(), name='time'),
        path('<pk>/update/shoptime/', SetShopTime.as_view(), name='shoptime'),
        path('get_category/', UserStoreUpdate.get_cities, name='get_cities'),
]
