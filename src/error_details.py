from pydantic import BaseModel


class ErrorDetails(BaseModel):
   internal_code: str | None
   http_status_code: int
   reason: str | None
