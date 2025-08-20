from enum import Enum


class DVSAMotTestOdometerUnitType3Type1(str, Enum):
    KM = "KM"
    MI = "MI"

    def __str__(self) -> str:
        return str(self.value)
