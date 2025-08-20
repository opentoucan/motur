from enum import Enum


class DVANIMotTestOdometerResultType(str, Enum):
    NO_ODOMETER = "NO_ODOMETER"
    READ = "READ"

    def __str__(self) -> str:
        return str(self.value)
