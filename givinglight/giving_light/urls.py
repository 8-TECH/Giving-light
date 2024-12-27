from django.urls import path
from . import views

urlpatterns = [
    path('', views.giving_light, name="giving_light"),
]
