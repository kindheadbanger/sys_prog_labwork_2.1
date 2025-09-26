import os
import stat

def permissions(path: str, mode: int):
    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.chmod(file_path, mode)
                print(f"success: {file_path}")
            except Exception as ex:
                print(f"error {file_path}: {ex}")

        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.chmod(dir_path, mode)
                print(f"success: {dir_path}")
            except Exception as ex:
                print(f"error {dir_path}: {ex}")

print("Enter path: ")
a = input()
permissions(a, 0o644)

# "D:/Files/education/Created/test"