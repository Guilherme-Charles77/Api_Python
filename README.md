# 📚 Book API - Flask RESTful Application

Este é um projeto simples de uma API RESTful feita com Flask para gerenciar um cadastro de livros. Ela permite criar, listar, buscar e excluir livros armazenados em um banco de dados SQLite.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite

---

## 📁 Estrutura do Projeto

```
.
├── main.py                # Arquivo principal da aplicação Flask
├── db.py                  # Instância do SQLAlchemy
├── models.py              # Modelo Book (ORM)
├── instance/
│   └── books.db           # Banco de dados SQLite
├── tests/
│   └── views.http         # Requisições de teste com REST Client (VS Code)
└── requirements.txt       # Dependências do projeto
```

---

## ▶️ Como Executar

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/book-api.git
cd book-api
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**

```bash
python main.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`

---

## 📌 Endpoints da API

### ➕ Criar um novo livro
**POST** `/livros`

```json
{
  "title": "Dom Casmurro",
  "author": "Machado de Assis",
  "publish": 1899
}
```

### 📚 Listar todos os livros
**GET** `/livros`

### 🔍 Buscar um livro por ID
**GET** `/livros/<id>`

### ❌ Deletar um livro por ID
**DELETE** `/livros/<id>`

---

## ✅ Testes com REST Client

Você pode testar os endpoints com a extensão [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) no VS Code. As requisições estão no arquivo `tests/views.http`.

---

## 📦 Dependências

As bibliotecas usadas estão listadas em `requirements.txt`. Para instalar todas, use:

```bash
pip install -r requirements.txt
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Fique à vontade para usar, modificar e contribuir.

---

Desenvolvido com 💻 por [Seu Nome]
