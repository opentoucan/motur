#!/bin/sh

uv tool run openapi-python-client generate --url https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/v1.2.0-vehicle-enquiry-service.json --output-path ./src/generated/ves_client --meta none
uv tool run openapi-python-client generate --url https://documentation.history.mot.api.gov.uk/mot-history-api/api-specification/mot_history_open_api_specification.yml --output-path ./src/generated/mot_client --meta none
