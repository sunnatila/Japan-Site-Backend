from django.urls import path
from .views import GetProductsApiView

urlpatterns = [
    path('get/', GetProductsApiView.as_view()),
    path('get/<int:pk>/', GetProductsApiView.as_view()),

]