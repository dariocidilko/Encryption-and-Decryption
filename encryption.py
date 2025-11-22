from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

if os.path.exists("AES.key"): # If the AES key file exists, load it.
    with open("AES.key", "rb") as file:
        Key = file.read()
    print(f"The AES-256 key was loaded successfully. \n")
else: # If there is no AES key file, generate a new key and save it.
    Key = AESGCM.generate_key(bit_length=256) # Generate a new AES-256 key.
    
    with open("AES.key", "wb") as file:
        file.write(Key)

    # These are print statements to inform the user about the key generation and the saving process.
    print("A new AES-256 key was generated and saved as 'AES.key'")
    print("Do not lose this key, as it is required for decryption.")    

aesgcm = AESGCM(Key) # Create an AES-GCM cipher instance.

# This is a function to encrypt a single file inside of a folder.
def encrypt_file(Path):

    # Read the file input.
    with open(Path, "rb") as file:
        Data = file.read()

    # GCM requires a 96-bit (12-byte) nonce.
    Nonce = os.urandom(12)
    Encrypted = aesgcm.encrypt(Nonce, Data, None)

    # Overwrite the original file (This will replace the original file with the encrypted version).
    with open(Path, "wb") as file:
        file.write(Nonce + Encrypted)

    print(f"File encrypted: {Path}")

# This is a function to encrypt all files inside of a provided folder.
def encrypt_folder(folder_path):

    # Walk through all files in the folder and its subfolders.
    for root_dir, sub_dir, files in os.walk(folder_path):

        # Encrypt each file found.
        for filename in files:
            file_path = os.path.join(root_dir, filename)
            encrypt_file(file_path) # Call the encrypt_file function for each file.

# Get the folder path to encrypt from the user.
folder_path = input("Enter the full path of the folder to encrypt: ")
encrypt_folder(folder_path)
