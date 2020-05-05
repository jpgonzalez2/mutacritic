# Videojuego con una puntuación total y una descripción


from google.appengine.ext import ndb


class Videojuego(ndb.Model):
    nombre = ndb.StringProperty(indexed=True)
    puntuacion = ndb.IntegerProperty()
    descripcion = ndb.StringProperty(required=True)