from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', ListApiView.as_view(), name='home'),
    path('item/<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:item_id>/', BuyItemView.as_view(), name='buy_item'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('intent/<int:item_id>/', BuyItemIntent.as_view(), name='intent'),
    path('add_to_cart/<int:item_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('my_cart/', CartListView.as_view(), name='my_cart'),
    path('my_cart/<int:order_id>', CartListView.as_view(), name='my_cart_delete_item'),
    path('buy_all/', BuyAllCart.as_view(), name='buy_from_cart'),
    path('create_coupone/', CreateCouponeView.as_view(), name='create_coupone'),
    
    path('api/v1/create_item', CreateItemView.as_view(), name='create_item'),
    path('api/v1/update_item/<int:pk>', UpdateItemView.as_view(), name='create_item'),
]