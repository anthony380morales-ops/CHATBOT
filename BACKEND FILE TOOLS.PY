import os

def read_file(path: str) -> str:
    if not os.path.exists(path):
        return f"⚠️ File not found: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, content: str) -> str:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"✅ File saved successfully at {path}"

def list_files(directory: str) -> list:
    if not os.path.exists(directory):
        return []
    return os.listdir(directory)
