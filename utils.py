#arquivo para ajudar a visualizar o banco 
from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=29)
    print(pessoa)
    db_session.add(pessoa) #adicionando pessoa à session
    db_session.commit() #e comitando logo após 

def consulta():
    # pessoa = Pessoas.query.filter_by(nome='Rafael')
    pessoa = Pessoas.query.all()
    print(pessoa)

if __name__ == "__main__":
    #insere_pessoas()
    consulta()