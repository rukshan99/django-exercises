from django.urls import path
from . import views

urlpatterns = [
    path('simple_template_view', views.simple_template_view, name='simple_template_view'),
    path('<int:num_page>', views.num_page_view, name='num_page-view'),
    path('<str:topic>', views.news_view, name='news_view'),
    path('<int:num1>/<int:num2>', views.add_view, name='add_view')
]