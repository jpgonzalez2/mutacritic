# coding: utf-8
# Modifica el videojuego


import webapp2
import time
from webapp2_extras import jinja2

from model.comentario import Comentario
from webapp2_extras.users import users


class ModificaComentarioHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        comentario = Comentario.recupera(self.request)
        valores_plantilla = {
            "clave_videojuego": self.request.GET["vdj"],
            "usr": usr,
            "comentario": comentario,
            "clave_comentario": self.request.GET["id"],
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_comentario.html",
            **valores_plantilla))

    def post(self):
        str_puntuacion = self.request.get("edPuntuacion", "")
        texto = self.request.get("edTexto", "")
        clave_videojuego = self.request.GET["vdj"]
        editado = True

        comentario = Comentario.recupera(self.request)

        try:
            puntuacion = int(str_puntuacion)
        except ValueError:
            puntuacion = -1

        if (not (puntuacion) or not (texto)):
            return self.redirect("/comentarios/modifica?vdj=" + clave_videojuego)
        else:
            comentario.puntuacion = puntuacion
            comentario.texto = texto
            comentario.editado = editado

            comentario.put()
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
    ('/comentarios/modifica', ModificaComentarioHandler)
], debug=True)