# 🎯 PI_3Semestre_2-2025 - Grupo Morgan Dev 
Sistema de Gerenciamento de Eventos - Cerimonial KD (Karine Diane)

## 🔎 Visão Geral  
O Cerimonial KD é um sistema desenvolvido pela equipe Morgan Devs (alunos da Fatec Araras “Antônio Brambilla”) para facilitar a gestão completa de eventos — desde o planejamento até a execução. O sistema centraliza dados de eventos, convidados, fornecedores, contratos e finanças em uma única plataforma, com foco em eficiência, controle e colaboração.

## 🎯 Objetivo / Problema que Resolve  
Muitas equipes de cerimonialistas e organizadores de eventos enfrentam dispersão de informações: planilhas separadas, falta de controle de contratos, dificuldade na gestão financeira e no acompanhamento de fornecedores e convidados.  
Este sistema busca resolver esses problemas oferecendo:

- Registro e controle de eventos (data, local, tipo, etc.)  
- Gestão de convidados com check-in por tablet  
- Controle financeiro e orçamentos  
- Checklists personalizáveis para cada evento  
- Gestão de fornecedores e contratos  
- Comunicação via WhatsApp (quando aplicável)  
- Controle de acesso com diferentes perfis (Admin / Equipe)  
- Funcionalidade offline e backups automáticos  

## ✅ Funcionalidades Principais  

| Funcionalidade | Descrição |
|---------------|-----------|
| Cadastro e controle de eventos | Criar, editar, listar e remover eventos |
| Gestão de convidados & check-in | Registrar convidados, realizar check-in via tablet |
| Gestão de fornecedores e contratos | Adicionar fornecedores, contratos e detalhes associados |
| Checklists customizáveis | Criar listas de tarefas para cada evento (pré-evento, pós-evento) |
| Controle de acesso | Perfis de usuário diferentes (ex: Admin, Cliente e Staff) |
| Suporte offline + backups automáticos | Permite uso mesmo sem conexão e salvamento automático de dados |

## 🛠️ Tecnologias Utilizadas  
- Back-end: Python + Django  
- Banco de dados: DbSqlite3 e MongoDB  
- Gestão de projeto: metodologia Scrum, uso de Trello para organização de tarefas  
- Ferramentas / Ambiente: VS Code, GitHub, virtualenv para ambiente Python e mongoengine 

## 🧑‍💻 Equipe “Morgan Devs”  
| Nome | Função |
|------|--------|
| Felipe Rafael Rocha | Back-end |
| Fernanda Maciel Palma | Front-end |
| Jamila Moraes Cardoso | Scrum Master / Coordenação |
| Patrick E. Beck Franzini | Banco de Dados |
| Rafaela C. Lemes | Full Stack |
| Valdir Garcia | Documentação |

> *Morgan Devs é uma equipe multidisciplinar formada por alunos da Fatec Araras. Nosso trabalho segue os princípios do Scrum: entregas incrementais, colaboração e melhoria contínua.*  

## 📁 Estrutura do Repositório  
/core → Lógica principal, regras de negócio<br>
/front-end/… → Código de interface / cliente (se aplicável)<br>
/config → Configurações do sistema (banco, ambiente, variáveis)<br>
/DOCUMENTAÇÃO → Especificações, diagramas, documentação adicional<br>
requirements.txt → Dependências Python<br>
manage.py → Script principal de execução<br>
README.md → Documentação deste repositório



## 🚀 Como Executar / Rodar Localmente  

1. Clone o repositório  
   ```bash
   git clone https://github.com/jmcardoso18/PI-2-2025-3-semestre.git  
   cd PI-2-2025-3-semestre  

   Crie e ative um ambiente virtual (Python)
   Copie o código python -m venv venv  
    
    # Linux / Mac
   source venv/bin/activate  
    # Windows
   venv\Scripts\activate  

2. Instale as dependências

    ```bash
    Use '..' e volte para pasta raiz

    Copie  código
    pip install -r requirements.txt  
    
    Ative o banco de dados nativo

    python manage.py makemigrations
    python manage.py migrate

    Crie o SuperUsuario
    python manage.py createsuperuser

    Execute o servidor
    python manage.py runserver

3. Configurando o Mongo

    ````
    Instale as dependências:

    pip install -r requirements.txt

    Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

    MONGO_URI=mongodb+srv://SEU_USUARIO:SUA_SENHA@SEU_CLUSTER.mongodb.net/SEU_BANCO
    * Crie um cluster no site do mongo atlas "https://www.mongodb.com/atlas"

    Certifique-se de que o .env está no .gitignore para não subir credenciais.

    O Django carregará essa variável automaticamente via python-dotenv.


4. Para rodar o front
    ```bash
    Abra o terminal do gitbash

    Entre na pasta
    cd front-end/karine-diena

    rode os comandos
    npm install
    npm run dev

    abra pelo servidor 
    http://localhost:5173/


## 📄 Licença & Uso
Este projeto foi desenvolvido exclusivamente para fins acadêmicos (Projeto Integrador da Fatec Araras). Todos os direitos reservados à equipe Morgan Devs — 2025.

## 🙏 Agradecimentos & Orientadores
Agradecemos à Fatec Araras e aos professores orientadores:

Renato Cividini Matthiesen — Gestão Ágil de Projeto de Software

Thiago Mendes — Banco de Dados Não Relacional

Orlando Saraiva do Nascimento Júnior — Desenvolvimento Web III
