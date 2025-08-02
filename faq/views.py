from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FAQSerializer
from .models import FAQ


class FAQGetApiView(APIView):
    serializer_class = FAQSerializer


    def get(self, request):
        all_faqs = FAQ.objects.all()
        serializer = self.serializer_class(all_faqs, many=True)
        return Response(serializer.data, status=200)
