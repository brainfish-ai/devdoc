from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectStatsStats")


@_attrs_define
class ProjectStatsStats:
    """
    Attributes:
        total_files (int | Unset):
        mdx_pages (int | Unset):
        config_files (int | Unset):
        other_files (int | Unset):
        total_size_bytes (int | Unset):
        total_size_kb (float | Unset):
    """

    total_files: int | Unset = UNSET
    mdx_pages: int | Unset = UNSET
    config_files: int | Unset = UNSET
    other_files: int | Unset = UNSET
    total_size_bytes: int | Unset = UNSET
    total_size_kb: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_files = self.total_files

        mdx_pages = self.mdx_pages

        config_files = self.config_files

        other_files = self.other_files

        total_size_bytes = self.total_size_bytes

        total_size_kb = self.total_size_kb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_files is not UNSET:
            field_dict["totalFiles"] = total_files
        if mdx_pages is not UNSET:
            field_dict["mdxPages"] = mdx_pages
        if config_files is not UNSET:
            field_dict["configFiles"] = config_files
        if other_files is not UNSET:
            field_dict["otherFiles"] = other_files
        if total_size_bytes is not UNSET:
            field_dict["totalSizeBytes"] = total_size_bytes
        if total_size_kb is not UNSET:
            field_dict["totalSizeKB"] = total_size_kb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_files = d.pop("totalFiles", UNSET)

        mdx_pages = d.pop("mdxPages", UNSET)

        config_files = d.pop("configFiles", UNSET)

        other_files = d.pop("otherFiles", UNSET)

        total_size_bytes = d.pop("totalSizeBytes", UNSET)

        total_size_kb = d.pop("totalSizeKB", UNSET)

        project_stats_stats = cls(
            total_files=total_files,
            mdx_pages=mdx_pages,
            config_files=config_files,
            other_files=other_files,
            total_size_bytes=total_size_bytes,
            total_size_kb=total_size_kb,
        )

        project_stats_stats.additional_properties = d
        return project_stats_stats

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
