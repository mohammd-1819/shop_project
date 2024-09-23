from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/list', views.PostListView.as_view(), name='post-list'),
    path('search', views.BlogSearchView.as_view(), name='blog-search'),
    path('post/category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),

]
