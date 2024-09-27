from django.shortcuts import render
from rest_framework import viewsets

from networknode.models import NetworkNode, Product
from networknode.permissions import IsActiveEmployee
from networknode.serializers import NetworkNodeSerializer, ProductSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee, ]

    # Фильтрация по стране
    def get_queryset(self):
        country = self.request.query_params.get('country')
        if country:
            return self.queryset.filter(country=country)
        return self.queryset

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee, ]