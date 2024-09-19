from django.urls import path
from . import views

urlpatterns = [
    path('class_view/', views.class_view, name='class_view'),
    path('function_view/', views.function_view, name='function_view'),
]