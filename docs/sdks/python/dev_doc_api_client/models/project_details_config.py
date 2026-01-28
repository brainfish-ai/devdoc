from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectDetailsConfig")


@_attrs_define
class ProjectDetailsConfig:
    """
    Attributes:
        name (str | Unset):
        favicon (str | Unset):
        navigation (str | Unset):
    """

    name: str | Unset = UNSET
    favicon: str | Unset = UNSET
    navigation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        favicon = self.favicon

        navigation = self.navigation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if favicon is not UNSET:
            field_dict["favicon"] = favicon
        if navigation is not UNSET:
            field_dict["navigation"] = navigation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        favicon = d.pop("favicon", UNSET)

        navigation = d.pop("navigation", UNSET)

        project_details_config = cls(
            name=name,
            favicon=favicon,
            navigation=navigation,
        )

        project_details_config.additional_properties = d
        return project_details_config

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
