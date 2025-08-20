import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dvsa_mot_test_data_source import DVSAMotTestDataSource
from ..models.dvsa_mot_test_odometer_result_type import DVSAMotTestOdometerResultType
from ..models.dvsa_mot_test_odometer_unit_type_1 import DVSAMotTestOdometerUnitType1
from ..models.dvsa_mot_test_odometer_unit_type_2_type_1 import (
    DVSAMotTestOdometerUnitType2Type1,
)
from ..models.dvsa_mot_test_odometer_unit_type_3_type_1 import (
    DVSAMotTestOdometerUnitType3Type1,
)
from ..models.dvsa_mot_test_test_result import DVSAMotTestTestResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.defect import Defect


T = TypeVar("T", bound="DVSAMotTest")


@_attrs_define
class DVSAMotTest:
    """- Test result information from DVSA (Driver and Vehicle Standards Agency, Great Britain)

    Attributes:
        completed_date (datetime.datetime): - Date-time the test was completed.
            - ISO Standard Date Format Example: 2023-02-17T09:17:46.000Z.
        test_result (DVSAMotTestTestResult): - Result of the MOT test. Only Passed or Failed tests are included.
            Example: PASSED.
        odometer_result_type (DVSAMotTestOdometerResultType): - Whether or not the odometer was read during the MOT
            test. NO_ODOMETER means that a value is not available
        data_source (DVSAMotTestDataSource): - Source of the MOT test data.  In this case, DVSA (Driver and Vehicle
            Standards Agency, Great Britain)
        registration_at_time_of_test (Union[None, Unset, str]): - Registration number of the vehicle at the time of the
            test Example: AA51AAA.
        expiry_date (Union[None, Unset, datetime.date]): - Date the MOT test will expire
            - Format: YYYY-MM-DD
        odometer_value (Union[None, Unset, str]): - Odometer reading, if read
        odometer_unit (Union[DVSAMotTestOdometerUnitType1, DVSAMotTestOdometerUnitType2Type1,
            DVSAMotTestOdometerUnitType3Type1, None, Unset]): - Whether the odometer was read in miles or kilometres
            Example: MI.
        mot_test_number (Union[None, Unset, str]): - 12 digit MOT test number
        defects (Union[None, Unset, list['Defect']]): - Defects found during the MOT test
    """

    completed_date: datetime.datetime
    test_result: DVSAMotTestTestResult
    odometer_result_type: DVSAMotTestOdometerResultType
    data_source: DVSAMotTestDataSource
    registration_at_time_of_test: Union[None, Unset, str] = UNSET
    expiry_date: Union[None, Unset, datetime.date] = UNSET
    odometer_value: Union[None, Unset, str] = UNSET
    odometer_unit: Union[
        DVSAMotTestOdometerUnitType1,
        DVSAMotTestOdometerUnitType2Type1,
        DVSAMotTestOdometerUnitType3Type1,
        None,
        Unset,
    ] = UNSET
    mot_test_number: Union[None, Unset, str] = UNSET
    defects: Union[None, Unset, list["Defect"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed_date = self.completed_date.isoformat()

        test_result = self.test_result.value

        odometer_result_type = self.odometer_result_type.value

        data_source = self.data_source.value

        registration_at_time_of_test: Union[None, Unset, str]
        if isinstance(self.registration_at_time_of_test, Unset):
            registration_at_time_of_test = UNSET
        else:
            registration_at_time_of_test = self.registration_at_time_of_test

        expiry_date: Union[None, Unset, str]
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        odometer_value: Union[None, Unset, str]
        if isinstance(self.odometer_value, Unset):
            odometer_value = UNSET
        else:
            odometer_value = self.odometer_value

        odometer_unit: Union[None, Unset, str]
        if isinstance(self.odometer_unit, Unset):
            odometer_unit = UNSET
        elif isinstance(self.odometer_unit, DVSAMotTestOdometerUnitType1):
            odometer_unit = self.odometer_unit.value
        elif isinstance(self.odometer_unit, DVSAMotTestOdometerUnitType2Type1):
            odometer_unit = self.odometer_unit.value
        elif isinstance(self.odometer_unit, DVSAMotTestOdometerUnitType3Type1):
            odometer_unit = self.odometer_unit.value
        else:
            odometer_unit = self.odometer_unit

        mot_test_number: Union[None, Unset, str]
        if isinstance(self.mot_test_number, Unset):
            mot_test_number = UNSET
        else:
            mot_test_number = self.mot_test_number

        defects: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.defects, Unset):
            defects = UNSET
        elif isinstance(self.defects, list):
            defects = []
            for defects_type_0_item_data in self.defects:
                defects_type_0_item = defects_type_0_item_data.to_dict()
                defects.append(defects_type_0_item)

        else:
            defects = self.defects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completedDate": completed_date,
                "testResult": test_result,
                "odometerResultType": odometer_result_type,
                "dataSource": data_source,
            }
        )
        if registration_at_time_of_test is not UNSET:
            field_dict["registrationAtTimeOfTest"] = registration_at_time_of_test
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if odometer_value is not UNSET:
            field_dict["odometerValue"] = odometer_value
        if odometer_unit is not UNSET:
            field_dict["odometerUnit"] = odometer_unit
        if mot_test_number is not UNSET:
            field_dict["motTestNumber"] = mot_test_number
        if defects is not UNSET:
            field_dict["defects"] = defects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.defect import Defect

        d = dict(src_dict)
        completed_date = isoparse(d.pop("completedDate"))

        test_result = DVSAMotTestTestResult(d.pop("testResult"))

        odometer_result_type = DVSAMotTestOdometerResultType(
            d.pop("odometerResultType")
        )

        data_source = DVSAMotTestDataSource(d.pop("dataSource"))

        def _parse_registration_at_time_of_test(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        registration_at_time_of_test = _parse_registration_at_time_of_test(
            d.pop("registrationAtTimeOfTest", UNSET)
        )

        def _parse_expiry_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = isoparse(data).date()

                return expiry_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        expiry_date = _parse_expiry_date(d.pop("expiryDate", UNSET))

        def _parse_odometer_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        odometer_value = _parse_odometer_value(d.pop("odometerValue", UNSET))

        def _parse_odometer_unit(
            data: object,
        ) -> Union[
            DVSAMotTestOdometerUnitType1,
            DVSAMotTestOdometerUnitType2Type1,
            DVSAMotTestOdometerUnitType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                odometer_unit_type_1 = DVSAMotTestOdometerUnitType1(data)

                return odometer_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                odometer_unit_type_2_type_1 = DVSAMotTestOdometerUnitType2Type1(data)

                return odometer_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                odometer_unit_type_3_type_1 = DVSAMotTestOdometerUnitType3Type1(data)

                return odometer_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    DVSAMotTestOdometerUnitType1,
                    DVSAMotTestOdometerUnitType2Type1,
                    DVSAMotTestOdometerUnitType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        odometer_unit = _parse_odometer_unit(d.pop("odometerUnit", UNSET))

        def _parse_mot_test_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mot_test_number = _parse_mot_test_number(d.pop("motTestNumber", UNSET))

        def _parse_defects(data: object) -> Union[None, Unset, list["Defect"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                defects_type_0 = []
                _defects_type_0 = data
                for defects_type_0_item_data in _defects_type_0:
                    defects_type_0_item = Defect.from_dict(defects_type_0_item_data)

                    defects_type_0.append(defects_type_0_item)

                return defects_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Defect"]], data)

        defects = _parse_defects(d.pop("defects", UNSET))

        dvsa_mot_test = cls(
            completed_date=completed_date,
            test_result=test_result,
            odometer_result_type=odometer_result_type,
            data_source=data_source,
            registration_at_time_of_test=registration_at_time_of_test,
            expiry_date=expiry_date,
            odometer_value=odometer_value,
            odometer_unit=odometer_unit,
            mot_test_number=mot_test_number,
            defects=defects,
        )

        dvsa_mot_test.additional_properties = d
        return dvsa_mot_test

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
