import psutil
import os

def dump_memory(pid):
    with open(f"/proc/{pid}/mem", "rb") as mem_file:
        memory = mem_file.read()
    
    print("[INFO] Memory Dump Completed.")
    with open("memory_dump.bin", "wb") as f:
        f.write(memory)

pid = int(input("Enter Process ID: "))
dump_memory(pid
