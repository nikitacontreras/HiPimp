from typing import Optional, Dict, Any

class Pet:
    def __init__(self, person: Dict[str, Any]):
        self.location: Optional[str] = person.get("location")
        self.country_code: Optional[str] = person.get("countryCode")
        self.state: Optional[str] = person.get("state")
        self.province: Optional[str] = person.get("province")
        self.city: Optional[str] = person.get("city")
        self.city_id: Optional[str] = person.get("cityId")
        self.latitude: Optional[str] = person.get("latitude")
        self.longitude: Optional[str] = person.get("longitude")
        self.zip_code: Optional[str] = person.get("zipCode")
        self.user_id: Optional[int] = person.get("userId")
        self.display_name: Optional[str] = person.get("displayName")
        self.country: Optional[str] = person.get("country")
        self.full_name: Optional[str] = person.get("fullName")
        self.age: Optional[int] = person.get("age")
        self.gender: Optional[str] = person.get("gender")
        self.primary_photo: Optional[Dict[str, Any]] = person.get("primaryPhoto")
        self.cover_photo: Optional[Any] = person.get("coverPhoto")
        self.theme_color: Optional[Any] = person.get("themeColor")
        self.last_active_date: Optional[int] = person.get("lastActiveDate")
        self.is_valid: Optional[bool] = person.get("isValid")
        self.reg_cc_iso: Optional[Any] = person.get("regCCIso")
        self.is_high_risk: Optional[bool] = person.get("isHighRisk")
        self.is_blocked: Optional[bool] = person.get("isBlocked")
        self.has_blocked_user: Optional[bool] = person.get("hasBlockedUser")
        self.live_stream_id: Optional[Any] = person.get("liveStreamId")
        self.live_broadcast_id: Optional[Any] = person.get("liveBroadcastId")
        self.brand: Optional[str] = person.get("brand")
        self.is_eu_user: Optional[bool] = person.get("isEUUser")
        self.photo_small: Optional[str] = person.get("photoSmall")
        self.photo_medium: Optional[str] = person.get("photoMedium")
        self.photo_large: Optional[str] = person.get("photoLarge")
        self.is_zombie: Optional[bool] = person.get("isZombie")
        self.is_locked: Optional[bool] = person.get("isLocked")
        self.is_deleted: Optional[bool] = person.get("isDeleted")
        self.last_active: Optional[str] = person.get("lastActive")
        self.last_active_time: Optional[int] = person.get("lastActiveTime")
        self.cash_transaction_eligible: Optional[bool] = person.get("cashTransactionEligible")
        self.opted_out: Optional[bool] = person.get("optedOut")
        self.is_undead: Optional[bool] = person.get("isUndead")
        self.id: Optional[int] = person.get("id")
        self.owner_id: Optional[int] = person.get("ownerId")
        self.can_buy: Optional[bool] = person.get("canBuy")
        self.value: Optional[str] = person.get("value")
        self.cash: Optional[str] = person.get("cash")
        self.assets: Optional[str] = person.get("assets")
        self.pet_count: Optional[int] = person.get("petCount")
        self.wisher_count: Optional[int] = person.get("wisherCount")
        self.bonus: Optional[int] = person.get("bonus")
        self.level: Optional[int] = person.get("level")
        self.assets_to_level: Optional[str] = person.get("assetsToLevel")
        self.last_purchased: Optional[int] = person.get("lastPurchased")
        self.last_traded: Optional[int] = person.get("lastTraded")
        self.rank: Optional[int] = person.get("rank")
        self.tagged_asset_rank: Optional[int] = person.get("taggedAssetRank")
        self.country_asset_rank: Optional[int] = person.get("countryAssetRank")
        self.tagged_value_rank: Optional[int] = person.get("taggedValueRank")
        self.country_value_rank: Optional[int] = person.get("countryValueRank")
        self.lock_time: Optional[int] = person.get("lockTime")
        self.unlock_time: Optional[int] = person.get("unlockTime")
        self.lock_amount: Optional[int] = person.get("lockAmount")
        self.owner: Optional[Dict[str, Any]] = person.get("owner")
        self.purchase_token: Optional[str] = person.get("purchaseToken")

    @property
    def buyable(self):
        return self.can_buy and not self.is_locked

    @property
    def money_stats(self):
        return {"cash": self.cash, "value": self.value, "assets": self.assets}

    @property
    def info(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "display_name": self.display_name,
            "full_name": self.full_name,
            "age": self.age,
            "pets": self.pet_count,
        }
