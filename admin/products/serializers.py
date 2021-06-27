from dataclasses import field
from rest_framework import serializers
from .models import Product

# tutorial-learning: a serializer will injest db data and transform it into json, which can be consumed by the web app
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'