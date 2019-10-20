from django.urls import path

from .views import HomePageView, NewPostView, PostDetailView, PostUpdateView

urlpatterns = [
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('', HomePageView.as_view(), name='home'),
    path('post/new', NewPostView.as_view(), name='add_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail')]
