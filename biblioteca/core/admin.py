from django.contrib import admin
from .models import Books, Movies

# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = (
        "id",
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
    
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "diretor",
        "data_lancamento",
        "genero",
        "streaming",
        "duracao",
        "classificacao"
    )
