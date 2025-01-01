#List all the files in folders that user provides ?
#Step 1 - How to read Input from User
#Step2 - For loop on each and every user.-List files
# identify Module required to Implement this.
#Print Files 
# Handle any knwon error 

import os

def list_files_in_folders(folder_path):
    try:
        files = os.listdir(folder_path)
        return files,None
    except FileNotFoundError:
        return None, " File Not Found "
    except PermissionError:
        return None, "Permission Denied "

def main():
    folder_paths = input("Enter a list of folder paths seperated by spaces: ").split()

    for folder_path in folder_paths:
       files,error_message = list_files_in_folders(folder_path)
       if files:
          print(f"Files in {folder_path}")
          for file in files:
            print(file)
    else:
            print(f"Error in {folder_path}:{error_message}")

if __name__ == "__main__":
    main()