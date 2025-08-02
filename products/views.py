from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductsSerializer
from .models import Product


class GetProductsApiView(APIView):
    serializer_class = ProductsSerializer

    def get(self, request, pk=None):
        if pk:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response(data={
                    'message': 'no product with this id',
                    'status': 400
                })
            else:
                serializer = self.serializer_class(product)
                return Response(serializer.data, status=200)

        all_products = Product.objects.all()
        serializer = self.serializer_class(all_products, many=True)
        return Response(serializer.data, status=200)


