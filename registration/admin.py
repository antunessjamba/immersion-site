from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    # Campos exibidos na lista
    list_display = ('name', 'municipality', 'phone', 'gender', 'registration_date', 'status')
    
    # Filtro lateral para status
    list_filter = ('status', 'registration_date', 'gender')
    
    # Campo editável diretamente na lista
    list_editable = ('status',)
    
    # Campo de busca
    search_fields = ('name', 'municipality', 'phone')
    
    # Ordenação padrão por data (mais recente primeiro)
    ordering = ('-registration_date',)
    
    # Personalizar o layout da página de edição
    fields = ('name', 'municipality', 'phone', 'gender', 'registration_date', 'status')
    readonly_fields = ('registration_date',)  # Data só de leitura
    
    # Estilo personalizado para o admin (simples e bonito)
    class Media:
        css = {
            'all': ('/static/admin_custom.css',)  # Arquivo CSS personalizado
        }

# Criar um arquivo CSS personalizado (opcional, para embelezar)