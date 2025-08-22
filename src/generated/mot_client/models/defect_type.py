from enum import Enum


class DefectType(str, Enum):
    ADVISORY = "ADVISORY"
    DANGEROUS = "DANGEROUS"
    FAIL = "FAIL"
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    NON_SPECIFIC = "NON SPECIFIC"
    SYSTEM_GENERATED = "SYSTEM GENERATED"
    USER_ENTERED = "USER ENTERED"
    PRS = "PRS" # This is missing from the OpenAPI spec

    def __str__(self) -> str:
        return str(self.value)
