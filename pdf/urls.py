from django.urls import path
from . import views

urlpatterns = [
  path('accept/', views.accept, name='accept'),
  path('accept/<int:id>', views.resume, name='resume'),
  path('list/', views.list, name='list')
]