from django.contrib import admin
from django.urls import path

from app.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
