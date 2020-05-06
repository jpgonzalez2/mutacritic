# coding: utf-8
# Videojuego con una puntuación total y una descripción


from google.appengine.ext import ndb


class Videojuego(ndb.Model):
    titulo = ndb.StringProperty(indexed=True)
    puntuacion = ndb.IntegerProperty()
    descripcion = ndb.StringProperty(required=True)