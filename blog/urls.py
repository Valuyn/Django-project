from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    TagListView,
    TagPostListView,
    CommentCreateView,
    # CommentUpdateView,
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-post"),
    path('tag/<str:title>', TagPostListView.as_view(), name="tag-post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('post/<int:pk>/comment-create/', CommentCreateView.as_view(), name='comment-create'),
    # path('post/<int:pk>/comment-update/', CommentUpdateView.as_view(), name='comment-update'),
    path('about/', views.about, name='blog-about'),
]
