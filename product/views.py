from rest_framework import viewsets

from product.models import Product
from product.serializer import SnackSerializer


class SnackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = SnackSerializer
