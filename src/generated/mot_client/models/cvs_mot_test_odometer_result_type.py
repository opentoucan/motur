from enum import Enum


class CVSMotTestOdometerResultType(str, Enum):
    NO_ODOMETER = "NO_ODOMETER"
    READ = "READ"

    def __str__(self) -> str:
        return str(self.value)
