from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogMainPageView.as_view(), name='blog-main'),
    path('new/', views.BlogCreateView.as_view(), name='blog-create'),
]
