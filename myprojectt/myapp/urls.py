# myapp/urls.py
from django.urls import path
from .views import add_view, default_view

urlpatterns = [
    path('', default_view, name='default_view'),
    path('add/', add_view, name='add_view'),
]
