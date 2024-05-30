from rest_framework import serializers
from .models import CategorySings, SingsRoad


class CategorySingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySings
        fields = "__all__"


class SingRoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingsRoad
        fields = "__all__"


class DetailSingsRoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingsRoad
        fields = "__all__"