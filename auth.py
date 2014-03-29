from eve.auth import BasicAuth
import settings

class BasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,method):
        return username == settings.AUTH_USERNAME and password == settings.AUTH_PASSWORD