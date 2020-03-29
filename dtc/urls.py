from django.urls import path
from dtc import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
