# coding: utf-8
# Nuevo videojuego


import webapp2
import time
from webapp2_extras import jinja2

from model.videojuego import Videojuego


class NuevoVideojuegoHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_videojuego.html",
            **valores_plantilla))

    def post(self):
        titulo = self.request.get("edTitulo", "")
        puntuacion = 0
        descripcion = self.request.get("edDescripcion", "")

        if (not(titulo) or not(descripcion)):
            return self.redirect("videojuegos/nuevo")
        else:
            videojuego = Videojuego(titulo=titulo, puntuacion=puntuacion,
                                    descripcion=descripcion)
            videojuego.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/videojuegos/nuevo', NuevoVideojuegoHandler)
], debug=True)