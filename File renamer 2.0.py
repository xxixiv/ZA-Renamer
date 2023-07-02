import os

folder = input("Enter the folder path: ")
file_name = input("Enter the file name: ")
file_extension = input("Enter the file extension (e.g., '.txt'): ")
prefix_filter = input("Enter the prefix filter (leave empty for no filter): ")
extension_filter = input("Enter the extension filter (leave empty for no filter): ")

if not os.path.isdir(folder):
    print("Invalid folder path.")
    exit()

print(f"Your old file names: {os.listdir(folder)}")

num = 1
for file in os.listdir(folder):
    if prefix_filter and not file.startswith(prefix_filter):
        continue

    if extension_filter and not file.endswith(extension_filter):
        continue

    folder_location = os.path.join(folder, file)
    new_name = os.path.join(folder, f"{file_name}_{str(num)}{file_extension}")
    try:
        os.rename(folder_location, new_name)
        num += 1
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exit()

print("Files renamed.")
print(f"Your new file names: {os.listdir(folder)}")
