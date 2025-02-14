import os
from pathlib import Path
import httpx
from dotenv import load_dotenv
from ms_graph import get_access_token, MS_GRAPH_BASE_URL
from outlook import create_attachment

# place holder for when I want to move this to the actual main coding doc



# place holder ends

# still can still be abstracted
def draft_message_body(subject: str,attachment, email: str):
    message = {
        'subject': subject,
        'body': {
            'contentType': 'HTML',
            'content': 'See attached.' 
             },
        'toRecipients': [
            {
                'emailAddress': {
                    'address': email
                }
            }
        ],
        'importance': 'high',
        'attachments': attachment
    }
    return message




def send_mail(path: str, email: str,subject):

    load_dotenv()
    APPLICATION_ID = os.getenv('APPLICATION_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    SCOPES = ['User.Read', 'Mail.ReadWrite']


    try:
        access_token = get_access_token(
            app_id = APPLICATION_ID,
            client_secret= CLIENT_SECRET,
            scopes= SCOPES
        )
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        dir_attachments = Path(path)

        attachments = [create_attachment(attachment) for attachment in dir_attachments.iterdir() if attachment.is_file()]

        endpoint = f'{MS_GRAPH_BASE_URL}/me/sendMail'

        message = {
            'message': draft_message_body('Test Email with Attachments_',attachments,email)
        }

        response = httpx.post(endpoint,headers=headers,json=message)
        if response.status_code != 202:
            raise Exception(f'Failed to send email: {response.text}')
        print('Email sent')

    except httpx.HTTPStatusError as e:
        print(f'HTTP Error:{e}')
    except Exception as e:
        print(f'Error: {e}')





