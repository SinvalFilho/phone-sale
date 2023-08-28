from django.contrib import admin
from .models import Avaliacao

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'celular', 'pontuacao', 'data_avaliacao')
    search_fields = ('usuario__username', 'celular__marca', 'celular__modelo')
    list_filter = ('pontuacao', 'data_avaliacao')  # Adicione os campos que deseja filtrar aqui
    ordering = ('-data_avaliacao',)

admin.site.register(Avaliacao, AvaliacaoAdmin)
