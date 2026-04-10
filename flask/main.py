from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Banco de dados - início
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///papelaria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, default=0)
    preco = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "quantidade": self.quantidade, "preco": self.preco}

with app.app_context():
    db.create_all()
# Banco de dados - fim


@app.route('/produtos', methods=['GET']) # View
@app.route('/produtos/<int:id>', methods=['GET']) # View
def gerenciar_produtos(id=None): # View
    if id: # View
        produto = Produto.query.get(id) # View
        if produto: # View
            return jsonify(produto.to_dict()), 200 # view
        return jsonify({"erro": "Produto não encontrado"}), 404 # view

    produtos = Produto.query.all() # View
    return jsonify([p.to_dict() for p in produtos]), 200 # View

@app.route('/insert', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    
    novo_produto = Produto(
        nome=dados.get('nome'),
        quantidade=dados.get('quantidade'),
        preco=dados.get('preco')
    )
    
    db.session.add(novo_produto)
    db.session.commit()
    
    return jsonify({"mensagem": "Produto criado!", "id": novo_produto.id}), 201

@app.route('/update/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    dados = request.get_json()
    
    produto.nome = dados.get('nome', produto.nome)
    produto.quantidade = dados.get('quantidade', produto.quantidade)
    produto.preco = dados.get('preco', produto.preco)

    db.session.commit()
    return jsonify({"mensagem": "Produto atualizado!"}), 200

@app.route('/delete/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    db.session.delete(produto)
    db.session.commit()
    return jsonify({"mensagem": f"Produto '{produto.nome}' removido!"}), 200

if __name__ == '__main__':
    app.run(debug=True)