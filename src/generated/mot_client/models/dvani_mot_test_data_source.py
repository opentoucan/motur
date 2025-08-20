from enum import Enum


class DVANIMotTestDataSource(str, Enum):
    DVA_NI = "DVA NI"

    def __str__(self) -> str:
        return str(self.value)
