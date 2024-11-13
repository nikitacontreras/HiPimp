import os
from dotenv import load_dotenv

import api.api as API

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

API.set_credentials(username=username, password=password)

API.auth.login(API.u, API.p)

page = 1
while True:
    API.pets.list(page=page)
    API.pets.batch_buy()
    page += 1

