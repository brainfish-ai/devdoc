from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_stats_analytics import ProjectStatsAnalytics
    from ..models.project_stats_deployment import ProjectStatsDeployment
    from ..models.project_stats_stats import ProjectStatsStats


T = TypeVar("T", bound="ProjectStats")


@_attrs_define
class ProjectStats:
    """
    Attributes:
        slug (str | Unset):
        stats (ProjectStatsStats | Unset):
        deployment (ProjectStatsDeployment | Unset):
        analytics (ProjectStatsAnalytics | Unset):
    """

    slug: str | Unset = UNSET
    stats: ProjectStatsStats | Unset = UNSET
    deployment: ProjectStatsDeployment | Unset = UNSET
    analytics: ProjectStatsAnalytics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        deployment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deployment, Unset):
            deployment = self.deployment.to_dict()

        analytics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analytics, Unset):
            analytics = self.analytics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if stats is not UNSET:
            field_dict["stats"] = stats
        if deployment is not UNSET:
            field_dict["deployment"] = deployment
        if analytics is not UNSET:
            field_dict["analytics"] = analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_stats_analytics import ProjectStatsAnalytics
        from ..models.project_stats_deployment import ProjectStatsDeployment
        from ..models.project_stats_stats import ProjectStatsStats

        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: ProjectStatsStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = ProjectStatsStats.from_dict(_stats)

        _deployment = d.pop("deployment", UNSET)
        deployment: ProjectStatsDeployment | Unset
        if isinstance(_deployment, Unset):
            deployment = UNSET
        else:
            deployment = ProjectStatsDeployment.from_dict(_deployment)

        _analytics = d.pop("analytics", UNSET)
        analytics: ProjectStatsAnalytics | Unset
        if isinstance(_analytics, Unset):
            analytics = UNSET
        else:
            analytics = ProjectStatsAnalytics.from_dict(_analytics)

        project_stats = cls(
            slug=slug,
            stats=stats,
            deployment=deployment,
            analytics=analytics,
        )

        project_stats.additional_properties = d
        return project_stats

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
