from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.defect_type import DefectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Defect")


@_attrs_define
class Defect:
    """- Defects found during the MOT or annual test.

    Attributes:
        text (Union[None, Unset, str]): -  Description of the defect
        type_ (Union[Unset, DefectType]):
        dangerous (Union[None, Unset, bool]): - Whether the defect is dangerous Example: True.
    """

    text: Union[None, Unset, str] = UNSET
    type_: Union[Unset, DefectType] = UNSET
    dangerous: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        dangerous: Union[None, Unset, bool]
        if isinstance(self.dangerous, Unset):
            dangerous = UNSET
        else:
            dangerous = self.dangerous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_
        if dangerous is not UNSET:
            field_dict["dangerous"] = dangerous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("text", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DefectType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DefectType(_type_)

        def _parse_dangerous(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        dangerous = _parse_dangerous(d.pop("dangerous", UNSET))

        defect = cls(
            text=text,
            type_=type_,
            dangerous=dangerous,
        )

        defect.additional_properties = d
        return defect

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
