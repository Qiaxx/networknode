from rest_framework import serializers
from networknode.models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'release_date', 'network_node']


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt_to_supplier',
                  'created_at', 'products']
        read_only_fields = ['debt_to_supplier']
