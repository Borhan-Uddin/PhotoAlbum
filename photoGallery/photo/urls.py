from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add/',views.addPhoto, name='add'),
    path('view/<int:pk>/',views.photoView, name='photo'),
]