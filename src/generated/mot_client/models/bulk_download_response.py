from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_response import FileResponse


T = TypeVar("T", bound="BulkDownloadResponse")


@_attrs_define
class BulkDownloadResponse:
    """- File information from the bulk download service

    Attributes:
        bulk (Union[Unset, list['FileResponse']]): - Details about the bulk file
        delta (Union[Unset, list['FileResponse']]): - Details about the delta files
    """

    bulk: Union[Unset, list["FileResponse"]] = UNSET
    delta: Union[Unset, list["FileResponse"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bulk: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bulk, Unset):
            bulk = []
            for bulk_item_data in self.bulk:
                bulk_item = bulk_item_data.to_dict()
                bulk.append(bulk_item)

        delta: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.delta, Unset):
            delta = []
            for delta_item_data in self.delta:
                delta_item = delta_item_data.to_dict()
                delta.append(delta_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bulk is not UNSET:
            field_dict["bulk"] = bulk
        if delta is not UNSET:
            field_dict["delta"] = delta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_response import FileResponse

        d = dict(src_dict)
        bulk = []
        _bulk = d.pop("bulk", UNSET)
        for bulk_item_data in _bulk or []:
            bulk_item = FileResponse.from_dict(bulk_item_data)

            bulk.append(bulk_item)

        delta = []
        _delta = d.pop("delta", UNSET)
        for delta_item_data in _delta or []:
            delta_item = FileResponse.from_dict(delta_item_data)

            delta.append(delta_item)

        bulk_download_response = cls(
            bulk=bulk,
            delta=delta,
        )

        bulk_download_response.additional_properties = d
        return bulk_download_response

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
