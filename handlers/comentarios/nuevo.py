# coding: utf-8
# Nuevo comentario


import webapp2
import time
from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.comentario import Comentario


class NuevoComentarioHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
            "clave_videojuego": self.request.GET["vdj"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_comentario.html",
            **valores_plantilla))

    def post(self):
        usuario = self.request.get("edUsuario", "")
        str_puntuacion = self.request.get("edPuntuacion", "")
        texto = self.request.get("edTexto", "")
        clave_videojuego = self.request.GET["vdj"]

        try:
            puntuacion = int(str_puntuacion)
        except ValueError:
            puntuacion = -1

        if (not(puntuacion) or not(texto)):
            return self.redirect("comentario/nuevo")
        else:
            comentario = Comentario(usuario=usuario,
                                    puntuacion=puntuacion,
                                    texto=texto,
                                    clave_videojuego=ndb.Key(urlsafe=clave_videojuego))
            comentario.put()
            time.sleep(1)
            return self.redirect("/comentarios/lista?vdj=" + clave_videojuego)


app = webapp2.WSGIApplication([
    ('/comentarios/nuevo', NuevoComentarioHandler)
], debug=True)