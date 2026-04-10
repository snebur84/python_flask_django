from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# O Router registra automaticamente as rotas para o ViewSet
router = DefaultRouter()
router.register(r'books-api', views.BooksViewSet)

app_name = "core"

urlpatterns = [
    path("books/", views.BooksListView.as_view(), name="books_list"),
    path("movies/", views.MoviesListView.as_view(), name="movies_list"),
    path("books/create", views.BooksCreateView.as_view(), name="book_create"),
    path("movies/create", views.MoviesCreateView.as_view(), name="movie_create"),
    path("books/<str:isbn>/", views.BooksUpdateView.as_view(), name="book_update"),
    path("movies/<int:id>/", views.MoviesUpdateView.as_view(), name="movie_update"),
    path("api/", include(router.urls)),
]


