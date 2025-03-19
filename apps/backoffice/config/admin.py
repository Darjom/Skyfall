# apps/backoffice/config/admin.py

import flask_admin
from flask_admin.contrib import sqla
from flask_admin import BaseView, expose
from flask import abort, redirect, request, url_for
from flask_admin import helpers as admin_helpers
from flask_security import current_user

from apps.backoffice.config.security import security
from apps.backoffice.controllers.roles.RolesHomeGetWebController import RolesHomeGetWebController

admin = flask_admin.Admin(
    name='SASS Backoffice Dashboard OH-Sansi',
    base_template='my_master.html',
    template_mode='bootstrap4'
)

class MyModelView(sqla.ModelView):
    """Ejemplo: Restringe acceso a usuarios con rol superuser."""
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('superuser')

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            return redirect(url_for('security.login', next=request.url))

class CustomView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/custom_index.html')

# Registraremos modelos (Role, User, etc.) cuando tengamos los modelos
# admin.add_view(MyModelView(Role, db.session))
# admin.add_view(MyModelView(User, db.session))
# admin.add_view(CustomView(name="Custom", endpoint="custom"))
admin.add_view(RolesHomeGetWebController(name="Roles", endpoint="roles", menu_icon_type='fa', menu_icon_value='fa-connectdevelop',))

@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )