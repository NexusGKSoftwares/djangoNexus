from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home view for the student app
]
