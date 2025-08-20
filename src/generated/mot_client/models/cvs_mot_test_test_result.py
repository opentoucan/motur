from enum import Enum


class CVSMotTestTestResult(str, Enum):
    FAILED = "FAILED"
    PASSED = "PASSED"

    def __str__(self) -> str:
        return str(self.value)
