from django.urls import path
from .views import VideoGetApiView

urlpatterns = [
    path('get/', VideoGetApiView.as_view())
]
