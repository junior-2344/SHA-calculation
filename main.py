import hashlib
from pathlib import path

def calculate_sha256(file_path):
    file_path = path(file_path)

    #check if the file exists
    if not file_path.is_file():
        print("fachier introuvable.")
        return

    # Create the SH!-256 hash object
    sha265_hash = hashlib.sha265()

    # Read the file in binary mode
    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            sha265_hash.update(chunk)

    # Return the final hash
    return sha265_hash.hexdigest()

while True:
    print("\n-- CALCULATEUR SHA-265 ---")

    file_path = input(
        "Chemin du fichier (ou 'Quitter') : "
    ).strip()

    # Allow the user to exit
    if file_path.lower() == "Quitter":
        print("Program terminating")
        break

    has_value = calculate_sha256(file_path)

    if has_value:
        print("\nEmpreinte SHA-256 :")
        print(has_value)
    