from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL of the application
    path('about/', views.about, name='about'),  # Example 'about' page
    path('contact/', views.contact, name='contact'),  # Example 'about' page
    path('base/', views.base, name='base'),  # Example 'about' page

]
