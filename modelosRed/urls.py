from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('kruskal/', include('kruskal.urls')),
    path('flujoMaximo/', include('flujoMaximo.urls')),
    path('dijkstra/', include('dijkstra.urls')),
]
