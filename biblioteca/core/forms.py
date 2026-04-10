from django import forms
from .models import Books, Movies

class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = (
            "titulo",
            "diretor",
            "genero",
            "data_lancamento",
            "duracao",
            "streaming",
            "classificacao"
        )

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = (
            "isbn",
            "titulo",
            "autor",
            "genero",
            "ano_publicacao",
            "editora",
            "paginas",
            "status",
            "localizacao"
        )