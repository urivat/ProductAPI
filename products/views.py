from itertools import product
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer
from .models import Product
from products import serializer
from rest_framework.views import APIView
class ProductsList(APIView):

    def get(self , request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response (serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ProductsDetails(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404 
    #raise is setting an exception within the class if the results are not accepted in a try catch.
    # Can also be used to set a value to a bool if input is not valid. 
    def get(self, request, pk , format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer= ProductSerializer (product, data=request.data)
        if serializer.is_valid():     
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#product needs to be serialized in order to be translated.
#have to see if its valid which comes from if you have it or not.
    def delete(self, request, pk, format=None):
        product= self.get_object(pk)
        product.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
 









# @api_view(['GET', 'POST'])
# def products_list(request):
    
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_details(request,pk):
#         product = get_object_or_404(Product, pk=pk)
#         if request.method == 'GET':            
#             serializer = ProductSerializer(product)
#             return Response(serializer.data)

#         elif request.method == 'PUT':            
#             serializer = ProductSerializer(product, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
#         elif request.method == 'DELETE':
#             product.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

    
    
           
        




