from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']




def downloadFolder(service, fileId, destinationFolder):
    if not os.path.isdir(destinationFolder):
        os.mkdir(path=destinationFolder)

    results = service.files().list(
        pageSize=300,
        q="parents in '{0}'".format(fileId),
        fields="files(id, name, mimeType)"
        ).execute()

    items = results.get('files', [])

    for item in items:
        itemName = item['name']
        itemId = item['id']
        itemType = item['mimeType']
        filePath = destinationFolder + "/" + itemName

        if itemType == 'application/vnd.google-apps.folder':
            print "Stepping into folder: %s" %format(filePath)
            downloadFolder(service, itemId, filePath) # Recursive call
        elif not itemType.startswith('application/'):
            downloadFile(service, itemId, filePath)
        else:
            print "Unsupported file: %s"%format(itemName)


if __name__ == "__main__":
    """Based on the quickStart.py example at
    https://developers.google.com/drive/api/v3/quickstart/python
    """
    creds = getCredentials()
    service = build('drive', 'v3', credentials=creds)
    
    folderId = sys.argv[1]
    destinationFolder = sys.argv[2]
    downloadFolder(service, folderId, destinationFolder)