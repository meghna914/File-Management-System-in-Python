import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"file name {filename} is created successfully!!")
    except FileExistsError:
        print(f"file name {filename} already exists :(")
    except Exception as E:
        print ("An error occurred!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found !!")
    else:
        print("Files in the directory are as follows:\n")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file name {filename} has been deleted successfully!!")
    except FileNotFoundError:
        print("file not found !!")
    except Exception as E:
        print("An error has occurred !!")
        
def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"Content of {filename} is:\n{content}")
    except FileNotFoundError:
        print("file not found !!")
    except Exception as e:
        print("An error has occurred !!")
        
def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter the content to be added in the file:")
            f.write(content + "\n")
            print(f"Content is added to {filename} successfully!!")
    except FileNotFoundError:
        print(f"{filename} does not exist !!")
    except Exception as E:
        print("An error has occurred !!")

def main():
    while True:
        print('\n\nFILE MANAGEMENT SYSTEM\n')
        print("1: Create file")
        print("2: View all files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            filename = input("Enter the filename that you want to create: ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the filename you wanr to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the filename you want to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the filename you want to edit: ")
            edit_file(filename)
        elif choice == '6':
            print("Closing the app...")
            break
        else:
            print("Invalid choice!!")

if __name__ == "__main__":
    main()