from django.contrib import admin
from .models import (
    Usuario,
    Evento,
    Ocorrencia,
    Pendencia,
    Atividade,
    Fornecedor,
    Documento
)

admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Ocorrencia)
admin.site.register(Pendencia)
admin.site.register(Atividade)
admin.site.register(Fornecedor)
admin.site.register(Documento)