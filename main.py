from pathlib import Path
import os
def create_file():
    try:
        name = input("Enter the name of the file: ")
        path = Path(name)
        if path.exists():
            print("File already exists.")
        else:
            with open(name, 'w') as fs:
                data = input("Enter the data to write in the file: ")
                fs.write(data)
            print("File created successfully.")
    except Exception as err:
        print(f"Error occurred: {err}")
def read_file():
    try:
        path = Path(input("Enter the name of the file to read: "))
        if path.exists():
            with open(path, 'r') as fs:
                print(fs.read())
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error occurred: {err}")
def update_file():
    try:
        path = Path(input("Enter the name of the file to update: "))
        if path.exists():
            print("Operations available: \n1. Overwrite the file\n2. Append to the file")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                with open(path, 'w') as fs:
                    data = input("Enter the data to write in the file: ")
                    fs.write(data)
            elif choice == 2:
                with open(path, 'a') as fs:
                    data = input("Enter the data to append to the file: ")
                    fs.write(data)
            print("File updated successfully.")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error occurred: {err}")
def delete_file():
    try:
        path = Path(input("Enter the name of the file to delete: "))
        if path.exists():
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("File not found.")
    except Exception as err:
        print(f"Error occurred: {err}")
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")
choice = int(input("\n Enter your choice: "))
if choice == 1:
    create_file()
if choice == 2:
    read_file()
if choice == 3:
    update_file()
if choice == 4:
    delete_file()