import re

def extract_strings(filename):
    with open(filename, "rb") as f:
        data = f.read()
    
    strings = re.findall(b"[ -~]{4,}", data)  # Extracts ASCII strings
    for string in strings:
        print(string.decode())

print("[INFO] Extracting strings from 'binary.exe'...")
extract_strings("binary.exe")
