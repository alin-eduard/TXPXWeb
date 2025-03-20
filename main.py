import os
import json

# Folderul unde sunt fișierele text
FOLDER_PATH = "original_configs"  # Modifică dacă fișierele sunt în alt folder

# Lista fișierelor din folder
files = [f for f in os.listdir(FOLDER_PATH) if os.path.isfile(os.path.join(FOLDER_PATH, f))]

# Salvăm lista într-un fișier JSON
with open("files.json", "w", encoding="utf-8") as json_file:
    json.dump(files, json_file, indent=4)

print("files.json a fost generat cu succes!")
