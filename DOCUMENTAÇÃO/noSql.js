{
  "_id": "evt001",
  "id_cliente": "CLI-12345",
  "tipo": "Casamento",
  "nome": "Casamento de Ana e João",
  "data": "2025-11-15",
  "local": "Espaço Primavera",
  "convidados": 250,

  "usuario": {
    "id": 1,
    "nome": "Jamila Moraes",
    "email": "jamila@inovarh.com",
    "senha": "****",
    "tipo": "Administrador",
    "celular": "(19) 99999-9999",
    "pix": "jamila@pix.com"
  },

  "fornecedores": [
    {
      "id": 1,
      "servico": "Buffet",
      "empresa": "Delícias Gourmet",
      "status": "Confirmado",
      "documento": {
        "id": 11,
        "descricao": "Contrato de prestação de serviço",
        "url": "https://empresa.com/docs/contrato_buffet.pdf"
      }
    },
    {
      "id": 2,
      "servico": "Decoração",
      "empresa": "Flor e Arte",
      "status": "Pendente",
      "documento": {
        "id": 12,
        "descricao": "Proposta de decoração floral",
        "url": "https://empresa.com/docs/decoracao_proposta.pdf"
      }
    }
  ],

  "pendencias": [
    {
      "id": 1,
      "nome": "Pagamento do buffet",
      "descricao": "Falta pagamento da segunda parcela",
      "data": "2025-11-10"
    },
    {
      "id": 2,
      "nome": "Aprovação da decoração",
      "descricao": "Aguardando confirmação do casal",
      "data": "2025-10-31"
    }
  ],

  "atividades": [
    {
      "id": 1,
      "nome": "Reunião com fornecedores",
      "descricao": "Confirmar horários e entrega dos serviços",
      "horario": "2025-11-12T14:00:00Z",
      "status": "Agendada"
    },
    {
      "id": 2,
      "nome": "Visita ao local",
      "descricao": "Verificar disposição do espaço e layout final",
      "horario": "2025-11-14T10:00:00Z",
      "status": "Pendente"
    }
  ]
}