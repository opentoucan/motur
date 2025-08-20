from enum import Enum


class VehicleWithMotResponseHasOutstandingRecall(str, Enum):
    NO = "No"
    UNAVAILABLE = "Unavailable"
    UNKNOWN = "Unknown"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
