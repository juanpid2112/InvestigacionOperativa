from django.contrib import admin
from django.urls import include, path

from .views import kruskal

urlpatterns = [
    path('resolver/', kruskal.as_view()),
]
