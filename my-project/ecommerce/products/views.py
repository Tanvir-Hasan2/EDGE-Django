from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from rest_framework.permissions import IsAuthenticated



# Create your views here. all api created here

def index(request):
    return HttpResponse("Hello, world!!")

class ProductView(APIView):
         permission_classes = [IsAuthenticated]


#post api
class ProductView(APIView):

    #post api
    def post(self,request):
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    # get api single and list of product
    def get(self,request, id=None):
        if id:
            try:
              product = Product.objects.get(id=id)
            except Product.DoesNotExist:
                raise Http404
            serializer = ProductSerializers(product)
            return Response(serializer.data)
        else:    
          products= Product.objects.all()
          serializer = ProductSerializers(products,many=True)
          return Response(serializer.data)
        

    

     # put method for updating a product
    def put(self, request, id):
         if id:
             try:
                 product = Product.objects.get(id=id)
             except Product.DoesNotExist:
                 raise Http404
             serializer = ProductSerializers(product, data= request.data)
             if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status = status.HTTP_200_OK)
             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
         return Response({"error": "ID is required for updating a product"},status = status.HTTP_400_BAD_REQUEST)
    
    #delete operation
    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

        product.delete()
        serializer = ProductSerializers(product)
        return Response(serializer.data)  

    # put method for updating a product
    def patch(self, request, id):
         if id:
             try:
                 product = Product.objects.get(id=id)
             except Product.DoesNotExist:
                 raise Http404
             serializer = ProductSerializers(product, data= request.data,partial = True)
             if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status = status.HTTP_200_OK)
             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
         return Response({"error": "ID is required for updating a product"},status = status.HTTP_400_BAD_REQUEST)
    
    