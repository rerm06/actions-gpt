from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import gspread
import io
from flask import current_app as app

class GoogleService:
    def __init__(self):
        self.creds = Credentials.from_service_account_file(
            app.config['GOOGLE_SHEETS_CREDENTIALS_FILE'],
            scopes=app.config['GOOGLE_SHEETS_SCOPE']
        )
        self.client = gspread.authorize(self.creds)
        self.drive_service = build('drive', 'v3', credentials=self.creds)

    def update_sheet(self, sheet_name, values):
        sheet = self.client.open(sheet_name).sheet1
        sheet.append_row(values)
        return True

    def create_file_in_drive(self, name, content, mime_type='text/plain'):
        file_metadata = {'name': name, 'mimeType': mime_type}
        media = MediaIoBaseUpload(io.StringIO(content), mimetype=mime_type)
        file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    def list_files_in_drive(self, query=""):
        results = self.drive_service.files().list(
            q=query,
            pageSize=10,
            fields="nextPageToken, files(id, name, mimeType)").execute()
        items = results.get('files', [])
        return items

    def search_files(self, name=None, mime_type=None):
        query = ""
        if name:
            query += f"name contains '{name}'"
        if mime_type:
            if query: query += " and "
            query += f"mimeType = '{mime_type}'"
        return self.list_files_in_drive(query)
