from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_matches, name="matches"),
    path("add_match/", views.add_match, name="add_match"),
    path("edit_match/<int:id>/", views.edit_match, name="edit_match"),
    path("delete_match/<int:id>/", views.delete_match, name="delete_match"),
]
