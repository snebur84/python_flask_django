from django.db import models
from django.urls import reverse

class Books(models.Model):
    # Definindo as opções para o campo status
    STATUS_CHOICES = [
        ("disponivel", "Disponível"),
        ("reservado", "Reservado"),
        ("emprestado", "Emprestado"),
        ("eliminado", "Eliminado"),
    ]

    isbn = models.CharField("ISBN", max_length=150, unique=True)
    titulo = models.CharField("TÍTULO", max_length=100)
    autor = models.CharField("AUTOR", max_length=100)
    genero = models.CharField("GÊNERO", max_length=50)
    ano_publicacao = models.IntegerField("Ano de Publicação")
    editora = models.CharField("EDITORA", max_length=100)
    paginas = models.IntegerField("Total de Páginas") # Corrigido aqui
    status = models.CharField("STATUS", max_length=25, choices=STATUS_CHOICES, default="disponivel")
    localizacao = models.CharField("LOCAL", max_length=100)

    class Meta:
        ordering = ("isbn",)
        verbose_name = "Livro"
        verbose_name_plural = "Lista de Livros"

    def __str__(self) -> str:
        return f"{self.isbn} - Livro: {self.titulo}, Autor: {self.autor}, Status: {self.status}"
    
    def get_absolute_url(self):
        return reverse("core:book_update", kwargs={"isbn": self.isbn})
    
class Movies(models.Model):
    titulo = models.CharField("TÍTULO", max_length=100)
    diretor = models.CharField("DIRETOR", max_length=100)
    genero = models.CharField("GÊNERO", max_length=50)
    data_lancamento = models.IntegerField("DATA LANÇAMENTO")
    duracao = models.IntegerField("DURAÇÃO")
    streaming = models.CharField("STREAMING", max_length=100)
    classificacao = models.CharField("CLASSIFICAÇÃO", max_length=25)

    class Meta:
        ordering = ("data_lancamento", "titulo")
        verbose_name = "Filme"
        verbose_name_plural = "Lista de Filmes"

    def __str__(self) -> str:
        return f"{self.id} - Título: {self.titulo}, Diretor: {self.diretor}, Lançamento: {self.data_lancamento}"
    
    def get_absolute_url(self):
        return reverse("core:movie_update", kwargs={"id": self.id})