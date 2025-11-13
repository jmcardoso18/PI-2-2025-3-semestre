# 🎯 PI_3Semestre_2-2025

> 🧩 Repositório destinado ao **Projeto Interdisciplinar do 3º Semestre** — Fatec Araras “Antônio Brambilla”  
> Desenvolvido pela equipe **Morgan Devs**

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-Framework-black?logo=flask" />
  <img src="https://img.shields.io/badge/MongoDB-NoSQL-green?logo=mongodb" />
  <img src="https://img.shields.io/badge/Scrum-Agile-lightgrey?logo=scrumalliance" />
  <img src="https://img.shields.io/badge/Fatec-Araras-red" />
  <img src="https://img.shields.io/badge/License-Academic-orange" />
</p>

---

## 💡 Sobre o Projeto

O **PI_3Semestre_2-2025** é um sistema de **gerenciamento de eventos** desenvolvido para facilitar o trabalho de **cerimonialistas e suas equipes**, centralizando todas as informações em uma única plataforma.

Com o sistema, é possível gerenciar **eventos, convidados, fornecedores, contratos e finanças**, otimizando o processo de planejamento e execução.  
A aplicação segue o modelo **ágil Scrum**, garantindo entregas incrementais e melhoria contínua.

---

## 🧠 Funcionalidades Principais

- 🗓️ **Cadastro e controle de eventos**
- 👥 **Gestão de convidados** com check-in via tablet
- 💰 **Orçamento e controle financeiro**
- 📋 **Checklists personalizáveis**
- 🤝 **Gestão de fornecedores e contratos**
- 💬 **Comunicação via WhatsApp**
- 🔐 **Controle de acesso (Admin / Equipe)**
- ☁️ **Funcionalidade offline e backups automáticos**

---

## 🖼️ Prévia do Sistema

> *Visual conceitual ilustrativo do sistema de gerenciamento de eventos.*

<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/flask/flask.png" width="400px" alt="Prévia ilustrativa do sistema" />
</p>

---

## 🧩 Tecnologias Utilizadas

| 🧱 Camada           | 🛠️ Tecnologias                        |
|--------------------|--------------------------------------|
| **Back-end**        | Python, Flask (ou FastAPI), Virtualenv|
| **Banco de Dados**  | MongoDB                              |
| **Metodologia**     | Scrum (Gestão Ágil de Projetos)     |
| **Ferramentas**     | Trello, GitHub, VS Code              |

---

## 🧱 Metodologia de Desenvolvimento

O projeto é conduzido com base na metodologia **Scrum**, utilizando **sprints curtas** e **entregas incrementais**.  
As tarefas e o progresso são gerenciados via **Trello**, com reuniões semanais de acompanhamento.

---

## 👨‍💻 Equipe Morgan Devs

| 👤 Nome                   | 💼 Função         |
|----------------------------|-----------------|
| Felipe Rafael Rocha        | Back-end         |
| Fernanda Maciel Palma      | Front-end        |
| Jamila Moraes Cardoso      | Scrum Master     |
| Patrick E. Beck Franzini   | Banco de Dados   |
| Rafaela C. Lemes           | Full Stack       |
| Valdir Garcia              | Documentação     |

---

## 🏢 Empresa Fictícia

**Morgan Devs** é uma equipe multidisciplinar formada por alunos do curso de **Desenvolvimento de Software Multiplataforma (DSM)** da **Fatec Araras “Antônio Brambilla”**.  
A empresa segue os princípios do **Scrum**, com foco em **entregas incrementais**, **colaboração** e **melhoria contínua**.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos no âmbito do **Projeto Integrador (PI)** da Fatec Araras.  
© 2025 **Morgan Devs** — Todos os direitos reservados.

---

## 👨‍🏫 Professores Orientadores

- **Renato Cividini Matthiesen** — Gestão Ágil de Projeto de Software  
- **Thiago Mendes** — Banco de Dados Não Relacional  
- **Orlando Saraiva do Nascimento Junior** — Desenvolvimento Web III  

---

## ⭐ Agradecimentos

Agradecemos à **Fatec Araras** e aos **professores orientadores** pelo suporte técnico e pedagógico durante o desenvolvimento deste projeto.  

> 💬 “Na FAAL você pratica, você aprende!”  
> **Morgan Devs — Inovando com propósito.**

---

## 🖼️ Capturas de Tela (opcional)

Adicione aqui **prints ou mockups** do sistema:

![Tela Inicial](./FRONT-END/assets/img/tela-inicial.png)  
![Dashboard](./FRONT-END/assets/img/dashboard.png)

---

## ⚙️ Como Utilizar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/jmcardoso18/PI_3Semestre_2-2025.git
cd PI_3Semestre_2-2025/BACK-END.
2️⃣ Crie o ambiente virtual
python -m venv venv

3️⃣ Ative o ambiente virtual

Linux/Mac:

source venv/bin/activate


Windows:

venv\Scripts\activate

4️⃣ Instale as dependências do projeto
pip install -r requirements.txt

5️⃣ Configure as variáveis de ambiente (se necessário)

Crie um arquivo .env na raiz do projeto e adicione:

MONGO_URI=sua_string_de_conexao
SECRET_KEY=sua_chave_secreta

6️⃣ Execute o servidor
python app.py


O projeto estará disponível em:
👉 http://localhost:5000

7️⃣ (Opcional) Desative o ambiente virtual
deactivate

