import msal
import requests
from config import mot_settings

def fetch_history(reg: str):
    client_id = mot_settings.mot_client_id
    tenant_id = mot_settings.mot_tenant_id
    client_secret = mot_settings.mot_client_secret
    api_key = mot_settings.mot_api_key

    client = msal.ConfidentialClientApplication(client_id, authority=f"https://login.microsoftonline.com/{tenant_id}", client_credential=client_secret)
    result = client.acquire_token_for_client(scopes=["https://tapi.dvsa.gov.uk/.default"])
    if type(result) is not dict:
        return
    headers = {'accept': 'application/json','Authorization': f'{result['token_type']} {result['access_token']}','X-API-Key': f'{api_key}'}
    mot_response = requests.get(f'https://history.mot.api.gov.uk/v1/trade/vehicles/registration/{reg}', headers=headers)
    return mot_response.json()
