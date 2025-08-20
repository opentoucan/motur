from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.vehicle import Vehicle
from ...models.vehicle_request import VehicleRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: VehicleRequest,
    x_api_key: str,
    x_correlation_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-key"] = x_api_key

    if not isinstance(x_correlation_id, Unset):
        headers["X-Correlation-Id"] = x_correlation_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/vehicles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, Vehicle]]:
    if response.status_code == 200:
        response_200 = Vehicle.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, Vehicle]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: VehicleRequest,
    x_api_key: str,
    x_correlation_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, Vehicle]]:
    """Get vehicle details by registration number

     Returns vehicle details based on registration number

    Args:
        x_api_key (str):
        x_correlation_id (Union[Unset, str]):
        body (VehicleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Vehicle]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_key=x_api_key,
        x_correlation_id=x_correlation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: VehicleRequest,
    x_api_key: str,
    x_correlation_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, Vehicle]]:
    """Get vehicle details by registration number

     Returns vehicle details based on registration number

    Args:
        x_api_key (str):
        x_correlation_id (Union[Unset, str]):
        body (VehicleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Vehicle]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_key=x_api_key,
        x_correlation_id=x_correlation_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: VehicleRequest,
    x_api_key: str,
    x_correlation_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, Vehicle]]:
    """Get vehicle details by registration number

     Returns vehicle details based on registration number

    Args:
        x_api_key (str):
        x_correlation_id (Union[Unset, str]):
        body (VehicleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Vehicle]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_key=x_api_key,
        x_correlation_id=x_correlation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: VehicleRequest,
    x_api_key: str,
    x_correlation_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, Vehicle]]:
    """Get vehicle details by registration number

     Returns vehicle details based on registration number

    Args:
        x_api_key (str):
        x_correlation_id (Union[Unset, str]):
        body (VehicleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Vehicle]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_key=x_api_key,
            x_correlation_id=x_correlation_id,
        )
    ).parsed
