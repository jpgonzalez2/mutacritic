# coding: utf-8
# Comentario de los usuarios sobre el videojuego, con valoración


from google.appengine.ext import ndb


class Comentario(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    puntuacion = ndb.IntegerProperty(required=True)
    texto = ndb.StringProperty(required=True)