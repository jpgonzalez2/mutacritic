# coding: utf-8
# Elimina el comentario


import webapp2
import time
from webapp2_extras import jinja2

from model.comentario import Comentario


class EliminaComentarioHandler(webapp2.RequestHandler):
    def get(self):
        comentario = Comentario.recupera(self.request)
        comentario.key.delete()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/comentarios/elimina', EliminaComentarioHandler)
], debug=True)