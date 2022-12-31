from django.urls import path
from . import views

# This registers the app namespace
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name='example_view_path'),
    path('variables', views.variable_view, name='variable_view_path')
]