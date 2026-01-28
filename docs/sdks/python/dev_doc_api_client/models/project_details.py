from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_details_config import ProjectDetailsConfig
    from ..models.project_details_files_item import ProjectDetailsFilesItem


T = TypeVar("T", bound="ProjectDetails")


@_attrs_define
class ProjectDetails:
    """
    Attributes:
        slug (str | Unset):
        name (str | Unset):
        url (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        last_deployed_at (datetime.datetime | Unset):
        files_count (int | Unset):
        total_size (int | Unset): Total size in bytes
        files (list[ProjectDetailsFilesItem] | Unset):
        config (ProjectDetailsConfig | Unset):
    """

    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    last_deployed_at: datetime.datetime | Unset = UNSET
    files_count: int | Unset = UNSET
    total_size: int | Unset = UNSET
    files: list[ProjectDetailsFilesItem] | Unset = UNSET
    config: ProjectDetailsConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        url = self.url

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        last_deployed_at: str | Unset = UNSET
        if not isinstance(self.last_deployed_at, Unset):
            last_deployed_at = self.last_deployed_at.isoformat()

        files_count = self.files_count

        total_size = self.total_size

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if last_deployed_at is not UNSET:
            field_dict["lastDeployedAt"] = last_deployed_at
        if files_count is not UNSET:
            field_dict["filesCount"] = files_count
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size
        if files is not UNSET:
            field_dict["files"] = files
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_details_config import ProjectDetailsConfig
        from ..models.project_details_files_item import ProjectDetailsFilesItem

        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

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

        files_count = d.pop("filesCount", UNSET)

        total_size = d.pop("totalSize", UNSET)

        _files = d.pop("files", UNSET)
        files: list[ProjectDetailsFilesItem] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = ProjectDetailsFilesItem.from_dict(files_item_data)

                files.append(files_item)

        _config = d.pop("config", UNSET)
        config: ProjectDetailsConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ProjectDetailsConfig.from_dict(_config)

        project_details = cls(
            slug=slug,
            name=name,
            url=url,
            created_at=created_at,
            updated_at=updated_at,
            last_deployed_at=last_deployed_at,
            files_count=files_count,
            total_size=total_size,
            files=files,
            config=config,
        )

        project_details.additional_properties = d
        return project_details

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
