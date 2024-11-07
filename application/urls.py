from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL of the application
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), 
    path('base/', views.base, name='base'), 

]
