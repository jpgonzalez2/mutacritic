# coding: utf-8
# Elimina el videojuego


import webapp2
import time
from webapp2_extras import jinja2

from model.videojuego import Videojuego


class EliminaVideojuegoHandler(webapp2.RequestHandler):
    def get(self):
        videojuego = Videojuego.recupera(self.request)
        videojuego.key.delete()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/videojuegos/elimina', EliminaVideojuegoHandler)
], debug=True)