from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'price')
        read_only_fields = ("author",)

class ProductDetailSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("like_users")
        return ret