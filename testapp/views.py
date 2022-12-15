from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import productMainModel
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def Products(request):
    products = productMainModel.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response({'spam': serializer.data}, status = status.HTTP_200_OK)

@api_view(['GET'])
def getProduct(request, id):
    product = productMainModel.objects.get(pk = id)
    return Response({'status': 'success', 'user': ProductSerializer(product).data})

