from django.db import models

# -------------------------------------------------------------------
# Modelo USUARIO
# -------------------------------------------------------------------
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255) # P/ produção, use o User nativo do Django
    tipo = models.CharField(max_length=255)
    celular = models.CharField(max_length=15, blank=True, null=True)
    pix = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nome

# -------------------------------------------------------------------
# Modelo EVENTO
# -------------------------------------------------------------------
class Evento(models.Model):
    # Relação: Um Usuário pode ter vários Eventos
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="eventos")
    id_cliente = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)
    convidados = models.CharField(max_length=255) # Considere IntegerField se for só número

    def __str__(self):
        # Ex: "Casamento João e Maria (20/12/2025)"
        return f"{self.nome} ({self.data.strftime('%d/%m/%Y')})"

# -------------------------------------------------------------------
# Modelos "Filhos" do Evento
# -------------------------------------------------------------------

class Ocorrencia(models.Model):
    # Relação: Um Evento pode ter várias Ocorrências
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="ocorrencias")
    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tipo} - {self.evento.nome}"

class Pendencia(models.Model):
    # Relação: Um Evento pode ter várias Pendências
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="pendencias")
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data = models.CharField(max_length=255) # Considere DateField ou DateTimeField
    status = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Pendências"

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    # Relação: Um Evento pode ter várias Atividades
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="atividades")
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    horario = models.CharField(max_length=255) # Considere TimeField
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

# -------------------------------------------------------------------
# Modelos FORNECEDOR e DOCUMENTO
# -------------------------------------------------------------------

class Fornecedor(models.Model):
    # Relação: Um Evento pode ter vários Fornecedores
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="fornecedores")
    servico = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.empresa} ({self.servico})"

class Documento(models.Model):
    # Relação: Um Fornecedor pode ter vários Documentos
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name="documentos")
    descricao = models.CharField(max_length=255)
    url = models.URLField(max_length=1000) # URLField é perfeito para links

    def __str__(self):
        return self.descricao