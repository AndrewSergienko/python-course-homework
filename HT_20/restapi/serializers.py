from rest_framework.serializers import HyperlinkedModelSerializer
from shop.models import Product, Category


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'available']


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'products']