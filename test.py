from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
import io
import pickle
import os

scopes = ['https://www.googleapis.com/auth/drive']
credsFile = "credentials.json"
tokenPickleFile = "token.pickle"

def getAuthenticatedService():
    creds = None
    if os.path.exists(tokenPickleFile):
        with open(tokenPickleFile,"rb") as tokenFile:
            creds = pickle.load(tokenFile)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credsFile,scopes)
            creds = flow.run_local_server(port=0)
        with open(tokenPickleFile,"wb") as token:
            pickle.dump(creds,token)
    return build("drive","v3",credentials=creds)
def updateFile(fileID,newContent):
    service = getAuthenticatedService()
    mediaBody = MediaIoBaseUpload(io.BytesIO(newContent.encode()), mimetype='text/plain', resumable=True)
    updatedFile = service.files().update(fileId=fileID, media_body=mediaBody).execute()
    return updatedFile

def appendToFile(fileID,additionalContent):
    service = getAuthenticatedService()
    fileMetadata = service.files().get(fileId=fileID,fields='mimeType').execute()
    mimeType = fileMetadata.get('mimeType','')
    if mimeType.startswith('application/vnd.google-apps'):
        request = service.files().export_media(fileId=fileID,mimeType="text/plain")
        exportedContent = request.execute()
        exportedContentString = exportedContent.decode('utf-8')
        print(exportedContentString)
        newContent = exportedContentString + '\n' + additionalContent
        newContentIO = io.BytesIO(newContent.encode())
        mediaBody = MediaIoBaseUpload(newContentIO,mimetype ='text/plain',resumable=True)
        updatedFile = service.files().update(fileId=fileID,media_body=mediaBody).execute()
    return updatedFile
        
    
    currentContent = service.files().get_media(fileId = fileID).execute()
    print(currentContent,type(currentContent))
    return True
    

fileID = "1iptEZfA0p6ZZThUrPaOS4O44f7umeWwdvUG4Jjc_kSw"
newContent ="Hello Testing4"
print(appendToFile(fileID,additionalContent = newContent))
#updatedFile = updateFile(fileID,newContent)
#print('File updated : ',updatedFile)
    