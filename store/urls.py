
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:has_category_name>/', views.store, name='product_category'),
    path('<slug:has_category_name>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
