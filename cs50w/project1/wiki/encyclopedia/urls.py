from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("query", views.query, name="query"),
    path("randompage", views.randompage, name="randompage"),
    path("create", views.create, name="create"),
    path("<str:title>", views.entry, name="entry"),
    path('<str:title>/edit/', views.edit, name='edit')
]
