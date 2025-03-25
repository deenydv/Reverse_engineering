def xor_decrypt(data, key):
    return bytes([b ^ key for b in data])

with open("encrypted.bin", "rb") as f:
    encrypted_data = f.read()

key = 42  # Example XOR key
decrypted_data = xor_decrypt(encrypted_data, key)

with open("decrypted.bin", "wb") as f:
    f.write(decrypted_data)

print("[INFO] Decryption complete. Saved as 'decrypted.bin'"
