from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

if os.path.exists("AES.key"): # If the AES key file exists, load it.
    with open("AES.key", "rb") as file:
        Key = file.read()
    aesgcm = AESGCM(Key)
    print(f"The AES-256 key was loaded successfully for decryption. \n")
else: # If there is no AES key file, inform the user and exit.
    print("There is no decryption key in this directory.")
    exit(1) # Exit the program with an error code.

# This is a function to decrypt a single file inside of a folder.
def decrypt_file(Path):
    with open(Path, "rb") as file:
        Data = file.read()

    Nonce = Data[:12] # The first 12 bytes are nonce.
    Ciphertext = Data[12:] # The rest is the ciphertext

    Decrypted = aesgcm.decrypt(Nonce, Ciphertext, None)

    # Write the decrypted data back to the file.
    with open(Path, "wb") as file:
        file.write(Decrypted)
    print(f"Decrypted: {Path}")

# This is a function to decrypt all files in a folder.
def decrypt_folder(folder_path):

    # Walk through all files in the folder and its subfolders.
    for root_dir, sub_dir, files in os.walk(folder_path):

        # Decrypt each file found.
        for filename in files:
            file_path = os.path.join(root_dir, filename)
            decrypt_file(file_path) # Call the decrypt_file function for each file.

# Get the folder path to decrypt from the user.
folder_path = input("Enter the full path of the folder to decrypt: ")
decrypt_folder(folder_path)
