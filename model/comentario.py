# coding: utf-8
# Comentario de los usuarios sobre el videojuego, con valoración


from google.appengine.ext import ndb

from videojuego import Videojuego


class Comentario(ndb.Model):
    usuario = ndb.StringProperty(required=True)
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    puntuacion = ndb.IntegerProperty(required=True)
    texto = ndb.StringProperty(required=True)
    clave_videojuego = ndb.KeyProperty(kind=Videojuego)
    editado = ndb.BooleanProperty(required=True)

    @staticmethod
    def recupera_para(req):
        try:
            id_vdj = req.GET["vdj"]
        except KeyError:
            id_vdj = ""

        if id_vdj:
            clave_videojuego = ndb.Key(urlsafe=id_vdj)
            comentarios = Comentario.query(Comentario.clave_videojuego == clave_videojuego)
            return (clave_videojuego.get(), comentarios)
        else:
            print("ERROR: videojuego no encontrado")

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()