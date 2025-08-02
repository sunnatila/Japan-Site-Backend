from django.urls import path
from .views import ContactCreateApiView


urlpatterns = [
    path('create/', ContactCreateApiView.as_view())
]