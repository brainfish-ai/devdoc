from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeployResponse")


@_attrs_define
class DeployResponse:
    """
    Attributes:
        success (bool | Unset):  Example: True.
        slug (str | Unset): Project slug Example: my-docs-abc123.
        url (str | Unset): Live documentation URL Example: https://my-docs-abc123.devdoc.sh.
        blob_url (str | Unset): Storage URL
        is_update (bool | Unset): Whether this was an update to existing project
        files_count (int | Unset): Number of files deployed
        api_key (str | Unset): API key (only returned for new projects) Example: sk_live_abc123xyz....
    """

    success: bool | Unset = UNSET
    slug: str | Unset = UNSET
    url: str | Unset = UNSET
    blob_url: str | Unset = UNSET
    is_update: bool | Unset = UNSET
    files_count: int | Unset = UNSET
    api_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        slug = self.slug

        url = self.url

        blob_url = self.blob_url

        is_update = self.is_update

        files_count = self.files_count

        api_key = self.api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if slug is not UNSET:
            field_dict["slug"] = slug
        if url is not UNSET:
            field_dict["url"] = url
        if blob_url is not UNSET:
            field_dict["blobUrl"] = blob_url
        if is_update is not UNSET:
            field_dict["isUpdate"] = is_update
        if files_count is not UNSET:
            field_dict["filesCount"] = files_count
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        slug = d.pop("slug", UNSET)

        url = d.pop("url", UNSET)

        blob_url = d.pop("blobUrl", UNSET)

        is_update = d.pop("isUpdate", UNSET)

        files_count = d.pop("filesCount", UNSET)

        api_key = d.pop("apiKey", UNSET)

        deploy_response = cls(
            success=success,
            slug=slug,
            url=url,
            blob_url=blob_url,
            is_update=is_update,
            files_count=files_count,
            api_key=api_key,
        )

        deploy_response.additional_properties = d
        return deploy_response

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
