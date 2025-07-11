from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watch", views.watch, name="watch"),
    path("categories", views.categories, name="categories"),
    path("listings/<int:id>/", views.listings, name="listings"),
    path("categories/<str:catname>", views.cat, name="cat"),
    path("archive", views.archive, name="archive"),
]
