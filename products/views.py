from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
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
                    'message': 'No product with this id',
                    'status': 404
                }, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = self.serializer_class(product, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)

        all_products = Product.objects.all()
        serializer = self.serializer_class(all_products, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)