from django.urls import path
from movie.api import views as api_views

urlpatterns = [
    path('movies/', api_views.movie_list_create_api_view, name = "movie-list"),
    path('movies/<int:pk>', api_views.movie_detail_api_view, name = "movie-detail"),
]





