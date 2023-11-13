import os

user_home = os.path.expanduser("~")
downloads_folder = os.path.join(user_home, "Downloads")
folders = ['zips', 'jpgs', 'exe', 'mp4', 'pdf', 'others']

for folder in folders:
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    if os.path.isfile(file_path):
        file_extension = filename.split('.')[-1].lower()

        if file_extension == 'zip':
            destination_folder = os.path.join(downloads_folder, 'zips')
        elif file_extension == 'jpg':
            destination_folder = os.path.join(downloads_folder, 'jpgs')
        elif file_extension == 'exe':
            destination_folder = os.path.join(downloads_folder, 'exe')
        elif file_extension == 'mp4':
            destination_folder = os.path.join(downloads_folder, 'mp4')
        elif file_extension == 'pdf':
            destination_folder = os.path.join(downloads_folder, 'pdf')
        else:
            destination_folder = os.path.join(downloads_folder, 'others')

        destination_path = os.path.join(destination_folder, filename)
        os.rename(file_path, destination_path)
