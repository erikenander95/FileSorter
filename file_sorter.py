import os

# Get the user's home directory
user_home = os.path.expanduser("~")

# Define the path to the 'Downloads' folder
downloads_folder = os.path.join(user_home, "Downloads")

# Define the subfolders we want to organize files into
folders = ['zips', 'jpgs', 'others']

# Create subfolders if they don't exist
for folder in folders:
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Iterate through files in the 'Downloads' folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # Check if the item is a file
    if os.path.isfile(file_path):
        # Get the file extension
        file_extension = filename.split('.')[-1].lower()

        # Determine the destination folder based on the file extension
        if file_extension == 'zip':
            destination_folder = os.path.join(downloads_folder, 'zips')
        elif file_extension == 'jpg':
            destination_folder = os.path.join(downloads_folder, 'jpgs')
        else:
            destination_folder = os.path.join(downloads_folder, 'others')

        # Construct the destination path for the file
        destination_path = os.path.join(destination_folder, filename)

        # Move the file to its new location
        os.rename(file_path, destination_path)
