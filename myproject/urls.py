from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.write),
    path('', include('accounts.urls')), # متصل کردن بخش احراز هویت
]
