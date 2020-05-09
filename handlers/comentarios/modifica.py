# coding: utf-8
# Modifica el videojuego


import webapp2
import time
from webapp2_extras import jinja2

from model.videojuego import Videojuego
from model.comentario import Comentario


class ModificaComentarioHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
            "clave_videojuego": self.request.GET["vdj"],
            "comentario": Comentario.recupera(self.request)
        }
        #comentario.key.delete()
        #time.sleep(1)

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_comentario.html",
            **valores_plantilla))

    def post(self):
        usuario = self.request.get("edUsuario", "")
        str_puntuacion = self.request.get("edPuntuacion", "")
        texto = self.request.get("edtexto", "")
        clave_videojuego = self.request.GET["vdj"]

        try:
            puntuacion = int(str_puntuacion)
        except ValueError:
            puntuacion = -1

        if (not(texto) or not(puntuacion)):
            return self.redirect("/comentarios/modifica")
        else:
            comentario = Comentario(usuario=usuario, puntuacion=puntuacion,
                                    texto=texto, clave_videojuego=clave_videojuego)
            comentario.put()
            time.sleep(1)
            return self.redirect("/comentarios/lista?vdj=" + clave_videojuego)


app = webapp2.WSGIApplication([
    ('/comentarios/modifica', ModificaComentarioHandler)
], debug=True)