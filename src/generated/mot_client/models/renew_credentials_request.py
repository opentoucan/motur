from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenewCredentialsRequest")


@_attrs_define
class RenewCredentialsRequest:
    """- Information required to request a new client secret.

    Attributes:
        aws_api_key_value (Union[Unset, str]): - the api key that was issued when you registered Example: your-existing-
            aws-api-key-value.
        email (Union[Unset, str]): - the email address of the primary contact of the account Example:
            user.example@email.com.
    """

    aws_api_key_value: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_api_key_value = self.aws_api_key_value

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_api_key_value is not UNSET:
            field_dict["awsApiKeyValue"] = aws_api_key_value
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aws_api_key_value = d.pop("awsApiKeyValue", UNSET)

        email = d.pop("email", UNSET)

        renew_credentials_request = cls(
            aws_api_key_value=aws_api_key_value,
            email=email,
        )

        renew_credentials_request.additional_properties = d
        return renew_credentials_request

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
