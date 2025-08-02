from django.urls import path

from .views import ServiceGetApiView

urlpatterns = [
    path('get/', ServiceGetApiView.as_view()),
    path('get/<int:pk>/', ServiceGetApiView.as_view()),
]
