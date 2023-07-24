from rest_framework.generics import ListAPIView

from products.models import Product
from products.serializer import ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
