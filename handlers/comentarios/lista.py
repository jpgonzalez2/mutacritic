# Lista de comentarios sobre un videojuego


import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users


from model.videojuego import Videojuego
from model.comentario import Comentario

class ListaComentariosHandler(webapp2.RequestHandler):
    def get(self):
        videojuego, comentarios = Comentario.recupera_para(self.request)
        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
        else:
            url_usr = users.create_login_url("/")

        if users.is_current_user_admin():
            admin = True
        else:
            admin = False

        valores_plantilla = {
            "comentarios": comentarios,
            "videojuego": videojuego,
            "usr": usr,
            "url_usr": url_usr,
            "admin": admin
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("lista_comentarios.html",
            **valores_plantilla))



app = webapp2.WSGIApplication([
    ('/comentarios/lista', ListaComentariosHandler)
], debug=True)
