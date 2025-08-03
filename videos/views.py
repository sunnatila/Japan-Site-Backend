from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video
from .serializers import VideoSerializer


class VideoGetApiView(APIView):
    serializer_class = VideoSerializer


    def get(self, request):
        videos = Video.objects.all()
        serializer = self.serializer_class(videos, many=True)
        return Response(serializer.data, status=200)

