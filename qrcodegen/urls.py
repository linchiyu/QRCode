from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ativos/", views.ativos, name="ativos"),
    path("inativos/", views.inativos, name="inativos"),
]
