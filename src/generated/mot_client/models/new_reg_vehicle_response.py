import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.new_reg_vehicle_response_has_outstanding_recall import (
    NewRegVehicleResponseHasOutstandingRecall,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewRegVehicleResponse")


@_attrs_define
class NewRegVehicleResponse:
    """- Vehicle data for newly registered vehicles

    Attributes:
        has_outstanding_recall (NewRegVehicleResponseHasOutstandingRecall): - One of four values from the DVSA Recalls
            service:
              - Yes (There is at least one recall which has not yet been fixed)
              - No (There were one or more recalls which have all been fixed)
              - Unknown (No known recalls have been found in the available data)
              - Unavailable (We were unable to retrieve data from the Recalls service due to an error)
        registration (Union[None, Unset, str]): - Registration number of the vehicle
        make (Union[None, Unset, str]): - Name of the vehicle manufacturer Example: Ford.
        model (Union[None, Unset, str]): - Model of the vehicle Example: Focus.
        manufacture_year (Union[None, Unset, str]): - The year the vehicle was manufactured
            - Format: YYYY Example: 2024.
        fuel_type (Union[None, Unset, str]): - The type of fuel the vehicle uses Example: Petrol.
        primary_colour (Union[None, Unset, str]): - Primary paint colour of the vehicle Example: Silver.
        registration_date (Union[None, Unset, datetime.date]): - Date the vehicle was first registered
            - Format: YYYY-MM-DD
        manufacture_date (Union[None, Unset, datetime.date]): - Date the vehicle was manufactured
            - Format: YYYY-MM-DD
        mot_test_due_date (Union[None, Unset, datetime.date]): - Date the first MOT test is due
            - Format: YYYY-MM-DD
    """

    has_outstanding_recall: NewRegVehicleResponseHasOutstandingRecall
    registration: Union[None, Unset, str] = UNSET
    make: Union[None, Unset, str] = UNSET
    model: Union[None, Unset, str] = UNSET
    manufacture_year: Union[None, Unset, str] = UNSET
    fuel_type: Union[None, Unset, str] = UNSET
    primary_colour: Union[None, Unset, str] = UNSET
    registration_date: Union[None, Unset, datetime.date] = UNSET
    manufacture_date: Union[None, Unset, datetime.date] = UNSET
    mot_test_due_date: Union[None, Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_outstanding_recall = self.has_outstanding_recall.value

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

        manufacture_year: Union[None, Unset, str]
        if isinstance(self.manufacture_year, Unset):
            manufacture_year = UNSET
        else:
            manufacture_year = self.manufacture_year

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

        mot_test_due_date: Union[None, Unset, str]
        if isinstance(self.mot_test_due_date, Unset):
            mot_test_due_date = UNSET
        elif isinstance(self.mot_test_due_date, datetime.date):
            mot_test_due_date = self.mot_test_due_date.isoformat()
        else:
            mot_test_due_date = self.mot_test_due_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasOutstandingRecall": has_outstanding_recall,
            }
        )
        if registration is not UNSET:
            field_dict["registration"] = registration
        if make is not UNSET:
            field_dict["make"] = make
        if model is not UNSET:
            field_dict["model"] = model
        if manufacture_year is not UNSET:
            field_dict["manufactureYear"] = manufacture_year
        if fuel_type is not UNSET:
            field_dict["fuelType"] = fuel_type
        if primary_colour is not UNSET:
            field_dict["primaryColour"] = primary_colour
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if manufacture_date is not UNSET:
            field_dict["manufactureDate"] = manufacture_date
        if mot_test_due_date is not UNSET:
            field_dict["motTestDueDate"] = mot_test_due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_outstanding_recall = NewRegVehicleResponseHasOutstandingRecall(
            d.pop("hasOutstandingRecall")
        )

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

        def _parse_manufacture_year(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        manufacture_year = _parse_manufacture_year(d.pop("manufactureYear", UNSET))

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

        def _parse_mot_test_due_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mot_test_due_date_type_0 = isoparse(data).date()

                return mot_test_due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        mot_test_due_date = _parse_mot_test_due_date(d.pop("motTestDueDate", UNSET))

        new_reg_vehicle_response = cls(
            has_outstanding_recall=has_outstanding_recall,
            registration=registration,
            make=make,
            model=model,
            manufacture_year=manufacture_year,
            fuel_type=fuel_type,
            primary_colour=primary_colour,
            registration_date=registration_date,
            manufacture_date=manufacture_date,
            mot_test_due_date=mot_test_due_date,
        )

        new_reg_vehicle_response.additional_properties = d
        return new_reg_vehicle_response

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
