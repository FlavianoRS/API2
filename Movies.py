from flask import request
from flask_restplus import Resource, fields
from Models.Filmes import Filmes
from schemas.Movies import MoviesSchemas
from Server.instance import server

movie = server.movie
movieSCh = MoviesSchemas()
movieLSCH = MoviesSchemas(many=True)

class Filme(Resource):

    def get(self, id):
        daMovie = Filmes.find_id(id)

        if daMovie:
            return movieSCh.dump(daMovie), 200
        
        return{'Message':'Item não encontrado'}
