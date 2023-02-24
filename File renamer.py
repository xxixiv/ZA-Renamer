import os

folder = input(r"insert the name of folder eg: drivename:\users\username...: ")

print(f"your old file names{os.listdir(folder)}")

num = 1
for file_name in os.listdir(folder):

    folder_location = f"{folder}{file_name}"

   # dest = folder + input("insert the new name for the file: ") + input("insert the file extension with a dot: ")

    new_name = folder + str(num)

    num += 1

    os.rename(folder_location, new_name)

print("files renamed")

print(f"your new file names {os.listdir(folder)}")
