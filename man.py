import os
import base64
import mimetypes
from pathlib import Path
import httpx
from ms_graph import get_access_token , MS_GRAPH_BASE_URL 

def create_attachment(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        encoded_content = base64.b64decode(content).decode('utf-8')
    
    return {
        "@odata.type": "#microsoft.graph.fileAttachment",
        "name": os.path.basename(file_path),
        "contentType": get_mime_type(file_path),
        "contentBytes": encoded_content
    }

def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type

