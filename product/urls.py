from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('list', views.ProductListView.as_view(), name='product-list'),
    path('product/search', views.ProductSearchView.as_view(), name='product-search')

]
