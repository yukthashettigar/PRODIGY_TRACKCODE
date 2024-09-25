from PIL import Image

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = pixels[x, y]
            encrypted_pixel = tuple([val ^ key for val in pixel])
            pixels[x, y] = encrypted_pixel

    image.save(output_path)

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = pixels[x, y]
            decrypted_pixel = tuple([val ^ key for val in pixel])
            pixels[x, y] = decrypted_pixel

    image.save(output_path)

def main():
    while True:
        print("\nImage Encryption Tool")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            image_path = input("Enter the image path: ")
            output_path = input("Enter the output path: ")
            key = int(input("Enter the encryption key: "))
            encrypt_image(image_path, output_path, key)
        elif choice == "2":
            image_path = input("Enter the encrypted image path: ")
            output_path = input("Enter the output path: ")
            key = int(input("Enter the decryption key: "))
            decrypt_image(image_path, output_path, key)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
