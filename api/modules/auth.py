from utils.request import request
from bs4 import BeautifulSoup
from utils.logger import message


class Auth:
    def __init__(
        self,
        session: request,
        endpoint: str = "https://secure.hi5.com/secure_login.html?ver=2&display=full",
        username: str = None,
        password: str = None,
    ):
        self.__req = session
        self.__endpoint: str = endpoint

        self.username: str = username
        self.password: str = password

    def __getToken(self, username: str, password: str):
        message.info(f"Getting token for {username}")
        content = self.__req.session.get(self.__endpoint).text
        soup = BeautifulSoup(content, "html.parser")
        token = soup.find("input", {"id": "token"})["value"]
        message.success(f"Token found: {token}")
        return token

    def __checkIfLoginSuccessful(self, response_text: str) -> bool:
        message.info("Checking if login was successful")
        soup = BeautifulSoup(response_text, "html.parser")
        error_box_filler = soup.find(id="error_box_filler")
        error_box_login = soup.find(id="error_box_login")
        (
            message.success("Login successful")
            if not error_box_filler and not error_box_login
            else message.error("Login failed")
        )
        return error_box_filler is not None or error_box_login is not None

    def login(self, username: str, password: str) -> bool:
        response = self.__req.request(
            method="POST",
            url=self.__endpoint,
            data={
                "username": username,
                "password": password,
                "token": self.__getToken(username, password),
            },
        )
        return not self.__checkIfLoginSuccessful(response.text)

    @property
    def session_key(self):
        return self.session.cookies.get("session_key")
