# coding: utf-8
# Videojuego con una puntuación total y una descripción


from google.appengine.ext import ndb


class Videojuego(ndb.Model):
    titulo = ndb.StringProperty(indexed=True)
    puntuacion = ndb.IntegerProperty(required=True)
    descripcion = ndb.StringProperty(required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()