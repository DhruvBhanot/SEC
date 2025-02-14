import os
import webbrowser
import  msal 
from dotenv import load_dotenv

MS_GRAPH_BASE_URL = 'https://graph.microsoft.com/v1.0'

def get_access_token(app_id,client_secret,scopes):
    client = msal.ConfidentialClientApplication(
        client_id = app_id,
        client_credential= client_secret,
        authority= 'https://login.microsoftonline.com/consumers'
    )

    refresh_token = None
    if os.path.exists('refresh_token.txt'):
        with open('refresh_token.txt','r') as file:
            refresh_token = file.read().strip()
    
    if refresh_token:
        token_response = client.acquire_token_by_refresh_token(refresh_token, scopes= scopes)
    else:
        auth_request_url = client.get_authorization_request_url(scopes)
        webbrowser.open(auth_request_url)
        authorization_code = input("enter authorization code: ")


        if not authorization_code:
            raise ValueError("Aithorization code is empty")

        token_response = client.acquire_token_by_authorization_code(
            code= authorization_code,
            scopes=scopes
        )

    if 'access_token' in token_response:

        if 'refresh_token' in token_response:
            with open('refresh_token.txt','w') as file:
                file.write(token_response['refresh_token'])

        return token_response['access_token']

    else:
        raise Exception('Failed to acquire access token ' + str(token_response))


