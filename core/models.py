from django.db import models

# -------------------------------------------------------------------
# Modelo SERVICO (Para o Site / Landing Page)
# -------------------------------------------------------------------
class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    # Null=True permite deixar sem preço "Sob Consulta"
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.titulo

# -------------------------------------------------------------------
# Modelo USUARIO (Sistema Interno)
# -------------------------------------------------------------------
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255) 
    tipo = models.CharField(max_length=255)
    celular = models.CharField(max_length=15, blank=True, null=True)
    pix = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nome

# -------------------------------------------------------------------
# Modelo EVENTO
# -------------------------------------------------------------------
class Evento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="eventos")
    id_cliente = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)
    estimativa_convidados = models.CharField(max_length=255) 

    def __str__(self):
        return f"{self.nome} ({self.data.strftime('%d/%m/%Y')})"

# -------------------------------------------------------------------
# Modelos "Filhos" do Evento
# -------------------------------------------------------------------

class Ocorrencia(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="ocorrencias")
    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tipo} - {self.evento.nome}"

class Pendencia(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="pendencias")
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data = models.CharField(max_length=255) 
    status = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Pendências"

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="atividades")
    nome = models.CharField(max_length=255) 
    # Mudamos para TimeField para facilitar ordenação
    horario = models.TimeField()            
    # Checkbox de conclusão
    feito = models.BooleanField(default=False) 

    class Meta:
        ordering = ['horario'] 

    def __str__(self):
        return f"{self.nome} - {self.evento.nome}"

class Convidado(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Confirmado', 'Confirmado'),
        ('Recusado', 'Recusado'),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="convidados")
    nome = models.CharField(max_length=255)
    acompanhantes = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return self.nome

# -------------------------------------------------------------------
# Modelos FORNECEDOR e DOCUMENTO
# -------------------------------------------------------------------

class Fornecedor(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="fornecedores")
    servico = models.CharField(max_length=255) # Ex: "Buffet", "Fotografia"
    empresa = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.empresa} ({self.servico})"

class Documento(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name="documentos")
    descricao = models.CharField(max_length=255)
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.descricao
    
class Tarefa(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="tarefas")
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_limite = models.DateField()
    feito = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo