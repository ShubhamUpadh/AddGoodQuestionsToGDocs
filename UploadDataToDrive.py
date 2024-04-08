from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
import io
import pickle
import os
import time

scopes = ['https://www.googleapis.com/auth/drive']
credsFile = "credFile.json"
tokenPickleFile = "token.pickle"

class uploadData:
    def __init__(self):
        self.newCodes, self.fileID = None, None
        with open('output.txt','r') as file:
            self.newCodes = file.read()
        with open('fileName.txt','r') as file:
            self.fileID = file.read()
        
    def getAuthenticatedService(self):
        creds = None
        if os.path.exists(tokenPickleFile):
            with open(tokenPickleFile,"rb") as tokenFile:
                creds = pickle.load(tokenFile)
        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(credsFile,scopes)
            creds = flow.run_local_server(port=0)
            with open(tokenPickleFile,"wb") as token:
                pickle.dump(creds,token)
        return build("drive","v3",credentials=creds)
    
    def updateFile(self,fileID,newContent):
        service = self.getAuthenticatedService()
        mediaBody = MediaIoBaseUpload(io.BytesIO(newContent.encode()), mimetype='text/plain', resumable=True)
        updatedFile = service.files().update(fileId=fileID, media_body=mediaBody).execute()
        return updatedFile

    def appendToFile(self,fileID,additionalContent):
        service = self.getAuthenticatedService()
        fileMetadata = service.files().get(fileId=fileID,fields='mimeType').execute()
        mimeType = fileMetadata.get('mimeType','')
        if mimeType.startswith('application/vnd.google-apps'):
            request = service.files().export_media(fileId=fileID,mimeType="text/plain")
            exportedContent = request.execute()
            exportedContentString = exportedContent.decode('utf-8')
            #print(exportedContentString)
            newContent = exportedContentString + '\n' + additionalContent
            newContentIO = io.BytesIO(newContent.encode())
            mediaBody = MediaIoBaseUpload(newContentIO,mimetype ='text/plain',resumable=True)
            updatedFile = service.files().update(fileId=fileID,media_body=mediaBody).execute()
        return updatedFile
    
    def execute(self):
        self.appendToFile(self.fileID,additionalContent=self.newCodes)
if __name__ == '__main__':
    obj = uploadData()
    obj.execute()

'''       
startTime = time.time()  
with open('fileName.txt','r') as file:
    fileID = file.read()
#print(fileID,type(fileID))
#fileID = "1iptEZfA0p6ZZThUrPaOS4O44f7umeWwdvUG4Jjc_kSw"

newCodes = None
with open('output.txt','r') as file:
    newCodes = file.read()
#print(newCodes, type(newCodes))
up = uploadData()
print(up.appendToFile(fileID,additionalContent = newCodes))
print(f"Time taken is {time.time()-startTime}")
#updatedFile = updateFile(fileID,newContent)
#print('File updated : ',updatedFile)
'''
