from enum import Enum


class CVSMotTestDataSource(str, Enum):
    CVS = "CVS"

    def __str__(self) -> str:
        return str(self.value)
