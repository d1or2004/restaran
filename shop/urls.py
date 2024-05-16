from django.urls import path
from .views import LandingView, ShopView, ShopDetailView

urlpatterns = [
    path('shop/', LandingView.as_view(), name='landing-shop'),
    path('shop_shop/', ShopView.as_view(), name='shop'),
    path('shop_detail/', ShopDetailView.as_view(), name='shop-detail'),
]
