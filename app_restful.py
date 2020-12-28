from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

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

class Desenvolvedor(Resource): #aqui a classe esá recebendo a função resouce que está dentro do import
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem:':'Desenvolvedor de ID {} não existe'.format(id)}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador.'
            response = {'status':'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id) #método pop exclui o último elemento de uma lista
        return {'status':'sucesso', 'mensagem': 'Registro excluído'}

class ListaDesenvolvedores(Resource): #agora a consulta ao banco será feita por classe
    def get(self): #aqui ele busca todos os dados do banco
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao #adicionando ID à mensagem para saber qual ID foi registrado
        desenvolvedores.append(dados)
        return {'status':'sucesso','mensagem':'Registro inserido!'}, desenvolvedores[posicao]
    
#rotas
api.add_resource(Desenvolvedor, '/dev/<int:id>/') #a rota agora fica nesse formato. Ela recebe a classe e o URI
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == "__main__":
    app.run(debug=True)
