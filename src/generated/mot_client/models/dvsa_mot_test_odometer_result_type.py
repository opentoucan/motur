from enum import Enum


class DVSAMotTestOdometerResultType(str, Enum):
    NO_ODOMETER = "NO_ODOMETER"
    READ = "READ"
    UNREADABLE = "UNREADABLE"

    def __str__(self) -> str:
        return str(self.value)
