import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from .modules.pets import Pets
from .modules.auth import Auth

from utils.request import request

req = request()

pets = Pets(session=req)
auth = Auth(session=req)

u, p = None, None

def set_credentials(username: str, password: str):
    global u, p
    u, p = username, password