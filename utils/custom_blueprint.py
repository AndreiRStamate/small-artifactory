from flask import Blueprint
from utils.auth_utils import require_api_key

class SecureBlueprint(Blueprint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.before_request(self.check_api_key)

    def check_api_key(self):
        require_api_key()

class OpenBlueprint(Blueprint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass