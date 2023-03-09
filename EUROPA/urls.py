from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portugal", views.portugal, name="portugal"),
    path("espanha", views.espanha, name="espanha")
]