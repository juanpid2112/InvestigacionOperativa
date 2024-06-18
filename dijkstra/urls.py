from django.urls import path
from . import views

urlpatterns = [
    path('resolver/', views.DijkstraView.as_view(), name='kruskal'),
]
