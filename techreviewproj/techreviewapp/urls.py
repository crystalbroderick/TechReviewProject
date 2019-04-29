from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'), # empty quotes only work for index; index is default
    path('getTypes/', views.getTypes, name='types')
]