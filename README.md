# FileSorter
A python script for automatically sorting files in your downloads folder into folders based on their file types.

## Sorting Files in Downloads Folder Documentation

### Overview

This program is designed to organize files in your Downloads folder by moving them into separate folders based on their file extensions. It categorizes files into three main groups: 'zips,' 'jpgs,' and 'others.'

### Code Explanation

Here's a breakdown of the provided code:

1. Importing the necessary module:
   ```python
   import os
   ```

2. Setting up the paths:
   - `user_home`: Obtains the user's home directory.
   - `downloads_folder`: Forms the path to the 'Downloads' folder.
   ```python
   user_home = os.path.expanduser("~")
   downloads_folder = os.path.join(user_home, "Downloads")
   ```

3. Creating folders if they don't exist:
   - The `folders` list contains the names of the folders you want to create.
   - A loop iterates over each folder name, checks if the folder already exists, and creates it if it doesn't.
   ```python
   folders = ['zips', 'jpgs', 'exe', 'mp4', 'pdf', 'others']
   for folder in folders:
       folder_path = os.path.join(downloads_folder, folder)
       if not os.path.exists(folder_path):
           os.makedirs(folder_path)
   ```

4. Sorting files:
   - Another loop iterates over each file in the 'Downloads' folder.
   - For each file, it extracts the file extension and converts it to lowercase.
   - Based on the file extension, it determines the destination folder.
   - Finally, it renames the file and moves it to the appropriate destination folder.
   ```python
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
   ```

### Example

Let's illustrate how this program works with an example:

Suppose you have the following files in your 'Downloads' folder:
- `document.pdf`
- `image.jpg`
- `archive.zip`
- `music.mp4`
- `data.csv`

After running the program, your 'Downloads' folder will look like this:

```
Downloads/
│
├── zips/
│   └── archive.zip
│
├── jpgs/
│   └── image.jpg
│
├── mp4/
│   └── music.mp4
│
├── pdf/
│   └── document.pdf
│
├── others/
    └── data.csv
```

This code efficiently categorizes files into separate folders based on their extensions, making it easier to manage and find specific types of files.
