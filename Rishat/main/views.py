"""Build a full, working payments integration using Stripe Stripe Checkout"""

import stripe
from django.conf import settings
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Item, Order, Discount
from .serializers import ItemSerializers
from .services import order_summ, list_items


stripe.api_key = settings.STRIPE_API_SKEY


class ListApiView(APIView):
    """List All items"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response({'items': Item.objects.all()})


class CreateItemView(generics.CreateAPIView):
    serializer_class = ItemSerializers


class UpdateItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ItemDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail_item.html'

    def get(self, request, item_id):
        return Response({'item': get_object_or_404(Item, id=item_id), 'key': settings.STRIPE_API_PKEY})


class BuyItemView(APIView):

    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        if Discount.objects.filter(item=item_id).exists():
            coupon = Discount.objects.get(item=item_id).get_code()
            session = stripe.checkout.Session.create(
            line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
            }],
            mode='payment',
            discounts=[{
                'coupon': coupon,
            }],
            success_url='http://127.0.0.1:8000/success',
            cancel_url='http://127.0.0.1:8000/cancel',
            )
        else:
            session = stripe.checkout.Session.create(
            line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success',
            cancel_url='http://127.0.0.1:8000/cancel',
            )
        return Response({'id': session.id})


class BuyItemIntent(APIView):

    def post(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        intent = stripe.PaymentIntent.create(
            amount = int(item.price * 100),
            currency = item.currency,
            payment_method_types = ["card"],
            statement_descriptor = "Custom descriptor",
            metadata = {"item_id": item_id},
        )
        return Response({'id': intent['id']})


class AddToCart(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, item_id):
        if request.user:
            Order.objects.create(item_id=item_id, user=request.user)
            return Response({'success': True, 'items': Item.objects.all()}) 
        else:
            return Response({'error': True})


class CartListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cart.html'

    def get(self, request):
        orders = Order.objects.filter(user=request.user).select_related('item')
        order_sum = order_summ(orders)
        return Response({'orders': orders, 'order_sum': order_sum})

    def post(self, request, order_id):
        obj = get_object_or_404(Order, user=request.user, item_id=order_id)
        obj.delete()
        return redirect(reverse('my_cart'))


class BuyAllCart(APIView):

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        session = stripe.checkout.Session.create(
        line_items=list_items(orders),
        mode='payment',
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:8000/cancel',
        )
        orders = Order.objects.filter(user=request.user)
        orders.delete()
        orders.update()
        return Response({'id': session.id})


class CreateCouponeView(APIView):

    def get(self, request):
        session = stripe.Coupon.create(
            percent_off=25,
            duration="repeating",
            duration_in_months=3,
        )
        item = Item.objects.get(pk=1)
        if Discount.objects.filter(item=item).exists():
            return redirect(reverse('home'))
        else:
            Discount.objects.create(item=item, code=session.id, procent=25)
            return Response({'id': session.id})
