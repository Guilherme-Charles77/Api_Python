from flask import Flask, jsonify, request
from db import db
from dotenv import load_dotenv
from models import Book
import os


#Configuração de porta
load_dotenv()
port = int(os.getenv("API_RUN_PORT", "5000"))

#Configuração de App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db.init_app(app)


"""
Rotas
"""

#Criar livro
@app.route('/livros', methods = ["POST"])
def create():
    try:
        json = request.get_json()
        if not json or 'title' not in json or 'author' not in json:
            return jsonify({"error": "Title and author are required"}), 400

        try:
            publish = int(json.get('publish', 0))
        except ValueError:
            return jsonify({"error": "Publish year must be a number"}), 400

        new_book= Book(    
        title = json.get('title'),
        author = json.get('author'),
        publish = int(json.get('publish'))
        )

        #Salvar no banco de dados
        db.session.add(new_book)
        db.session.commit()

        return jsonify({
            "message": "Book created successfully",
            "book": {
                "id": new_book.id,
                "title": new_book.title,
                "author": new_book.author,
                "publish": new_book.publish
            }
        }), 201
    
    except Exception as e:
        # Em caso de erro, faz reversão e retorna mensagem de erro
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

#Listar livros
@app.route('/livros', methods = ["GET"])
def list():
    try:
        # Obtém todos os livros do banco de dados
        books = db.session.query(Book).all()
        
        # Serializa os livros para JSON
        books_list = [{
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "publish": book.publish
        } for book in books]
        
        return jsonify(books_list), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Buscar livro pelo ID
@app.route('/livros/<int:id>', methods = ["GET"])
def search(id):
    try:
     
        book = db.session.query(Book).filter_by(id=id).first()
        
        if not book:
            return jsonify({"error": "Book not found"}), 404
            
        # Retorna o livro buscado em Json
        return jsonify({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "publish": book.publish
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#Deleta Livro pelo ID
@app.route('/livros/<int:id>', methods = ["DELETE"])
def delete(id):
    try:
        book = db.session.query(Book).filter_by(id=id).first()
        
        if not book:
            return jsonify({"error": "Book not found"}), 404

        db.session.delete(book)
        db.session.commit()    
        # Retorna os detalhes do livro deletado
        return jsonify({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "publish": book.publish
        }, "Delete Susseful")
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    print(f"Api is runnig on {port}")
    app.run(debug=False, port = port)
