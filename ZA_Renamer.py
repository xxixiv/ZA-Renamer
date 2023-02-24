# First the Importing of the modules and libraries to be used
import os
from tkinter import *

# Create a frame for the display

frame = Tk()

# Give it a title
frame.title("File Renamer")

#frame.iconbitmap(r"C:\Users\Freddie xxix\Desktop\2022\Home_Projects\leafsymbold.ico")
# Set the frame's geometry
frame.geometry('500x200')

# Set the Header and the header's place and grid
header = Label(frame, text="the world's best file renamer".title())

header.place(x=150, y=0)

header.grid(row=0)

# Set the text variable for the Folder, Prefix and Suffix
fold = StringVar()

pref = StringVar()

suff = StringVar()

# Set the Folder's label and entry(for accepting inputs for the folder path) and the Folder's grid
folder_label = Label(frame, text="Folder Path: ")

folder_label.grid(column=0, row=4)

folder = Entry(frame, width=40, textvariable=fold, bg="white")

folder.grid(column=1, row=4)

prefix_lab = Label(frame, text="File Prefix: ")
prefix_lab.grid(column=0, row=5)
prefix = Entry(frame, width=40, textvariable=pref, bg="white")
prefix.grid(column=1, row=5)
suffix_lab = Label(frame, text="File Extension: ")
suffix_lab.grid(column=0, row=6)
suffix = Entry(frame, width=40, textvariable=suff, bg="white")
suffix.grid(column=1, row=6)

def rmBtn():
    num = 1

    for files in os.listdir(folder.get()):
        folder_location = f"{folder.get()}{files}"

        # dest = folder + input("insert the new name for the file: ") + input("insert the file extension with a dot: ")

        new_name = f"{folder.get()}{prefix.get()}  {str(num)}.{suffix.get()}"

        num += 1

        os.rename(folder_location, new_name)


rm_bttn = Button(frame, text="Rename", width=10, height=1, fg="black", bg="gray", command=rmBtn)
rm_bttn.grid(column=0, row=7)
frame.mainloop()

