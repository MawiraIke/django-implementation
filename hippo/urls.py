from django.urls import path

from .views import HomePageView, NewPostView

urlpatterns = [path('', HomePageView.as_view(), name='home'),
               path('new', NewPostView.as_view(), name='new')]
