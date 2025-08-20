from enum import Enum


class DVANIMotTestTestResult(str, Enum):
    FAILED = "FAILED"
    PASSED = "PASSED"

    def __str__(self) -> str:
        return str(self.value)
