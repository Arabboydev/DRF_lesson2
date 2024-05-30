from rest_framework import serializers
from .models import SignsRoad, CategorySigns


class CategorySignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySigns
        fields = "__all__"


class SignsRoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignsRoad
        fields = "__all__"


class DetailSignsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = SignsRoad
        fields = "__all__"