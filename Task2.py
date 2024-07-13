# Encrypting Image
from PIL import Image

def encrypt_image(path, key):
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()

def decrypt_image(path, key):
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    
# Usage
path = input('Enter path of Image: ')
key = int(input('Enter Key for encryption of Image: '))
print('The path of file : ', path)
print('Note : Encryption key and Decryption key must be same.')
print('Key for Decryption : ', key)

encrypt_image(path, key)
print('Encryption Done...')

decrypt_image(path, key)
print('Decryption Done...')