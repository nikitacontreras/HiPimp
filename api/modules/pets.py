import time
from utils.request import request
from utils.logger import message

from objects.pet import Pet


class Pets:
    def __init__(self, session: request):
        self.__req = session
        self.__petList: list = []
        pass

    def __parsePets(self, pets: list) -> list:
        for pet in pets:
            instance = Pet(pet)
            self.__petList.append(instance)

    def addToWishlist(self, pet: Pet):
        message.info(f"Adding {pet.display_name} to wishlist")
        res = self.__req.request(
            method="POST",
            url="https://hi5.com/api/?application_id=user&format=JSON",
            data={
                "method": "tagged.apps.pets.addToList",
                "uid_to_add": pet.user_id,
                "type_of_list": "wish",
            },
        )
        if res.json()["stat"] == "ok":
            message.success(f"{pet.display_name} added to wishlist")
            return True

        message.error(
            f"Failed to add {pet.display_name} to wishlist: {res.json()["error"]["message"]}"
        )
        
    def removeFromWishlist(self, pet: Pet):
        message.info(f"Removing {pet.display_name} from wishlist")
        res = self.__req.request(
            method="POST",
            url="https://hi5.com/api/?application_id=user&format=JSON",
            data={
                "method": "tagged.apps.pets.removeFromList",
                "uid_to_remove": pet.user_id,
                "type_of_list": "wish",
            },
        )
        if res.json()["stat"] == "ok":
            message.success(f"{pet.display_name} removed from wishlist")
            return True

        message.error(
            f"Failed to remove {pet.display_name} from wishlist: {res.json()["error"]["message"]}"
        )

    def addAsFriend(self, pet: Pet):
        message.info(f"Adding {pet.display_name} as friend")
        res = self.__req.request(
            method="POST",
            url="https://secure.hi5.com/api/?application_id=user&format=JSON",
            data={
                "method": "tagged.usermgmt.addFriend",
                "uid_to_add": pet.user_id,
            },
        )
        if res.json()["stat"] == "ok":
            message.success(f"{pet.display_name} added as friend")
            return True

        if res.json()["stat"] == "fail":
            errorCode = res.json()["error"]["code"]
            match errorCode:
                case 105:
                    message.error(f"Friend request already sent to {pet.display_name}")
                    return False
                
        message.error(
            f"Failed to add {pet.display_name} as friend: {res.json()["error"]["message"]}"
        )
        return False
    
    def list(self, page: int = 0, rows: int = 20):
        message.info(f"Getting pets list page {page} with {rows} rows")
        res = self.__req.request(
            method="POST",
            url="https://hi5.com/api/?application_id=user&format=JSON",
            data={
                "method": "tagged.apps.pets.getPetsBySearch",
                "num_result": rows,
                "page_num": page,
                "gender": "F",
                "min_age": 18,
                "max_age": 23,
                "value_min": 0,
                "value_max": 1999652561000000000000,
            },
        )

        if res.json()["stat"] == "fail":
            message.error(
                f"Failed to get pets list: {res.json()["error"]['message']}, trying to get list from different endpoint"
            )
            self.suggestions(rows=rows)
            return

        message.success(f"Got {len(res.json()["result"]["pets"])} pets")
        self.__parsePets(res.json()["result"]["pets"])

    def suggestions(self, rows: int = 10, max_age: int = 23):
        message.info(f"Getting pets suggestions with max age {max_age}")
        res = self.__req.request(
            method="POST",
            url="https://hi5.com/api/?application_id=user&format=JSON",
            data={
                "method": "tagged.apps.pets.getBuyPetsResults",
                "num_result": rows,
                "min_age": 18,
                "max_age": max,
                "value_min": 0,
                "value_max": 1999652561000000000000,
            },
        )

        if res.json()["stat"] == "fail":
            message.error(
                f"Failed to get pets suggestions: {res.json()["error"]['message']}"
            )
            exit(1)

        message.success(f"Got {len(res.json()["results"]["users"])} pets")
        self.__parsePets(res.json()["results"]["users"])

    def buy(
        self,
        pet: Pet,
        purchaseToken: str = None,
        price: str = None,
        owner_id: int = None,
    ):
        if not pet.buyable:
            message.error(f"{pet.display_name} is not buyable")
            return

        res = self.__req.request(
            method="POST",
            url="https://hi5.com/api/?application_id=user&format=JSON",
            data={
                "method": "tagged.apps.pets.buyPetAsync",
                "userid_to_buy": pet.user_id,
                "purchase_token": purchaseToken or pet.purchase_token,
                "pet_price": price or pet.value,
                "displayed_owner_id": owner_id or pet.owner_id,
                "ect": 0,
                "page_type": "browse",
                "source": "web",
            },
        )
        if res.json()["stat"] == "fail":
            errorCode = res.json()["error"]["code"]
            match errorCode:
                case 105:
                    new_price = res.json()["error"]["newValue"]
                    new_token = res.json()["error"]["newToken"]
                    new_owner = res.json()["error"]["newOwner"]["id"]

                    message.error(f"Price changed, new price: {new_price}")
                    self.buy(
                        pet,
                        purchaseToken=new_token,
                        price=new_price,
                        owner_id=new_owner,
                    )
                case 108:
                    message.error(
                        f"User has reached pet limit, skipping {pet.display_name}"
                    )
                    time.sleep(5)
                    return False
                case 122:
                    message.error(
                        f"Failed to buy {pet.display_name}: {res.json()["error"]["message"]}"
                    )
                    return False

        if res.json()["stat"] == "ok":
            if res.json()["results"]["boughtPetOk"] == True:
                message.success(f"{pet.display_name} bought successfully")
                return True

    def batch_buy(self):
        for pet in self.__petList:
            if (self.buy(pet) == True):
                self.addToWishlist(pet)
            # self.addAsFriend(pet)
            self.__petList.remove(pet)

    # def auto_buy(self, page: int = 0, rows: int = 20):
