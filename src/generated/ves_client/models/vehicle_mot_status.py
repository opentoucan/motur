from enum import Enum


class VehicleMotStatus(str, Enum):
    NOT_VALID = "Not valid"
    NO_DETAILS_HELD_BY_DVLA = "No details held by DVLA"
    NO_RESULTS_RETURNED = "No results returned"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
