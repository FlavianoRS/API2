from flask import jsonify
from marshmallow import ValidationError
from db import db
from Mash import mars
from Server.instance import server
from Controllers.Movies import Filme

api = server.api
app = server.app

@app.before_first_request
def criar_tabelas():
    db.create_all()

api.add_resource(Filme, '/movies/<int:id>')

if __name__ =='__main__':
    db.init_app(app)
    mars.init_app(app)
    server.run()