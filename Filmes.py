from db import db
from flask_sqlalchemy import SQLAlchemy


class Filmes(db.Model):
    __tablename__ = 'Filmes'
    
    id = db.Column(db.Integer, primary_key=True)#Column(Integer,primary_key=True)
    nome = Column(String(120), multable=False)
    avaliacao = Column(float, multable=True)
    test = db.Column(db.Integer)



    def __init__(self, nome, avaliacao):
        self.nome = nome
        self.avaliacao = avaliacao

    def jason(self, ):
        return{
            'Nome':self.nome,
            'Avaliacao': self.avaliacao
        }

    @classmethod
    def find_nome(cls, nome):
        return cls.query.filter_by(title=nome).first()
    
    @classmethod
    def find_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def salvar(self):
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    def alterar(self):
        pass

