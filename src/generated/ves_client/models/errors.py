from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Errors")


@_attrs_define
class Errors:
    """
    Attributes:
        title (str): Error title Example: Invalid vrn number.
        status (Union[Unset, str]):  Example: 400.
        code (Union[Unset, str]): DVLA reference code Example: 105.
        detail (Union[Unset, str]): A meaningful description of the error which has occurred Example: Invalid format for
            field - vehicle registration number.
    """

    title: str
    status: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        status = self.status

        code = self.code

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        status = d.pop("status", UNSET)

        code = d.pop("code", UNSET)

        detail = d.pop("detail", UNSET)

        errors = cls(
            title=title,
            status=status,
            code=code,
            detail=detail,
        )

        errors.additional_properties = d
        return errors

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
