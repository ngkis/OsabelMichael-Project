from django.urls import path
from .views import (
    HomePageView, PostListView, PostDetailView, 
    AnnouncementListView, FeedbackCreateView,
    CategoryListView, 
    CategoryDetailView,
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
