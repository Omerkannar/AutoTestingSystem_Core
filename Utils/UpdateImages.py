import os
import shutil
from tkinter import messagebox
import Global_Setting_Var


def copy_jpg_files(source_folder):

    selected_indices = source_folder.curselection()


    # check the user enter any test or report to the final report
    if selected_indices.__len__() != 1:
        messagebox.showinfo('Auto Test', 'you need to define one report')
        return

    selected = ",".join([source_folder.get(i).split(" ")[-1] for i in selected_indices])
    source_folder = Global_Setting_Var.ParentDirResu + selected
    destination_folder = Global_Setting_Var.ParentDirTest + selected

    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Ensure the Traget folder exists
    if not os.path.exists(destination_folder):
        print(f"Source folder '{destination_folder}' does not exist.")
        return

    # Get a list of JPG files in the source folder excluding those ending with "Diff"
    jpg_files = [file for file in os.listdir(source_folder) if file.lower().endswith('.jpg') and not file.lower().endswith('diff.jpg')]

    if not jpg_files:
        print(f"No eligible JPG files found in '{source_folder}'.")
        return

    # Copy each eligible JPG file to the destination folder

    try:
        for jpg_file in jpg_files:
            source_path = os.path.join(source_folder, jpg_file)
            destination_path = os.path.join(destination_folder, jpg_file)

            # Copy and replace the file
            shutil.copy2(source_path, destination_path)

        messagebox.showinfo('Auto Test', f"the JPG images was update.")
    except Exception as e:
        messagebox.showinfo('Auto Test', f"Error in update images: {e}")

#copy_jpg_files(source_folder, destination_folder)
#copy_jpg_files(source_folder)
