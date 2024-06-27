
#  qr code generator from texts or url

import qrcode
from PIL import Image
import qrcode.constants

def generate_qr_code(data, save_path):
    qr = qrcode.QRCode(version =1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size =10, border =4)
    
    qr.add_data(data)
    qr.make(fit = True)

    img = qr.make_image(fill= 'black', back_color= 'white')

    if not save_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        save_path += ".png"

    img.save(save_path)
    print(f'QR Code successfully generated and saved to {save_path}')

if __name__=="__main__":
    data = input('Enter the text or url to generate qr code for: ')
    save_path = input("Enter the path for saving the qr code : ")
    generate_qr_code(data, save_path)

    
        