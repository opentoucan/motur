import msal
import requests
import settings

settings = settings.Settings()

def fetch_history(reg: str):
    client_id = settings.client_id
    tenant_id = settings.tenant_id
    client_secret = settings.client_secret
    api_key = settings.api_key

    client = msal.ConfidentialClientApplication(client_id, authority=f"https://login.microsoftonline.com/{tenant_id}", client_credential=client_secret)
    result = client.acquire_token_for_client(scopes=["https://tapi.dvsa.gov.uk/.default"])
    headers = {'accept': 'application/json','Authorization': f'{result['token_type']} {result['access_token']}','X-API-Key': f'{api_key}'}
    mot_response = requests.get(f'https://history.mot.api.gov.uk/v1/trade/vehicles/registration/{reg}', headers=headers)
    return mot_response.json()
