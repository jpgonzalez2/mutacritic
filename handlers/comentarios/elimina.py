# coding: utf-8
# Elimina el comentario


import webapp2
import time
from webapp2_extras import jinja2

from model.comentario import Comentario


class EliminaComentarioHandler(webapp2.RequestHandler):
    def get(self):
        clave_videojuego = self.request.GET["vdj"]
        comentario = Comentario.recupera(self.request)
        comentario.key.delete()
        time.sleep(1)

        suma = 0
        cont = 0
        videojuego, comentarios = Comentario.recupera_para(self.request)
        for comentario in comentarios:
            suma += int(comentario.puntuacion)
            cont += 1
        res = suma / cont
        videojuego.puntuacion = res
        videojuego.put()
        time.sleep(1)

        return self.redirect("/comentarios/lista?vdj=" + clave_videojuego)

app = webapp2.WSGIApplication([
    ('/comentarios/elimina', EliminaComentarioHandler)
], debug=True)