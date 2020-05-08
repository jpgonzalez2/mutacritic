# Lista de comentarios sobre un videojuego


import webapp2
from webapp2_extras import jinja2


from model.videojuego import Videojuego
from model.comentario import Comentario

class ListaComentariosHandler(webapp2.RequestHandler):
    def get(self):
        videojuego, comentarios = Comentario.recupera_para(self.request)

        valores_plantilla = {
            "comentarios": comentarios,
            "videojuego": videojuego
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("lista_comentarios.html",
            **valores_plantilla))



app = webapp2.WSGIApplication([
    ('/comentarios/lista', ListaComentariosHandler)
], debug=True)
