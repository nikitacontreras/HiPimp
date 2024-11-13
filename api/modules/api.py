from typing import Union, Literal

class apiFormatter:
    def __init__(self, data):
        self.method = data["method"]
        self.num_results: int = 20
        self.gender: Union[Literal["F"], Literal["M"]] = "F"
        self.min_age: int = 18
        self.max_age: int = 100
        self.country: int = -1
        self.source = "web"