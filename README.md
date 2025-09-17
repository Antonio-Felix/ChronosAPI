<h1 align="center">⏳ CHRONOS API</h1>
<p align="center">Uma API para acompanhamento de treinos, dietas e usuários, desenvolvida com Django REST Framework.</p>

<p align="center" gap="8px">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain-wordmark.svg" height="256" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/djangorest/djangorest-original.svg" height="256" />
</p>

````markdown

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Django 5.x
- Django REST Framework
- Banco de dados: PostgreSQL
- Autenticação JWT
- Swagger / DRF Spectacular

---

## ✨ Funcionalidades

- Gerenciamento de alunos, personais e nutricionistas
- Listar, criar, atualizar e deletar dados
- Autenticação via JWT
- Paginação
- Documentação de API com Swagger / DRF Spectacular

---

## ⚙️ Pré-requisitos

- Python 3.x
- Pip
- Virtualenv (venv)
- Banco de dados configurado (PostgreSQL)

````

## 🛠️ Instalação

1. Clone o repositório:
   
```bash
git clone https://github.com/Antonio-Felix/ChronosAPI.git
cd ChronosAPI
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure variáveis de ambiente (`.env`):

```env
DJANGO_SECRET_KEY=suachavesecreta
DEBUG=True

DB_NAME=prova
DB_USER=postgres
DB_PASSWORD=123321
DB_HOST=localhost
DB_PORT=5432
```

5. Execute as migrations:

```bash
python manage.py migrate
```

6. Crie um superusuário:

```bash
python manage.py createsuperuser
```

7. Inicie o servidor:

```bash
python manage.py runserver
```

---

## 📌 Estrutura de Endpoints

### 🔐 Autenticação

| Método | Endpoint            | Descrição           |
| ------ | ------------------- | ------------------- |
| POST   | /api/token/         | Obter token JWT     |
| POST   | /api/token/refresh/ | Atualizar token JWT |

### 🥗 Diets

| Método | Endpoint                          | Descrição                        |
| ------ | --------------------------------- | -------------------------------- |
| GET    | /api/v1/diets/                    | Listar todas as diets            |
| POST   | /api/v1/diets/                    | Criar uma nova diet              |
| GET    | /api/v1/diets/{id}/               | Detalhes de uma diet             |
| PUT    | /api/v1/diets/{id}/               | Atualizar completamente uma diet |
| PATCH  | /api/v1/diets/{id}/               | Atualizar parcialmente uma diet  |
| DELETE | /api/v1/diets/{id}/               | Remover uma diet                 |
| POST   | /api/v1/diets/{id}/add\_calories/ | Adicionar calorias               |
| POST   | /api/v1/diets/{id}/add\_water/    | Adicionar água                   |

### 🏋️ Exercises

| Método | Endpoint                | Descrição               |
| ------ | ----------------------- | ----------------------- |
| GET    | /api/v1/exercises/      | Listar exercícios       |
| POST   | /api/v1/exercises/      | Criar exercício         |
| GET    | /api/v1/exercises/{id}/ | Detalhes do exercício   |
| PUT    | /api/v1/exercises/{id}/ | Atualizar completamente |
| PATCH  | /api/v1/exercises/{id}/ | Atualizar parcialmente  |
| DELETE | /api/v1/exercises/{id}/ | Remover exercício       |

### 👤 Users

| Método | Endpoint            | Descrição               |
| ------ | ------------------- | ----------------------- |
| GET    | /api/v1/users/      | Listar usuários         |
| POST   | /api/v1/users/      | Criar usuário           |
| GET    | /api/v1/users/{id}/ | Detalhes do usuário     |
| PUT    | /api/v1/users/{id}/ | Atualizar completamente |
| PATCH  | /api/v1/users/{id}/ | Atualizar parcialmente  |
| DELETE | /api/v1/users/{id}/ | Remover usuário         |

### 🏃 Workouts

| Método | Endpoint               | Descrição               |
| ------ | ---------------------- | ----------------------- |
| GET    | /api/v1/workouts/      | Listar treinos          |
| POST   | /api/v1/workouts/      | Criar treino            |
| GET    | /api/v1/workouts/{id}/ | Detalhes do treino      |
| PUT    | /api/v1/workouts/{id}/ | Atualizar completamente |
| PATCH  | /api/v1/workouts/{id}/ | Atualizar parcialmente  |
| DELETE | /api/v1/workouts/{id}/ | Remover treino          |

---

## 🔑 Autenticação

* Endpoints protegidos requerem token JWT.
* Para obter um token:

```bash
POST /api/token/
{
  "username": "usuario",
  "password": "senha"
}
```

* Use o token no header das requisições:

```
Authorization: Bearer <SEU_TOKEN_AQUI>
```

---

## 📄 Licença

© GO+ Group. Todos os direitos reservados.
