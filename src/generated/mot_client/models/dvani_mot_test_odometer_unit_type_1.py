from enum import Enum


class DVANIMotTestOdometerUnitType1(str, Enum):
    KM = "KM"
    MI = "MI"

    def __str__(self) -> str:
        return str(self.value)
