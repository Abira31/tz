from functools import wraps
from flask_login import current_user
from flask import redirect
def is_admin():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if not current_user.is_admin:
                return fn(*args, **kwargs)
            else:
                return redirect('/profil')
        return decorator
    return wrapper