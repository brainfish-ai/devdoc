from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_deploy_status_response_200 import GetDeployStatusResponse200
from ...models.get_deploy_status_response_404 import GetDeployStatusResponse404
from ...types import UNSET, Response


def _get_kwargs(
    *,
    slug: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["slug"] = slug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/deploy",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDeployStatusResponse200 | GetDeployStatusResponse404 | None:
    if response.status_code == 200:
        response_200 = GetDeployStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetDeployStatusResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetDeployStatusResponse200 | GetDeployStatusResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    slug: str,
) -> Response[GetDeployStatusResponse200 | GetDeployStatusResponse404]:
    """Check Deployment Status

     Check if a project exists and get its URL

    Args:
        slug (str):  Example: my-docs-abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDeployStatusResponse200 | GetDeployStatusResponse404]
    """

    kwargs = _get_kwargs(
        slug=slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    slug: str,
) -> GetDeployStatusResponse200 | GetDeployStatusResponse404 | None:
    """Check Deployment Status

     Check if a project exists and get its URL

    Args:
        slug (str):  Example: my-docs-abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDeployStatusResponse200 | GetDeployStatusResponse404
    """

    return sync_detailed(
        client=client,
        slug=slug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    slug: str,
) -> Response[GetDeployStatusResponse200 | GetDeployStatusResponse404]:
    """Check Deployment Status

     Check if a project exists and get its URL

    Args:
        slug (str):  Example: my-docs-abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDeployStatusResponse200 | GetDeployStatusResponse404]
    """

    kwargs = _get_kwargs(
        slug=slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    slug: str,
) -> GetDeployStatusResponse200 | GetDeployStatusResponse404 | None:
    """Check Deployment Status

     Check if a project exists and get its URL

    Args:
        slug (str):  Example: my-docs-abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDeployStatusResponse200 | GetDeployStatusResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            slug=slug,
        )
    ).parsed
