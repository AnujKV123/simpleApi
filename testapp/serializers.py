from rest_framework import serializers
from .models import productMainModel

class ProductSerializer (serializers.ModelSerializer):

  class Meta:
    model = productMainModel
    exclude = ['unique_code']