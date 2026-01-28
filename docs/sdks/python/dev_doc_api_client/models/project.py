from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Attributes:
        slug (str | Unset):  Example: my-docs-abc123.
        name (str | Unset):  Example: My Documentation.
        url (str | Unset):  Example: https://my-docs-abc123.devdoc.sh.
        files_count (int | Unset):  Example: 15.
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        last_deployed_at (datetime.datetime | Unset):
    """

    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    files_count: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    last_deployed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        url = self.url

        files_count = self.files_count

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        last_deployed_at: str | Unset = UNSET
        if not isinstance(self.last_deployed_at, Unset):
            last_deployed_at = self.last_deployed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if files_count is not UNSET:
            field_dict["filesCount"] = files_count
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if last_deployed_at is not UNSET:
            field_dict["lastDeployedAt"] = last_deployed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        files_count = d.pop("filesCount", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _last_deployed_at = d.pop("lastDeployedAt", UNSET)
        last_deployed_at: datetime.datetime | Unset
        if isinstance(_last_deployed_at, Unset):
            last_deployed_at = UNSET
        else:
            last_deployed_at = isoparse(_last_deployed_at)

        project = cls(
            slug=slug,
            name=name,
            url=url,
            files_count=files_count,
            created_at=created_at,
            updated_at=updated_at,
            last_deployed_at=last_deployed_at,
        )

        project.additional_properties = d
        return project

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
