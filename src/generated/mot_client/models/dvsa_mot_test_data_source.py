from enum import Enum


class DVSAMotTestDataSource(str, Enum):
    DVSA = "DVSA"

    def __str__(self) -> str:
        return str(self.value)
