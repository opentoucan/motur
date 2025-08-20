import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vehicle_mot_status import VehicleMotStatus
from ..models.vehicle_tax_status import VehicleTaxStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vehicle")


@_attrs_define
class Vehicle:
    """
    Attributes:
        registration_number (str): Registration number of the vehicle Example: WN67DSO.
        tax_status (Union[Unset, VehicleTaxStatus]): Tax status of the vehicle Example: Untaxed.
        tax_due_date (Union[Unset, datetime.date]): Date of tax liability, used in calculating licence information
            presented to user Example: 2017-12-25.
        art_end_date (Union[Unset, datetime.date]): Additional Rate of Tax End Date, format: YYYY-MM-DD Example:
            2007-12-25.
        mot_status (Union[Unset, VehicleMotStatus]): MOT Status of the vehicle Example: No details held by DVLA.
        mot_expiry_date (Union[Unset, datetime.date]): Mot Expiry Date Example: 2008-12-25.
        make (Union[Unset, str]): Vehicle make Example: ROVER.
        month_of_first_dvla_registration (Union[Unset, datetime.date]): Month of First DVLA Registration Example:
            2011-11.
        month_of_first_registration (Union[Unset, datetime.date]): Month of First Registration Example: 2012-12.
        year_of_manufacture (Union[Unset, int]): Year of Manufacture Example: 2004.
        engine_capacity (Union[Unset, int]): Engine capacity in cubic centimetres Example: 1796.
        co_2_emissions (Union[Unset, int]): Carbon Dioxide emissions in grams per kilometre
        fuel_type (Union[Unset, str]): Fuel type (Method of Propulsion) Example: PETROL.
        marked_for_export (Union[Unset, bool]): True only if vehicle has been export marked Example: True.
        colour (Union[Unset, str]): Vehicle colour Example: Blue.
        type_approval (Union[Unset, str]): Vehicle Type Approval Category Example: N1.
        wheelplan (Union[Unset, str]): Vehicle wheel plan Example: NON STANDARD.
        revenue_weight (Union[Unset, int]): Revenue weight in kilograms Example: 1640.
        real_driving_emissions (Union[Unset, str]): Real Driving Emissions value Example: 1.
        date_of_last_v5c_issued (Union[Unset, datetime.date]): Date of last V5C issued Example: 2016-12-25.
        euro_status (Union[Unset, str]): Euro Status (Dealer / Customer Provided (new vehicles)) Example: Euro 5.
        automated_vehicle (Union[Unset, bool]): Automated Vehicle (AV) Example: True.
    """

    registration_number: str
    tax_status: Union[Unset, VehicleTaxStatus] = UNSET
    tax_due_date: Union[Unset, datetime.date] = UNSET
    art_end_date: Union[Unset, datetime.date] = UNSET
    mot_status: Union[Unset, VehicleMotStatus] = UNSET
    mot_expiry_date: Union[Unset, datetime.date] = UNSET
    make: Union[Unset, str] = UNSET
    month_of_first_dvla_registration: Union[Unset, datetime.date] = UNSET
    month_of_first_registration: Union[Unset, datetime.date] = UNSET
    year_of_manufacture: Union[Unset, int] = UNSET
    engine_capacity: Union[Unset, int] = UNSET
    co_2_emissions: Union[Unset, int] = UNSET
    fuel_type: Union[Unset, str] = UNSET
    marked_for_export: Union[Unset, bool] = UNSET
    colour: Union[Unset, str] = UNSET
    type_approval: Union[Unset, str] = UNSET
    wheelplan: Union[Unset, str] = UNSET
    revenue_weight: Union[Unset, int] = UNSET
    real_driving_emissions: Union[Unset, str] = UNSET
    date_of_last_v5c_issued: Union[Unset, datetime.date] = UNSET
    euro_status: Union[Unset, str] = UNSET
    automated_vehicle: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registration_number = self.registration_number

        tax_status: Union[Unset, str] = UNSET
        if not isinstance(self.tax_status, Unset):
            tax_status = self.tax_status.value

        tax_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.tax_due_date, Unset):
            tax_due_date = self.tax_due_date.isoformat()

        art_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.art_end_date, Unset):
            art_end_date = self.art_end_date.isoformat()

        mot_status: Union[Unset, str] = UNSET
        if not isinstance(self.mot_status, Unset):
            mot_status = self.mot_status.value

        mot_expiry_date: Union[Unset, str] = UNSET
        if not isinstance(self.mot_expiry_date, Unset):
            mot_expiry_date = self.mot_expiry_date.isoformat()

        make = self.make

        month_of_first_dvla_registration: Union[Unset, str] = UNSET
        if not isinstance(self.month_of_first_dvla_registration, Unset):
            month_of_first_dvla_registration = (
                self.month_of_first_dvla_registration.isoformat()
            )

        month_of_first_registration: Union[Unset, str] = UNSET
        if not isinstance(self.month_of_first_registration, Unset):
            month_of_first_registration = self.month_of_first_registration.isoformat()

        year_of_manufacture = self.year_of_manufacture

        engine_capacity = self.engine_capacity

        co_2_emissions = self.co_2_emissions

        fuel_type = self.fuel_type

        marked_for_export = self.marked_for_export

        colour = self.colour

        type_approval = self.type_approval

        wheelplan = self.wheelplan

        revenue_weight = self.revenue_weight

        real_driving_emissions = self.real_driving_emissions

        date_of_last_v5c_issued: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_last_v5c_issued, Unset):
            date_of_last_v5c_issued = self.date_of_last_v5c_issued.isoformat()

        euro_status = self.euro_status

        automated_vehicle = self.automated_vehicle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrationNumber": registration_number,
            }
        )
        if tax_status is not UNSET:
            field_dict["taxStatus"] = tax_status
        if tax_due_date is not UNSET:
            field_dict["taxDueDate"] = tax_due_date
        if art_end_date is not UNSET:
            field_dict["artEndDate"] = art_end_date
        if mot_status is not UNSET:
            field_dict["motStatus"] = mot_status
        if mot_expiry_date is not UNSET:
            field_dict["motExpiryDate"] = mot_expiry_date
        if make is not UNSET:
            field_dict["make"] = make
        if month_of_first_dvla_registration is not UNSET:
            field_dict["monthOfFirstDvlaRegistration"] = (
                month_of_first_dvla_registration
            )
        if month_of_first_registration is not UNSET:
            field_dict["monthOfFirstRegistration"] = month_of_first_registration
        if year_of_manufacture is not UNSET:
            field_dict["yearOfManufacture"] = year_of_manufacture
        if engine_capacity is not UNSET:
            field_dict["engineCapacity"] = engine_capacity
        if co_2_emissions is not UNSET:
            field_dict["co2Emissions"] = co_2_emissions
        if fuel_type is not UNSET:
            field_dict["fuelType"] = fuel_type
        if marked_for_export is not UNSET:
            field_dict["markedForExport"] = marked_for_export
        if colour is not UNSET:
            field_dict["colour"] = colour
        if type_approval is not UNSET:
            field_dict["typeApproval"] = type_approval
        if wheelplan is not UNSET:
            field_dict["wheelplan"] = wheelplan
        if revenue_weight is not UNSET:
            field_dict["revenueWeight"] = revenue_weight
        if real_driving_emissions is not UNSET:
            field_dict["realDrivingEmissions"] = real_driving_emissions
        if date_of_last_v5c_issued is not UNSET:
            field_dict["dateOfLastV5CIssued"] = date_of_last_v5c_issued
        if euro_status is not UNSET:
            field_dict["euroStatus"] = euro_status
        if automated_vehicle is not UNSET:
            field_dict["automatedVehicle"] = automated_vehicle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        registration_number = d.pop("registrationNumber")

        _tax_status = d.pop("taxStatus", UNSET)
        tax_status: Union[Unset, VehicleTaxStatus]
        if isinstance(_tax_status, Unset):
            tax_status = UNSET
        else:
            tax_status = VehicleTaxStatus(_tax_status)

        _tax_due_date = d.pop("taxDueDate", UNSET)
        tax_due_date: Union[Unset, datetime.date]
        if isinstance(_tax_due_date, Unset):
            tax_due_date = UNSET
        else:
            tax_due_date = isoparse(_tax_due_date).date()

        _art_end_date = d.pop("artEndDate", UNSET)
        art_end_date: Union[Unset, datetime.date]
        if isinstance(_art_end_date, Unset):
            art_end_date = UNSET
        else:
            art_end_date = isoparse(_art_end_date).date()

        _mot_status = d.pop("motStatus", UNSET)
        mot_status: Union[Unset, VehicleMotStatus]
        if isinstance(_mot_status, Unset):
            mot_status = UNSET
        else:
            mot_status = VehicleMotStatus(_mot_status)

        _mot_expiry_date = d.pop("motExpiryDate", UNSET)
        mot_expiry_date: Union[Unset, datetime.date]
        if isinstance(_mot_expiry_date, Unset):
            mot_expiry_date = UNSET
        else:
            mot_expiry_date = isoparse(_mot_expiry_date).date()

        make = d.pop("make", UNSET)

        _month_of_first_dvla_registration = d.pop("monthOfFirstDvlaRegistration", UNSET)
        month_of_first_dvla_registration: Union[Unset, datetime.date]
        if isinstance(_month_of_first_dvla_registration, Unset):
            month_of_first_dvla_registration = UNSET
        else:
            month_of_first_dvla_registration = isoparse(
                _month_of_first_dvla_registration
            ).date()

        _month_of_first_registration = d.pop("monthOfFirstRegistration", UNSET)
        month_of_first_registration: Union[Unset, datetime.date]
        if isinstance(_month_of_first_registration, Unset):
            month_of_first_registration = UNSET
        else:
            month_of_first_registration = isoparse(_month_of_first_registration).date()

        year_of_manufacture = d.pop("yearOfManufacture", UNSET)

        engine_capacity = d.pop("engineCapacity", UNSET)

        co_2_emissions = d.pop("co2Emissions", UNSET)

        fuel_type = d.pop("fuelType", UNSET)

        marked_for_export = d.pop("markedForExport", UNSET)

        colour = d.pop("colour", UNSET)

        type_approval = d.pop("typeApproval", UNSET)

        wheelplan = d.pop("wheelplan", UNSET)

        revenue_weight = d.pop("revenueWeight", UNSET)

        real_driving_emissions = d.pop("realDrivingEmissions", UNSET)

        _date_of_last_v5c_issued = d.pop("dateOfLastV5CIssued", UNSET)
        date_of_last_v5c_issued: Union[Unset, datetime.date]
        if isinstance(_date_of_last_v5c_issued, Unset):
            date_of_last_v5c_issued = UNSET
        else:
            date_of_last_v5c_issued = isoparse(_date_of_last_v5c_issued).date()

        euro_status = d.pop("euroStatus", UNSET)

        automated_vehicle = d.pop("automatedVehicle", UNSET)

        vehicle = cls(
            registration_number=registration_number,
            tax_status=tax_status,
            tax_due_date=tax_due_date,
            art_end_date=art_end_date,
            mot_status=mot_status,
            mot_expiry_date=mot_expiry_date,
            make=make,
            month_of_first_dvla_registration=month_of_first_dvla_registration,
            month_of_first_registration=month_of_first_registration,
            year_of_manufacture=year_of_manufacture,
            engine_capacity=engine_capacity,
            co_2_emissions=co_2_emissions,
            fuel_type=fuel_type,
            marked_for_export=marked_for_export,
            colour=colour,
            type_approval=type_approval,
            wheelplan=wheelplan,
            revenue_weight=revenue_weight,
            real_driving_emissions=real_driving_emissions,
            date_of_last_v5c_issued=date_of_last_v5c_issued,
            euro_status=euro_status,
            automated_vehicle=automated_vehicle,
        )

        vehicle.additional_properties = d
        return vehicle

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
