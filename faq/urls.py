from django.urls import path
from .views import FAQGetApiView


urlpatterns = [
    path('get/', FAQGetApiView.as_view())
]