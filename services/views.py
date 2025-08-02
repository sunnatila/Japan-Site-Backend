from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Service
from .serializers import ServiceSerializer

class ServiceGetApiView(APIView):
    serializer_class = ServiceSerializer


    def get(self, request, pk=None):
        if pk:
            try:
                service = Service.objects.get(pk=pk)

            except Service.DoesNotExist:
                return Response(data={
                    'message': 'service not found with this id',
                    'status': 404
                })
            else:
                serializer = self.serializer_class(service)
                return Response(serializer.data, status=200)

        all_services = Service.objects.all()
        serializer = self.serializer_class(all_services, many=True)
        return Response(serializer.data, status=200)

