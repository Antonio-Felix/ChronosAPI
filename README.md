# Projeto_web_II

1. Sobre:
````
# Chronos

ChronosAPI, é uma API desenvolvida com a funcionalidade de acompanhamento de treinos e dietas.

## Tecnologias Utilizadas

- Python 3.x
- Django 5.x
- Django REST Framework
- Banco de dados: PostgreSQL
- JWT

## Funcionalidades

- Listar, criar, atualizar e deletar alunos, personais e nutricionistas
- Autenticação via JWT
- Paginação
- Documentação de API com Swagger / DRF Spectacular

## Pré-requisitos

- Python 3.x instalado
- Pip
- Virtualenv (venv)
- Banco de dados configurado

## Instalação

1. Clone o repositório:
```bash
git clone https://https://github.com/Antonio-Felix/ChronosAPI.git
cd ChronosAPI
````

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

4. Configure variáveis de ambiente (ex.: `.env`):

```env
DB_NAME=Nome_do_banco
DB_USER=Nome_do_user
DB_PASSWORD=Senha_do_user
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

7. Rode o servidor:

```bash
python manage.py runserver
```

## Estrutura de Endpoints

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST   | /api/token/ | Obter token JWT |
| POST   | /api/token/refresh/ | Atualizar token JWT |

### Diets
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | /api/v1/diets/ | Listar todas as diets |
| POST   | /api/v1/diets/ | Criar uma nova diet |
| GET    | /api/v1/diets/{id}/ | Detalhes de uma diet |
| PUT    | /api/v1/diets/{id}/ | Atualizar uma diet completamente |
| PATCH  | /api/v1/diets/{id}/ | Atualizar parcialmente uma diet |
| DELETE | /api/v1/diets/{id}/ | Remover uma diet |
| POST   | /api/v1/diets/{id}/add_calories/ | Adicionar calorias à diet |
| POST   | /api/v1/diets/{id}/add_water/ | Adicionar água à diet |

### Exercises
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | /api/v1/exercises/ | Listar todos os exercícios |
| POST   | /api/v1/exercises/ | Criar um novo exercício |
| GET    | /api/v1/exercises/{id}/ | Detalhes de um exercício |
| PUT    | /api/v1/exercises/{id}/ | Atualizar completamente um exercício |
| PATCH  | /api/v1/exercises/{id}/ | Atualizar parcialmente um exercício |
| DELETE | /api/v1/exercises/{id}/ | Remover um exercício |

### Users
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | /api/v1/users/ | Listar todos os usuários |
| POST   | /api/v1/users/ | Criar um novo usuário |
| GET    | /api/v1/users/{id}/ | Detalhes de um usuário |
| PUT    | /api/v1/users/{id}/ | Atualizar completamente um usuário |
| PATCH  | /api/v1/users/{id}/ | Atualizar parcialmente um usuário |
| DELETE | /api/v1/users/{id}/ | Remover um usuário |

### Workouts
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | /api/v1/workouts/ | Listar todos os treinos |
| POST   | /api/v1/workouts/ | Criar um novo treino |
| GET    | /api/v1/workouts/{id}/ | Detalhes de um treino |
| PUT    | /api/v1/workouts/{id}/ | Atualizar completamente um treino |
| PATCH  | /api/v1/workouts/{id}/ | Atualizar parcialmente um treino |
| DELETE | /api/v1/workouts/{id}/ | Remover um treino |

## Autenticação

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

## Licença

© GO+. Todos os direitos reservados.

```

Quer que eu faça essa versão prática também?
```
