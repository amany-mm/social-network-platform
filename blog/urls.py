from django.urls import path, include
from rest_framework import routers

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    FollowsListView,
    FollowersListView,
    postpreference,
    post_list)
from .import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),

    path('post/add/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:postid>/preference/<int:userpreference>',
         postpreference, name='postpreference'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/<str:username>/follows',
         FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers',
         FollowersListView.as_view(), name='user-followers'),


    path('l/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/posts', post_list)
]
