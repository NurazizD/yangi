from django.urls import path
from .views import Post_view

urlpatterns = [
    path('',Post_view.as_view()),
]