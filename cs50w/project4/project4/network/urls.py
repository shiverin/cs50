
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path('<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    path("profile/<str:username>/follow/", views.toggle_follow, name="toggle_follow"),
    path('<int:post_id>/edit/', views.edit, name='edit'),
]
