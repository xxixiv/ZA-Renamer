import os
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog


def rename_files():
    folder_path = folder_entry.get()
    file_prefix = prefix_entry.get()
    file_extension = suffix_entry.get()

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path")
        return

    if not file_extension.startswith("."):
        messagebox.showerror("Error", "File extension should start with a dot (e.g., '.txt')")
        return

    num = 1
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(file_extension.lower()):
            folder_location = os.path.join(folder_path, filename)
            new_name = os.path.join(folder_path, f"{file_prefix} {str(num)}{file_extension}")
            try:
                os.rename(folder_location, new_name)
                num += 1
            except Exception as e:
                messagebox.showerror("Error", str(e))
                return

    messagebox.showinfo("Success", "File renaming completed successfully")


def select_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(tk.END, folder_path)


def select_file_extension():
    file_extension = simpledialog.askstring("Select File Extension", "Enter the file extension (e.g., '.txt'):")
    if file_extension:
        suffix_entry.delete(0, tk.END)
        suffix_entry.insert(tk.END, file_extension)


# Create the main frame
frame = tk.Tk()
frame.title("File Renamer")
frame.geometry('500x200')

# Create the header label
header = tk.Label(frame, text="The World's Best File Renamer".title())
header.grid(row=0)

# Create the folder path entry and label
folder_label = tk.Label(frame, text="Folder Path: ")
folder_label.grid(column=0, row=1)
folder_entry = tk.Entry(frame, width=40, bg="white")
folder_entry.grid(column=1, row=1)
select_folder_button = tk.Button(frame, text="Select Folder", command=select_folder)
select_folder_button.grid(column=2, row=1)

# Create the file prefix entry and label
prefix_label = tk.Label(frame, text="File Prefix: ")
prefix_label.grid(column=0, row=2)
prefix_entry = tk.Entry(frame, width=40, bg="white")
prefix_entry.grid(column=1, row=2)

# Create the file extension entry and label
suffix_label = tk.Label(frame, text="File Extension: ")
suffix_label.grid(column=0, row=3)
suffix_entry = tk.Entry(frame, width=40, bg="white")
suffix_entry.grid(column=1, row=3)
select_extension_button = tk.Button(frame, text="Select Extension", command=select_file_extension)
select_extension_button.grid(column=2, row=3)

# Create the rename button
rename_button = tk.Button(frame, text="Rename", width=10, height=1, fg="black", bg="gray", command=rename_files)
rename_button.grid(column=0, row=4)

# Run the main event loop
frame.mainloop()
