# setting_template/urls.py

from django.urls import path
from . import views
from .views import render_view

urlpatterns = [
    path('', views.index, name='index'),
    
    path("api/render/", render_view),
]