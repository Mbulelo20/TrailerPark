from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('browse', views.get_all, name='get_all'),
    path('review', views.review, name='review'),
    path('favorites', views.favorites, name='favorites'),
    path('search/', views.search_movie, name='search_movie'),
    path('movie/<str:id>', views.movie_item, name='movie_item'),
    path('movie/trailer/<str:id>/<str:link>/', views.movie_item, name='movie_item'),
]
