import stripe
from http import HTTPStatus

from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.conf import settings

from orders.forms import OrderForm
from common.views import CommonMixin

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(CommonMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Заказ успешно оплачен!'


class CanceledTemplateView(CommonMixin, TemplateView):
    template_name = 'orders/cancel.html'
    title = 'Ошибка оплаты'


class OrderCreateVew(CommonMixin, CreateView):
    title = 'Оформление заказа'
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateVew, self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1NWHYhCEb9bne1UWbZXflksV',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_canceled')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateVew, self).form_valid(form)
