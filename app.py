from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>') #aqui ele coloca a tipagem do dado e qual dado será fornecido no banco, no caso, a pesquisa retornará por ID
def pessoa(id):
    return jsonify({'id':id, 'nome':'Rafael', 'profissao':'Desenvolvedor'})

# @app.route('/soma/<int:valor1>/<int:valor2>') #colocando operações matemáticas para o método get capturar o valor na uri retornar a soma
# def soma(valor1, valor2):
#     return jsonify({'soma':valor1 + valor2})

@app.route('/soma/', methods=['POST', 'GET'])
def soma():
    # dados = json.loads(request.data) #tranforma os dados recebidos para formato json
    # print(dados)
    # return 'soma'

    # dados = json.loads(request.data)
    # total = sum(dados['valores']) #fazendo a soma dos valores e retornando o total
    # return jsonify({'soma': total})
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores']) #fazendo a soma dos valores e retornando o total conforme tipo de método
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})

if __name__ == "__main__":
    app.run(debug=True)