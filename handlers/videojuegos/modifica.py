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
            "videojuego": videojuego,
            "clave_videojuego": self.request.GET["id"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_videojuego.html",
            **valores_plantilla))

    def post(self):
        titulo = self.request.get("edTitulo", "")
        descripcion = self.request.get("edDescripcion", "")

        videojuego = Videojuego.recupera(self.request)

        if (not(titulo) or not(descripcion)):
            return self.redirect("videojuegos/modifica")
        else:
            videojuego.titulo = titulo
            videojuego.descripcion = descripcion

            videojuego.put()
            time.sleep(1)

        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/videojuegos/modifica', ModificaVideojuegoHandler)
], debug=True)