import requests, os, json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class request:
    def __init__(self):
        self.method = None
        self.url = None
        self.data = None
        self.headers = None
        # with open(os.path.join(os.getcwd(), "cookies.json"), "r") as f:
        #     self.cookies = json.load(f)
        self.__session = requests.Session()
        self.response: requests.Response = None

    @property
    def session(self) -> requests.Session:
        return self.__session

    @session.setter
    def session(self, sess_object) -> requests.Session:
        self.__session = sess_object

    def request(self, method: str, url: str, data: dict = None, headers: dict = None):
        self.method = method
        self.url = url
        self.data = data
        self.headers = headers

        self.response = self.__req()
        return self.response

    def __req(self):
        return self.__session.request(
            self.method,
            self.url,
            headers=self.headers,
            data=self.data,
            allow_redirects=True,
            verify=False,
        )
