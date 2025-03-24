import os
import pickle
import logging
import shutil
import time  # Import the time module
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import subprocess

# Define Google Drive API scopes
SCOPES = ["https://www.googleapis.com/auth/drive"]

# Logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Tracking files
METADATA_UPDATED_FILE = "metadata_updated.txt"
UPLOADED_FILES_FILE = "uploaded_files.txt"

# Runtime limit in seconds (5 hours = 5 * 60 * 60, 40 minutes = 40 * 60)
RUNTIME_LIMIT = 18000 # 5 hours and 40 minutes

def authenticate_google_drive():
    """Authenticate and get credentials for Google Drive API."""
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("drive", "v3", credentials=creds)

def load_tracking_file(filename):
    """Load tracking data from a file."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return set(f.read().splitlines())
    return set()

def save_tracking_file(filename, data):
    """Save tracking data to a file."""
    with open(filename, "w") as f:
        f.writelines("\n".join(data))

def append_to_tracking_file(filename, line):
    """Append a single line to a tracking file."""
    with open(filename, "a") as f:
        f.write(line + "\n")

def clear_folder(folder_path):
    """Delete all files in a specified folder."""
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)

def delete_folders(*folder_paths):
    """Delete specified folders and their contents."""
    for folder_path in folder_paths:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Deleted folder: {folder_path}")

def download_and_encode_file(service, file, download_path, metaupdate_path):
    """Download file, encode it, update metadata, and return the path to the encoded file."""
    file_id = file['id']
    file_name = file['name']
    download_file_path = os.path.join(download_path, file_name)
    encoded_file_path = os.path.join(metaupdate_path, file_name)

    # Download file
    request = service.files().get_media(fileId=file_id)
    with open(download_file_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
    print(f"Downloaded: {file_name}")

    # Encode file and update metadata
    file_title = os.path.splitext(file_name)[0]
    try:
        subprocess.run([
            "ffmpeg", "-i", download_file_path, "-map", "0", "-c", "copy",
               "-metadata", f"title={file_title}",
        # Audio metadata (s:a:0 to s:a:10)
        '-metadata:s:a:0', 'title=MovieHai',
        '-metadata:s:a:1', 'title=MovieHai',
        '-metadata:s:a:2', 'title=MovieHai',
        '-metadata:s:a:3', 'title=MovieHai',
        '-metadata:s:a:4', 'title=MovieHai',
        '-metadata:s:a:5', 'title=MovieHai',
        '-metadata:s:a:6', 'title=MovieHai',
        '-metadata:s:a:7', 'title=MovieHai',
        '-metadata:s:a:8', 'title=MovieHai',
        '-metadata:s:a:9', 'title=MovieHai',
        '-metadata:s:a:10', 'title=MovieHai',
        # Video metadata (s:v:0)
        '-metadata:s:v:0', 'title=MovieHai',
        # Subtitle metadata (s:s:0 to s:s:40)
        '-metadata:s:s:0', 'title=MovieHai',
        '-metadata:s:s:1', 'title=MovieHai',
        '-metadata:s:s:2', 'title=MovieHai',
        '-metadata:s:s:3', 'title=MovieHai',
        '-metadata:s:s:4', 'title=MovieHai',
        '-metadata:s:s:5', 'title=MovieHai',
        '-metadata:s:s:6', 'title=MovieHai',
        '-metadata:s:s:7', 'title=MovieHai',
        '-metadata:s:s:8', 'title=MovieHai',
        '-metadata:s:s:9', 'title=MovieHai',
        '-metadata:s:s:10', 'title=MovieHai',
        '-metadata:s:s:11', 'title=MovieHai',
        '-metadata:s:s:12', 'title=MovieHai',
        '-metadata:s:s:13', 'title=MovieHai',
        '-metadata:s:s:14', 'title=MovieHai',
        '-metadata:s:s:15', 'title=MovieHai',
        '-metadata:s:s:16', 'title=MovieHai',
        '-metadata:s:s:17', 'title=MovieHai',
        '-metadata:s:s:18', 'title=MovieHai',
        '-metadata:s:s:19', 'title=MovieHai',
        '-metadata:s:s:20', 'title=MovieHai',
        '-metadata:s:s:21', 'title=MovieHai',
        '-metadata:s:s:22', 'title=MovieHai',
        '-metadata:s:s:23', 'title=MovieHai',
        '-metadata:s:s:24', 'title=MovieHai',
        '-metadata:s:s:25', 'title=MovieHai',
        '-metadata:s:s:26', 'title=MovieHai',
        '-metadata:s:s:27', 'title=MovieHai',
        '-metadata:s:s:28', 'title=MovieHai',
        '-metadata:s:s:29', 'title=MovieHai',
        '-metadata:s:s:30', 'title=MovieHai',
        '-metadata:s:s:31', 'title=MovieHai',
        '-metadata:s:s:32', 'title=MovieHai',
        '-metadata:s:s:33', 'title=MovieHai',
        '-metadata:s:s:34', 'title=MovieHai',
        '-metadata:s:s:35', 'title=MovieHai',
        '-metadata:s:s:36', 'title=MovieHai',
        '-metadata:s:s:37', 'title=MovieHai',
        '-metadata:s:s:38', 'title=MovieHai',
        '-metadata:s:s:39', 'title=MovieHai',
        '-metadata:s:s:40', 'title=MovieHai',
            encoded_file_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # Suppress FFmpeg output
        print(f"Metadata updated: {file_name}")
        logging.info(f"Successfully processed {file_name}")
        os.remove(download_file_path)  # Remove original downloaded file after encoding
        return encoded_file_path
    except subprocess.CalledProcessError as e:
        logging.error(f"Error processing metadata for {file_name}: {e}")
        return None

def upload_file_to_drive(service, folder_id, file_path):
    """Upload a file to Google Drive."""
    file_name = os.path.basename(file_path)
    file_metadata = {"name": file_name, "parents": [folder_id]}
    try:
        media = MediaFileUpload(file_path, resumable=True)
        service.files().create(body=file_metadata, media_body=media, fields="id").execute()
        print(f"Uploaded: {file_name}")
        logging.info(f"Successfully uploaded {file_name}")
        append_to_tracking_file(UPLOADED_FILES_FILE, file_name)  # Append immediately after upload
        os.remove(file_path)  # Remove encoded file after upload
        return True
    except Exception as e:
        logging.error(f"Error uploading {file_name}: {e}")
        return False

def process_folder(service, folder_id, upload_folder_id, download_path, metaupdate_path, start_time):
    """Process all files in a Google Drive folder."""
    uploaded_files = load_tracking_file(UPLOADED_FILES_FILE)
    page_token = None
    all_files = []

    # Fetch all files and sort by name in ascending order
    while True:
        results = service.files().list(
            q=f"'{folder_id}' in parents",
            spaces='drive',
            fields="nextPageToken, files(id, name)",
            orderBy="name asc",
            pageToken=page_token
        ).execute()

        files = results.get('files', [])
        all_files.extend(files)
        page_token = results.get('nextPageToken', None)
        if page_token is None:
            break

    total_files = len(all_files)
    print(f"\nTotal files in folder: {total_files}")

    # Categorize files
    skipped_files = [file['name'] for file in all_files if file['name'] in uploaded_files]
    files_to_process = [file for file in all_files if file['name'] not in uploaded_files]

    # Display skipped files
    print(f"Skipped files ({len(skipped_files)}):")
    for file in skipped_files:
        print(f" - {file}")

    print(f"\nFiles to process ({len(files_to_process)}):")
    downloaded = 0
    for file in files_to_process:
        # Check if runtime limit has been exceeded
        elapsed_time = time.time() - start_time
        if elapsed_time >= RUNTIME_LIMIT:
            print(f"\nRuntime limit of {RUNTIME_LIMIT // 3600} hours and {(RUNTIME_LIMIT % 3600) // 60} minutes reached. Stopping script.")
            logging.info(f"Runtime limit reached. Stopping script.")
            return

        file_name = file['name']
        print(f"\nProcessing: {file_name} ({downloaded + 1}/{len(files_to_process)})")

        # Create necessary folders
        os.makedirs(download_path, exist_ok=True)
        os.makedirs(metaupdate_path, exist_ok=True)

        # Download, encode, and upload the file
        encoded_file_path = download_and_encode_file(service, file, download_path, metaupdate_path)
        if encoded_file_path:
            if upload_file_to_drive(service, upload_folder_id, encoded_file_path):
                uploaded_files.add(file_name)

        # Delete folders after processing the file
        delete_folders(download_path, metaupdate_path)

        downloaded += 1

    print("\nProcessing complete!")

def main():
    try:
        # Record the start time
        start_time = time.time()

        service = authenticate_google_drive()
        download_folder_ids = ["10yYGEmApb27ebo7-s1HRT0aH9PNYLJbn"]
        upload_folder_id = "1W18rqJL27QoAsfmd3LbkVNVAnpxAsqxM"
        download_path = "Download"
        metaupdate_path = "MetaUpdate"

        for folder_id in download_folder_ids:
            process_folder(service, folder_id, upload_folder_id, download_path, metaupdate_path, start_time)

    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()