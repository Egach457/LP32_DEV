from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
from werkzeug.utils import secure_filename
import mimetypes

from webapp.lib.config import SERVICE_ACCOUNT_FILE, PARENT_FOLDER_ID

SCOPES = ["https://www.googleapis.com/auth/drive"]


def authenticate():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
    )
    return creds


def upload_photo(file_path):
    creds = authenticate()
    service = build("drive", "v3", credentials=creds)

    filename = secure_filename(file_path)
    file_metadata = {"name": filename, "parents": [PARENT_FOLDER_ID]}
    mime_type, _ = mimetypes.guess_type(filename)
    media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
    file = (
        service.files()
        .create(
            body=file_metadata,
            media_body=media,
            fields="id",
        )
        .execute()
    )
    print(f"Uploaded file metadata: {file}")

    return file["id"]


# file = upload_photo("collage.jpg")
# print(file)

# upload_photo("collage.jpg")
