from django.urls import path
from boda import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hola/<name>", views.hola_buenas, name="hola_buenas"),
    path("evento", views.evento, name="evento"),
]