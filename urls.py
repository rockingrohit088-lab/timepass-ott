from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.split if hasattr(admin.site, 'split') else admin.site.urls), # एडमिन पैनल का रास्ता
    path('', include('movies.urls')), # हमारे नेटफ्लिक्स होमपेज का रास्ता
]
