from rest_framework import serializers
from .models import Category, Item
from django.utils import timezone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        for i in "!@#$%^&*":
            if i in value:
                raise serializers.ValidationError("Name should not contain !@#$%^&*")
        return value


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def validate(self, data):
        if str(f'{data["category_id"]}C') not in data["QR"] and str(f'{data["price"]}P') not in data["QR"] \
                and str(f'{data["id"]}I') not in data["QR"]:
            raise serializers.ValidationError("QR should be cat_id + C, price + P, id + I")
        return data

# НЕ совсем понял с ForeignKey как поступить