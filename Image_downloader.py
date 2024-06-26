
import requests
from PIL import Image
from io import BytesIO
import os

def download_image(url , save_path):
    response = requests.get(url)
    if response.status_code ==200:
        img = Image.open(BytesIO(response.content))

        if not save_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            save_path = os.path.join(save_path, "downloaded_image.jpg")

            img.save(save_path)
            print(f'Image is saved successfully at {save_path}')
            return img
    else:
        print(f'image is not downloaded , response status is :{response.status_code}')


def resize_image(img, width, height, save_path):
    resized_img = img.resize((width, height))

    if not save_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        save_path = os.path.join(save_path, "resized_image.jpg") 
    resized_img.save(save_path)
    print(f'image is successfully resized and saved at {save_path}')


if __name__ == "__main__":
    url = input('Enter the url : ')
    save_path = input('Enter the save path : ')
    img = download_image(url, save_path)

    if img:
        width = int(input('Enter the width : '))    
        height = int(input('Enter the height : '))
        resized_save_path = input('Enter the resized save path')
        resize_image(img, width, height, resized_save_path)
