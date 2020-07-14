#isso aqui tudo vai fazer o banco e a conexão
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship #criando uma sessão
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True) #criando o banco e convertendo acentuação. /// é para criar a tabela em modo memória
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine)) #aqui ele conecta o banco à sessão

Base = declarative_base() #base declarativa default do sqlalchemy
Base.query = db_session.query_property() #pesquisa da query recebe as propridades da dessão da base. Trecho importante para trabalhar com as consultas

#a partir daqui será as tabelas, que neste caso, tbm são no modelo de classes
class Pessoas(Base):
    __tablename__='pessoas' #o nome da classe será o mesmo nome da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self): # essa função representa a classe. Podemos usá-la para imprimir a classe pessoa sem a necessidade de definir um campo da classe
        return '<Pessoa {}>'.format(self.nome)

class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas') #completando a relação com a tabela pessoas

def init_db():
    Base.metadata.create_all(bind=engine) #nesse comando ele cria o banco de dados

if __name__ == "__main__":
    init_db() #colocamos essa função aqui para melhorar a segunraça do banco