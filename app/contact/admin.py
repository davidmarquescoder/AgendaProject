from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email',)
    ordering = ('-id',) # Estou ordenando pelo id de forma decrescente
    list_filter = ('created_date',) # Criando um filtro por data de criação
    search_fields = ('first_name', 'last_name', 'email',) # Adicionando um campo de pesquisa para procurar contatos registrados
    list_per_page = 10 # Setando quanto valores serão exibidos em cada página
    list_max_show_all = 200 # Se clicar em 'mostrar tudo' ele exibirá no máximo 200 contatos
    list_editable = ('first_name',)
    list_display_links = ('phone', 'id',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',) # Estou ordenando pelo id de forma decrescente