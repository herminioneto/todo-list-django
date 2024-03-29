from django.contrib import admin
from django.urls import path

from todos.views import home

# Adicionar urls para cada view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
