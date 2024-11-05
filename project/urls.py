from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('application/', include('application.urls')),  # Include your application's URLs
]
