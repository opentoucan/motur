from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.new_reg_vehicle_response import NewRegVehicleResponse
from ...models.vehicle_with_mot_response import VehicleWithMotResponse
from ...types import Response


def _get_kwargs(
    vin: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/trade/vehicles/vin/{vin}".format(
            vin=vin,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[ErrorResponse, Union["NewRegVehicleResponse", "VehicleWithMotResponse"]]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["NewRegVehicleResponse", "VehicleWithMotResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = VehicleWithMotResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = NewRegVehicleResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[ErrorResponse, Union["NewRegVehicleResponse", "VehicleWithMotResponse"]]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vin: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[ErrorResponse, Union["NewRegVehicleResponse", "VehicleWithMotResponse"]]
]:
    """Get MOT Tests for a single vehicle by vehicle identification number

     ```
    GET /v1/trade/vehicles/vin/
    ```

    Args:
        vin (str): - Vehicle Identification Number, where it was used in the request. Usually 17
            alphanumeric characters. Example: 1N4G7TCF1A9895216.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['NewRegVehicleResponse', 'VehicleWithMotResponse']]]
    """

    kwargs = _get_kwargs(
        vin=vin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vin: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[ErrorResponse, Union["NewRegVehicleResponse", "VehicleWithMotResponse"]]
]:
    """Get MOT Tests for a single vehicle by vehicle identification number

     ```
    GET /v1/trade/vehicles/vin/
    ```

    Args:
        vin (str): - Vehicle Identification Number, where it was used in the request. Usually 17
            alphanumeric characters. Example: 1N4G7TCF1A9895216.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['NewRegVehicleResponse', 'VehicleWithMotResponse']]
    """

    return sync_detailed(
        vin=vin,
        client=client,
    ).parsed


async def asyncio_detailed(
    vin: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[ErrorResponse, Union["NewRegVehicleResponse", "VehicleWithMotResponse"]]
]:
    """Get MOT Tests for a single vehicle by vehicle identification number

     ```
    GET /v1/trade/vehicles/vin/
    ```

    Args:
        vin (str): - Vehicle Identification Number, where it was used in the request. Usually 17
            alphanumeric characters. Example: 1N4G7TCF1A9895216.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['NewRegVehicleResponse', 'VehicleWithMotResponse']]]
    """

    kwargs = _get_kwargs(
        vin=vin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vin: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[ErrorResponse, Union["NewRegVehicleResponse", "VehicleWithMotResponse"]]
]:
    """Get MOT Tests for a single vehicle by vehicle identification number

     ```
    GET /v1/trade/vehicles/vin/
    ```

    Args:
        vin (str): - Vehicle Identification Number, where it was used in the request. Usually 17
            alphanumeric characters. Example: 1N4G7TCF1A9895216.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['NewRegVehicleResponse', 'VehicleWithMotResponse']]
    """

    return (
        await asyncio_detailed(
            vin=vin,
            client=client,
        )
    ).parsed
