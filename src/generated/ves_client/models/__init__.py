"""Contains all the data models used in inputs/outputs"""

from .error_response import ErrorResponse
from .errors import Errors
from .vehicle import Vehicle
from .vehicle_mot_status import VehicleMotStatus
from .vehicle_request import VehicleRequest
from .vehicle_tax_status import VehicleTaxStatus

__all__ = (
    "ErrorResponse",
    "Errors",
    "Vehicle",
    "VehicleMotStatus",
    "VehicleRequest",
    "VehicleTaxStatus",
)
