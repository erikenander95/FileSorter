import os

downloads_folder = "C:/Users/erike/Downloads"

folders = ['zips', 'jpgs', 'others']
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
        else:
            destination_folder = os.path.join(downloads_folder, 'others')

        destination_path = os.path.join(destination_folder, filename)

        os.rename(file_path, destination_path)