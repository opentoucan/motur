from enum import Enum


class VehicleTaxStatus(str, Enum):
    NOT_TAXED_FOR_ON_ROAD_USE = "Not Taxed for on Road Use"
    SORN = "SORN"
    TAXED = "Taxed"
    UNTAXED = "Untaxed"

    def __str__(self) -> str:
        return str(self.value)
