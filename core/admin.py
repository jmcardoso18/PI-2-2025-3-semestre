from django.contrib import admin
from .models import Servico, Usuario, Evento, Ocorrencia, Pendencia, Atividade, Fornecedor, Documento

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco')
    search_fields = ('titulo',)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local', 'tipo')
    list_filter = ('data', 'tipo')

# Registrando todos os modelos
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Usuario)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Ocorrencia)
admin.site.register(Pendencia)
admin.site.register(Atividade)
admin.site.register(Fornecedor)
admin.site.register(Documento)