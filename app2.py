from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Rafael',
        'habilidades': ['Python', 'Flask'],
    },
    {   
        'id':'1',
        'nome':'Galealini',
        'habilidades': ['Python', 'Django']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])

def desenvolvedor(id):
    # if request.method == 'GET': #aqui ele vai configurar a busca do dicionário pelo ID
    #     desenvolvedor = desenvolvedores[id]
    #     print(desenvolvedor)
    #     return jsonify(desenvolvedor)
    if request.method == 'GET': #desta forma ele vai deixar mais explícito quando um resgistro está modificado
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem:':'Desenvolvedor de ID {} não existe'.format(id)}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador.'
            response = {'status':'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT': #aqui ele vai permitir, a partir da busca, editar o ID
        dados = json.loads(request.data) #aqui ele está ajustando as requisições para ficar em formato json e permitindo armazenar o input do usuário em uma variável "dados"
        desenvolvedores[id] = dados #aqui ele está atribuindo o valor de dados para a lista desenvolvedores na posição id
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id) #método pop exclui o último elemento de uma lista
        return jsonify({'status':'sucesso', 'mensagem': 'Registro excluído'})

@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao #adicionando ID à mensagem para saber qual ID foi registrado
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','mensagem':'Registro inserido!'}, desenvolvedores[posicao])
    elif request.method == 'GET': #consulta de todos os desenvolvedores
        return jsonify(desenvolvedores)

if __name__ == "__main__":
    app.run(debug=True)