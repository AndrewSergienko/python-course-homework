from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('<int:id>/<slug:slug>/edit', views.product_edit, name='product_edit'),
    path('<int:id>/<slug:slug>/remove', views.product_remove, name='product_remove'),
]