from django.contrib import admin
from django.urls import path

from app.views import home

urlpatterns = [
    path('', home, name='home'),
    path('xpto', home, name='home2'),
    path('admin/', admin.site.urls),
]
