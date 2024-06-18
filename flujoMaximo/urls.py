from django.urls import path
from . import views

urlpatterns = [
    path('resolver/', views.FlujoMaximoView.as_view(), name='flujo_maximo'),
]