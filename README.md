# 🎓 Sistema de Gestão de Carteiras Estudantis

> Projeto desenvolvido para a disciplina de Desenvolvimento Web 2. Um sistema completo para cadastro, gestão e emissão de carteiras de estudante em Django.

---

## 🚀 Funcionalidades
- **🔐 Fluxo de Acesso Seguro**: Primeira página direciona para o cadastro de novos administradores.
- **👤 Gestão de Usuários**: Cadastro simplificado de coordenadores para acesso ao painel.
- **🪪 Gestão de Carteiras**: Controle total (Criar, Listar, Visualizar) dos dados estudantis.
- **📸 Upload de Mídia**: Suporte para fotos dos alunos diretamente no sistema.
- **📄 Emissão de PDF**: Função de impressão otimizada para gerar a carteira física.
- **🌑 Dark Mode**: Interface confortável aos olhos com tons charcoal e azul glacial.

---

## 📊 Estrutura de Dados (DER)

O banco de dados foi projetado para separar as credenciais de acesso dos dados sensíveis dos alunos. Abaixo, a descrição técnica do Diagrama de Entidade-Relacionamento:

| Entidade: **User** (Django Auth) | Entidade: **CarteiraEstudante** |
| :--- | :--- |
| `id` (PK) - Integer | `id` (PK) - Integer |
| `username` - Varchar(150) | `nome_completo` - Varchar(200) |
| `password` - Hash | `matricula` - Varchar(20) |
| | `curso` - Varchar(100) |
| | `foto` - ImageField |
| | `data_nascimento` - Date |
| | `validade` - Date |

---

## 🛠️ Tecnologias Utilizadas
* **Backend:** [Python 3](https://www.python.org/) & [Django 5](https://www.djangoproject.com/)
* **Frontend:** HTML5, CSS3, JavaScript
* **Framework CSS:** [Bootstrap 5](https://getbootstrap.com/)
* **Banco de Dados:** SQLite (Desenvolvimento)

---
