from . import api
from api.resources.registration import RegistrationAPI
from api.resources.login import LoginAPI
from api.resources.test import TestAPI
from api.resources.user import UserAPI
api.add_resource(RegistrationAPI,'/registration',strict_slashes=False)
api.add_resource(LoginAPI,'/login',strict_slashes=False)
api.add_resource(TestAPI,'/test',strict_slashes=False)
api.add_resource(UserAPI,'/user',strict_slashes=False)
