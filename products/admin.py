from django.contrib import admin
from .models import Celular

@admin.register(Celular)
class CelularAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'preco', 'estoque', 'data_atualizacao', 'foto', 'publicada')
    list_display_links = ('id', 'marca', 'modelo', 'data_atualizacao')  # Removido 'publicada' de list_display_links
    list_filter = ('marca', 'publicada', 'data_atualizacao')
    search_fields = ('marca', 'modelo', 'data_atualizacao')
    list_editable = ('publicada',)
    ordering = ('marca', 'modelo', 'data_atualizacao')
    list_per_page = 20

    fieldsets = (
        (None, {'fields': ('marca', 'modelo', 'preco', 'estoque', 'foto', 'publicada')}),
    )
