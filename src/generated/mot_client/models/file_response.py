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

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileResponse")


@_attrs_define
class FileResponse:
    """- File information from the bulk download service

    Attributes:
        filename (Union[Unset, str]): - filename of the downloaded file
        download_url (Union[Unset, str]): - Presigned URL for the related file:
             - URL valid for 5 mins from generation
             - Expect a .gz file which contains at least one other .gz file
        file_size (Union[Unset, float]): - Size of the ZIP file in bytes
        file_created_on (Union[Unset, datetime.date]): - Date the file was created
            - Format: YYYY-MM-DD
    """

    filename: Union[Unset, str] = UNSET
    download_url: Union[Unset, str] = UNSET
    file_size: Union[Unset, float] = UNSET
    file_created_on: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        download_url = self.download_url

        file_size = self.file_size

        file_created_on: Union[Unset, str] = UNSET
        if not isinstance(self.file_created_on, Unset):
            file_created_on = self.file_created_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if file_created_on is not UNSET:
            field_dict["fileCreatedOn"] = file_created_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename", UNSET)

        download_url = d.pop("downloadUrl", UNSET)

        file_size = d.pop("fileSize", UNSET)

        _file_created_on = d.pop("fileCreatedOn", UNSET)
        file_created_on: Union[Unset, datetime.date]
        if isinstance(_file_created_on, Unset):
            file_created_on = UNSET
        else:
            file_created_on = isoparse(_file_created_on).date()

        file_response = cls(
            filename=filename,
            download_url=download_url,
            file_size=file_size,
            file_created_on=file_created_on,
        )

        file_response.additional_properties = d
        return file_response

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
