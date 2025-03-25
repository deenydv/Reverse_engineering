import marshal
import dis

def extract_functions(pyc_file):
    with open(pyc_file, "rb") as f:
        f.read(16)  # Skip header
        code_obj = marshal.load(f)
    
    print("[INFO] Extracted functions:")
    for const in code_obj.co_consts:
        if isinstance(const, type(code_obj)):
            print(f" - {const.co_name}")

extract_functions("__pycache__/target.cpython-39.pyc"
