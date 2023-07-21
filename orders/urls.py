from django.urls import path

from orders.views import OrderCreateVew, SuccessTemplateView, CanceledTemplateView

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateVew.as_view(), name='order_create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-canceled/', CanceledTemplateView.as_view(), name='order_canceled'),
]
