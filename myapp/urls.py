from django.urls import path
from . import views

urlpatterns = [
    path('create_instance/', views.create_instance, name='create_instance'),
    path('check_status/<str:instance_id>/', views.check_instance_status, name='check_instance_status'),
    path('display_image/<str:instance_id>/', views.display_image, name='display_image'),
]
