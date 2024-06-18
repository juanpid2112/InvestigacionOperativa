from django.urls import path
from . import views

urlpatterns = [
    path('resolver/', views.KruskalView.as_view(), name='kruskal'),
]
