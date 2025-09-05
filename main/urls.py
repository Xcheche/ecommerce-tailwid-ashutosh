from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]
