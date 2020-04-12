from django.urls import path
from dtc import views

urlpatterns = [
    path('demo/', views.hello_world, name='hello_world'),
    path('', views.welcome, name='hello_world'),
    path('maps/', views.maps, name='maps'),
    path('routes/', views.routes, name='routes'),
    path('serializer/', views.exampleSerializer, name='example_serializer'),
]
