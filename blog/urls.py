from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogMainPageView.as_view(), name='blog-main'),
]
