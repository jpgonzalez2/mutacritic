# coding: utf-8
# Modifica el videojuego


import webapp2
import time
from webapp2_extras import jinja2

from model.videojuego import Videojuego


class ModificaVideojuegoHandler(webapp2.RequestHandler):
    def get(self):
        videojuego = Videojuego.recupera(self.request)
        valores_plantilla = {
            "videojuego": videojuego
        }
        videojuego.key.delete()
        time.sleep(1)

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_videojuego.html",
            **valores_plantilla))

    def post(self):
        titulo = self.request.get("edTitulo", "")
        str_puntuacion = self.request.get("edPuntuacion", "0")
        descripcion = self.request.get("edDescripcion", "")

        try:
            puntuacion = int(str_puntuacion)
        except ValueError:
            puntuacion = -1

        if (not(titulo) or not(descripcion)):
            return self.redirect("videojuegos/modifica")
        else:
            videojuego = Videojuego(titulo=titulo, puntuacion=puntuacion,
                                    descripcion=descripcion)
            videojuego.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/videojuegos/modifica', ModificaVideojuegoHandler)
], debug=True)