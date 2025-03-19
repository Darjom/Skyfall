# apps/backoffice/middlewares/SessionAuth.py
from functools import wraps
from flask import session, redirect, url_for, abort, request


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("user_id"):
            return redirect(url_for('security.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def roles_required(*roles):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_role = session.get("user_role")
            if user_role not in roles:
                return abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return wrapper