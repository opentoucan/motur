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

from ..models.vehicle_with_mot_response_has_outstanding_recall import (
    VehicleWithMotResponseHasOutstandingRecall,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cvs_mot_test import CVSMotTest
    from ..models.dvani_mot_test import DVANIMotTest
    from ..models.dvsa_mot_test import DVSAMotTest


T = TypeVar("T", bound="VehicleWithMotResponse")


@_attrs_define
class VehicleWithMotResponse:
    """- Vehicle data for vehicles with at least one MOT or annual test

    Attributes:
        has_outstanding_recall (VehicleWithMotResponseHasOutstandingRecall): - One of four values from the DVSA Recalls
            service:
              - Yes (There is at least one recall which has not yet been fixed)
              - No (There were one or more recalls which have all been fixed)
              - Unknown (No known recalls have been found in the available data)
              - Unavailable (We were unable to retrieve data from the Recalls service due to an error)
        mot_tests (list[Union['CVSMotTest', 'DVANIMotTest', 'DVSAMotTest']]):
        registration (Union[None, Unset, str]): - Registration number of the vehicle
        make (Union[None, Unset, str]):  Example: Ford.
        model (Union[None, Unset, str]):  Example: Focus.
        first_used_date (Union[None, Unset, datetime.date]): - Date the vehicle is first used in Great Britain, Northern
            Ireland or abroad
            - Format: YYYY-MM-DD
        fuel_type (Union[None, Unset, str]): - The type of fuel the vehicle uses Example: Petrol.
        primary_colour (Union[None, Unset, str]):  Example: Silver.
        registration_date (Union[None, Unset, datetime.date]): - Date the vehicle is first registered in Great Britain,
            Northern Ireland or abroad
            - Format: YYYY-MM-DD
        manufacture_date (Union[None, Unset, datetime.date]): - Date the vehicle was manufactured
            - Format: YYYY-MM-DD
        engine_size (Union[None, Unset, str]): - Engine cylinder capacity (cc) of the vehicle Example: 1598.
    """

    has_outstanding_recall: VehicleWithMotResponseHasOutstandingRecall
    mot_tests: list[Union["CVSMotTest", "DVANIMotTest", "DVSAMotTest"]]
    registration: Union[None, Unset, str] = UNSET
    make: Union[None, Unset, str] = UNSET
    model: Union[None, Unset, str] = UNSET
    first_used_date: Union[None, Unset, datetime.date] = UNSET
    fuel_type: Union[None, Unset, str] = UNSET
    primary_colour: Union[None, Unset, str] = UNSET
    registration_date: Union[None, Unset, datetime.date] = UNSET
    manufacture_date: Union[None, Unset, datetime.date] = UNSET
    engine_size: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dvani_mot_test import DVANIMotTest
        from ..models.dvsa_mot_test import DVSAMotTest

        has_outstanding_recall = self.has_outstanding_recall.value

        mot_tests = []
        for mot_tests_item_data in self.mot_tests:
            mot_tests_item: dict[str, Any]
            if isinstance(mot_tests_item_data, DVSAMotTest):
                mot_tests_item = mot_tests_item_data.to_dict()
            elif isinstance(mot_tests_item_data, DVANIMotTest):
                mot_tests_item = mot_tests_item_data.to_dict()
            else:
                mot_tests_item = mot_tests_item_data.to_dict()

            mot_tests.append(mot_tests_item)

        registration: Union[None, Unset, str]
        if isinstance(self.registration, Unset):
            registration = UNSET
        else:
            registration = self.registration

        make: Union[None, Unset, str]
        if isinstance(self.make, Unset):
            make = UNSET
        else:
            make = self.make

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        first_used_date: Union[None, Unset, str]
        if isinstance(self.first_used_date, Unset):
            first_used_date = UNSET
        elif isinstance(self.first_used_date, datetime.date):
            first_used_date = self.first_used_date.isoformat()
        else:
            first_used_date = self.first_used_date

        fuel_type: Union[None, Unset, str]
        if isinstance(self.fuel_type, Unset):
            fuel_type = UNSET
        else:
            fuel_type = self.fuel_type

        primary_colour: Union[None, Unset, str]
        if isinstance(self.primary_colour, Unset):
            primary_colour = UNSET
        else:
            primary_colour = self.primary_colour

        registration_date: Union[None, Unset, str]
        if isinstance(self.registration_date, Unset):
            registration_date = UNSET
        elif isinstance(self.registration_date, datetime.date):
            registration_date = self.registration_date.isoformat()
        else:
            registration_date = self.registration_date

        manufacture_date: Union[None, Unset, str]
        if isinstance(self.manufacture_date, Unset):
            manufacture_date = UNSET
        elif isinstance(self.manufacture_date, datetime.date):
            manufacture_date = self.manufacture_date.isoformat()
        else:
            manufacture_date = self.manufacture_date

        engine_size: Union[None, Unset, str]
        if isinstance(self.engine_size, Unset):
            engine_size = UNSET
        else:
            engine_size = self.engine_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasOutstandingRecall": has_outstanding_recall,
                "motTests": mot_tests,
            }
        )
        if registration is not UNSET:
            field_dict["registration"] = registration
        if make is not UNSET:
            field_dict["make"] = make
        if model is not UNSET:
            field_dict["model"] = model
        if first_used_date is not UNSET:
            field_dict["firstUsedDate"] = first_used_date
        if fuel_type is not UNSET:
            field_dict["fuelType"] = fuel_type
        if primary_colour is not UNSET:
            field_dict["primaryColour"] = primary_colour
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if manufacture_date is not UNSET:
            field_dict["manufactureDate"] = manufacture_date
        if engine_size is not UNSET:
            field_dict["engineSize"] = engine_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cvs_mot_test import CVSMotTest
        from ..models.dvani_mot_test import DVANIMotTest
        from ..models.dvsa_mot_test import DVSAMotTest

        d = dict(src_dict)
        has_outstanding_recall = VehicleWithMotResponseHasOutstandingRecall(
            d.pop("hasOutstandingRecall")
        )

        mot_tests = []
        _mot_tests = d.pop("motTests")
        for mot_tests_item_data in _mot_tests:

            def _parse_mot_tests_item(
                data: object,
            ) -> Union["CVSMotTest", "DVANIMotTest", "DVSAMotTest"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    mot_tests_item_type_0 = DVSAMotTest.from_dict(data)

                    return mot_tests_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    mot_tests_item_type_1 = DVANIMotTest.from_dict(data)

                    return mot_tests_item_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                mot_tests_item_type_2 = CVSMotTest.from_dict(data)

                return mot_tests_item_type_2

            mot_tests_item = _parse_mot_tests_item(mot_tests_item_data)

            mot_tests.append(mot_tests_item)

        def _parse_registration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        registration = _parse_registration(d.pop("registration", UNSET))

        def _parse_make(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        make = _parse_make(d.pop("make", UNSET))

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_first_used_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_used_date_type_0 = isoparse(data).date()

                return first_used_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        first_used_date = _parse_first_used_date(d.pop("firstUsedDate", UNSET))

        def _parse_fuel_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fuel_type = _parse_fuel_type(d.pop("fuelType", UNSET))

        def _parse_primary_colour(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_colour = _parse_primary_colour(d.pop("primaryColour", UNSET))

        def _parse_registration_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_date_type_0 = isoparse(data).date()

                return registration_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        registration_date = _parse_registration_date(d.pop("registrationDate", UNSET))

        def _parse_manufacture_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manufacture_date_type_0 = isoparse(data).date()

                return manufacture_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        manufacture_date = _parse_manufacture_date(d.pop("manufactureDate", UNSET))

        def _parse_engine_size(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        engine_size = _parse_engine_size(d.pop("engineSize", UNSET))

        vehicle_with_mot_response = cls(
            has_outstanding_recall=has_outstanding_recall,
            mot_tests=mot_tests,
            registration=registration,
            make=make,
            model=model,
            first_used_date=first_used_date,
            fuel_type=fuel_type,
            primary_colour=primary_colour,
            registration_date=registration_date,
            manufacture_date=manufacture_date,
            engine_size=engine_size,
        )

        vehicle_with_mot_response.additional_properties = d
        return vehicle_with_mot_response

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
