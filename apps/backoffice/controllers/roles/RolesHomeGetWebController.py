# apps/oh_sansi/controllers/roles/RolesHomeGetWebController.py

from flask import Blueprint, render_template
from flask_admin import BaseView, expose
from apps.backoffice.middlewares.SessionAuth import login_required, roles_required


roles_bp = Blueprint("backoffice_roles", __name__)



class RolesHomeGetWebController(BaseView):
    edit_modal = True
    create_modal = True
    can_export = True
    can_view_details = True
    details_modal = True

    @expose('/')
    @login_required
    @roles_required("admin")
    def index(self):
        """
        Muestra la vista Home (listado) para la sección de Roles,
        accesible sólo por usuarios logueados con rol 'admin'. y los permisos necesarios
        """
        # Aquí haces tu lógica. Ejemplo:
        #   - Cargar datos que quieras mostrar (roles, usuarios, etc.)
        #   - Llamar a tu capa de servicio en src/application/searcher
        #   - Retornar una plantilla Jinja con render_template
        return render_template("admin/custom_index.html")

