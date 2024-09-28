from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!!")

class ProductView(APIView):
    def post(self,request):
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)




    def get(self,request):
        products= Product.objects.all()
        serializer = ProductSerializers(products,many=True)
        return Response(serializer.data)