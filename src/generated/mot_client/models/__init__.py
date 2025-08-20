"""Contains all the data models used in inputs/outputs"""

from .bulk_download_response import BulkDownloadResponse
from .cvs_mot_test import CVSMotTest
from .cvs_mot_test_data_source import CVSMotTestDataSource
from .cvs_mot_test_odometer_result_type import CVSMotTestOdometerResultType
from .cvs_mot_test_odometer_unit_type_1 import CVSMotTestOdometerUnitType1
from .cvs_mot_test_odometer_unit_type_2_type_1 import CVSMotTestOdometerUnitType2Type1
from .cvs_mot_test_odometer_unit_type_3_type_1 import CVSMotTestOdometerUnitType3Type1
from .cvs_mot_test_test_result import CVSMotTestTestResult
from .defect import Defect
from .defect_type import DefectType
from .dvani_mot_test import DVANIMotTest
from .dvani_mot_test_data_source import DVANIMotTestDataSource
from .dvani_mot_test_odometer_result_type import DVANIMotTestOdometerResultType
from .dvani_mot_test_odometer_unit_type_1 import DVANIMotTestOdometerUnitType1
from .dvani_mot_test_odometer_unit_type_2_type_1 import (
    DVANIMotTestOdometerUnitType2Type1,
)
from .dvani_mot_test_odometer_unit_type_3_type_1 import (
    DVANIMotTestOdometerUnitType3Type1,
)
from .dvani_mot_test_test_result import DVANIMotTestTestResult
from .dvsa_mot_test import DVSAMotTest
from .dvsa_mot_test_data_source import DVSAMotTestDataSource
from .dvsa_mot_test_odometer_result_type import DVSAMotTestOdometerResultType
from .dvsa_mot_test_odometer_unit_type_1 import DVSAMotTestOdometerUnitType1
from .dvsa_mot_test_odometer_unit_type_2_type_1 import DVSAMotTestOdometerUnitType2Type1
from .dvsa_mot_test_odometer_unit_type_3_type_1 import DVSAMotTestOdometerUnitType3Type1
from .dvsa_mot_test_test_result import DVSAMotTestTestResult
from .error_response import ErrorResponse
from .file_response import FileResponse
from .new_reg_vehicle_response import NewRegVehicleResponse
from .new_reg_vehicle_response_has_outstanding_recall import (
    NewRegVehicleResponseHasOutstandingRecall,
)
from .renew_credentials_request import RenewCredentialsRequest
from .renew_credentials_response import RenewCredentialsResponse
from .vehicle_with_mot_response import VehicleWithMotResponse
from .vehicle_with_mot_response_has_outstanding_recall import (
    VehicleWithMotResponseHasOutstandingRecall,
)

__all__ = (
    "BulkDownloadResponse",
    "CVSMotTest",
    "CVSMotTestDataSource",
    "CVSMotTestOdometerResultType",
    "CVSMotTestOdometerUnitType1",
    "CVSMotTestOdometerUnitType2Type1",
    "CVSMotTestOdometerUnitType3Type1",
    "CVSMotTestTestResult",
    "Defect",
    "DefectType",
    "DVANIMotTest",
    "DVANIMotTestDataSource",
    "DVANIMotTestOdometerResultType",
    "DVANIMotTestOdometerUnitType1",
    "DVANIMotTestOdometerUnitType2Type1",
    "DVANIMotTestOdometerUnitType3Type1",
    "DVANIMotTestTestResult",
    "DVSAMotTest",
    "DVSAMotTestDataSource",
    "DVSAMotTestOdometerResultType",
    "DVSAMotTestOdometerUnitType1",
    "DVSAMotTestOdometerUnitType2Type1",
    "DVSAMotTestOdometerUnitType3Type1",
    "DVSAMotTestTestResult",
    "ErrorResponse",
    "FileResponse",
    "NewRegVehicleResponse",
    "NewRegVehicleResponseHasOutstandingRecall",
    "RenewCredentialsRequest",
    "RenewCredentialsResponse",
    "VehicleWithMotResponse",
    "VehicleWithMotResponseHasOutstandingRecall",
)
