from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!<h1>'

@app.route('/usuario', methods=['GET'])
def buscar_usuario():
    usuario = {
        "nome": "Mayara",
        "idade": 16,
        "telefone": "(19) 971682360"
    }
    return usuario


@app.route('/produto', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    print(f'Novo produto {dados}')

    return jsonify(
        {
            "messagem": "Produto salvo com sucesso",
            "produto_cadastrado": dados
         }
    ), 201


@app.route('/produto', methods=['PUT'])
def atualizar_produto():
    produto = {
        "id": 1,
        "nome": "Caneta Vermelha",
        "preco": 1.5,
        "descricao": "Caneta esferográfica",
        "marca": "Bic"
    }

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    if dados["id"] == produto["id"]:
        produto = dados
        print(f'roduto Atualizado {produto}')
        return jsonify({"messagem": "Produto atualizado com sucesso"}), 201
    else:
        return jsonify({"message": "Produto não encontrado"}), 400

    

if __name__ == '__main__':
    app.run(debug=True)