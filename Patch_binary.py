def patch_binary(file_path, offset, new_bytes):
    with open(file_path, "r+b") as f:
        f.seek(offset)
        f.write(new_bytes)

print("[INFO] Patching binary.exe...")
patch_binary("binary.exe", 0x10, b"\x90\x90")  # Overwrite with NOP instruction
