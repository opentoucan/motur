from enum import Enum


class DVSAMotTestTestResult(str, Enum):
    FAILED = "FAILED"
    PASSED = "PASSED"

    def __str__(self) -> str:
        return str(self.value)
