from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("brasil", views.brasil, name="brasil"),
    path("argentina", views.argentina, name="argentina"),
    path("uruguai", views.uruguai, name="uruguai"),
]