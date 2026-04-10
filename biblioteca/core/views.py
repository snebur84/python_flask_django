from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Books, Movies
from .forms import MoviesForm, BooksForm
from rest_framework import viewsets
from .serializers import BooksSerializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BooksListView(ListView):
    template_name = "core/books_list.html"
    paginate_by = 25
    model = Books

    def get_queryset(self, **kwargs):
        object_list = super().get_queryset(**kwargs).order_by('-isbn')
        return object_list

class MoviesListView(ListView):
    template_name = "core/movies_list.html"
    paginate_by = 25
    model = Movies

    def get_queryset(self, **kwargs):
        object_list = super().get_queryset(**kwargs)
        return object_list

class MoviesCreateView(CreateView):
    template_name = "core/movie_create.html"
    form_class = MoviesForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:movies_list")

class BooksCreateView(CreateView):
    template_name = "core/book_create.html"
    form_class = BooksForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:books_list")
    
class BooksUpdateView(UpdateView):
    template_name = "core/book_create.html"
    form_class = BooksForm

    def get_object(self):
        isbn = self.kwargs.get("isbn")
        return get_object_or_404(Books, isbn=isbn)

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("core:books_list")

class MoviesUpdateView(UpdateView):
    template_name = "core/movie_create.html"
    form_class = MoviesForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Movies, id=id)

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("core:movies_list")