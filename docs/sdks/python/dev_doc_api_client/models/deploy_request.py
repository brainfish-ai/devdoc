from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deploy_request_docs_json import DeployRequestDocsJson
    from ..models.deploy_request_files_item import DeployRequestFilesItem


T = TypeVar("T", bound="DeployRequest")


@_attrs_define
class DeployRequest:
    """
    Attributes:
        name (str): Project name from docs.json Example: My Documentation.
        docs_json (DeployRequestDocsJson): The docs.json configuration object
        files (list[DeployRequestFilesItem]): Content files to deploy
        slug (str | Unset): Existing project slug (for updates) Example: my-docs-abc123.
    """

    name: str
    docs_json: DeployRequestDocsJson
    files: list[DeployRequestFilesItem]
    slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        docs_json = self.docs_json.to_dict()

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "docsJson": docs_json,
                "files": files,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deploy_request_docs_json import DeployRequestDocsJson
        from ..models.deploy_request_files_item import DeployRequestFilesItem

        d = dict(src_dict)
        name = d.pop("name")

        docs_json = DeployRequestDocsJson.from_dict(d.pop("docsJson"))

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = DeployRequestFilesItem.from_dict(files_item_data)

            files.append(files_item)

        slug = d.pop("slug", UNSET)

        deploy_request = cls(
            name=name,
            docs_json=docs_json,
            files=files,
            slug=slug,
        )

        deploy_request.additional_properties = d
        return deploy_request

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
