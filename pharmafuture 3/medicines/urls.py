from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_medicine, name='add_medicine'),
    path('search/', views.search_medicine, name='search_medicine'),
    path('<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
    path('<int:medicine_id>/remove/', views.remove_medicine, name='remove_medicine'),
    path('add-home-product/', views.add_home_product, name='add_home_product'),
    path('edit-home-product/<int:product_id>/', views.edit_home_product, name='edit_home_product'),
    path('delete-home-product/<int:product_id>/', views.delete_home_product, name='delete_home_product'),
    path('home-product/<int:product_id>/', views.home_product_detail, name='home_product_detail'),
    path('', views.search_medicine, name='medicine_list'),
]

