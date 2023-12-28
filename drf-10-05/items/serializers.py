from rest_framework import serializers
from .models import Item, Category, CustomerOrder, SellRecord


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = '__all__'


class SellRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellRecord
        fields = '__all__'