from django.urls import path, include
from mysite_app import views

urlpatterns = [
    path('home/', views.home_page, name="home"),
    path('view/', views.view_page, name="view"),
    path('edit/', views.edit_page, name="edit"),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/signup/", views.signup_page, name="signup"),
]
