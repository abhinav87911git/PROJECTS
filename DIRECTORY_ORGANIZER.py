

import os
import shutil

def organize_directory(path):
    file_types = {
        'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mov', '.mkv', '.avi']
    }

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            for folder, extentions in file_types.items():
                if file.lower().endswith(tuple(extentions)):
                    folder_path = os.path.join(path, folder)
                    os.makedirs(folder_path, exist_ok= True)
                    shutil.move(file_path, folder_path)
                    break

if __name__ == "__main__":
    directory = input( 'Enter the path of the directory to organize: ')
    organize_directory(directory)               