# Utils.py
import datetime
import os
import platform
import re
import sys
import time
from tkinter import Tk, Label
import pygetwindow


from . import GlobalVariables


def replace_line(file_name, line_number, new_string):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        if 1 <= line_number <= len(lines):
            lines[line_number - 1] = new_string + "\n"

            with open(file_name, "w") as file:
                file.writelines(lines)

            print(f"Line {line_number} replaced successfully.")
        else:
            print(f"Invalid line number: {line_number}")

    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except IOError as e:
        print(f"An error occurred while reading or writing the file: {e}")


# input:
#   versionFile = string - path for the  version declaration txt file according to setting file
#   filenamedest = "pointer" to open TXT file
#   docType = string - define if the destination file is going to be ATP, ATP comment or ATR
#   testName = string - the current test name
# what does it do:
#   Step 1 write general  data in destination file
#   Step 2 copy version data to  destination file + add data for version modification
#   Step 3 create header for the process table according  to the type of the DOC
# output: none
def CreateDocHeader(versionFile, filename, docType, test_id, test_version, test_name, test_summary, test_threshold,
                    test_prerequisite, test_environment, test_timeout, test_site, version_mnot=None):
    # step 1
    filename.writelines('************** ' + test_name + ' ' + docType + ' **************\n\n')
    filename.writelines('Test ID:\t\t\t' + test_id + '\n\n')
    filename.writelines('User Selection:\n')
    filename.writelines('===============\n')
    filename.writelines('IOS Version:\t\t')
    filename.writelines(test_version + '\n')
    filename.writelines('Test name:\t\t\t')
    filename.writelines(test_name + '\n')
    filename.writelines('Summary:\t\t\t')
    filename.writelines(test_summary + '\n')
    curDiffNum = test_threshold
    if curDiffNum == "Static":
        curDiffStr = "Static - Nothing move"
    elif curDiffNum == "Dynamic":
        curDiffStr = "Dynamic - Small amount of moving object"
    elif curDiffNum == "Extreme":
        curDiffStr = "Extreme - Large amount of moving object"
    else:
        curDiffStr = ""
    filename.writelines('Threshold:\t\t\t')
    filename.writelines('Test difference filter was define as: ' + curDiffStr + ' \n')
    filename.writelines('Prerequisite:\t\t')
    filename.writelines(test_prerequisite + '\n')
    filename.writelines('Environment:\t\t')
    filename.writelines(test_environment + '\n')
    filename.writelines('TimeOut:\t\t\t')
    filename.writelines(test_timeout + '\n')
    filename.writelines('Site:\t\t\t\t')
    filename.writelines(test_site + '\n\n')
    general_Data(filename)

    # step 2
    file_Source = open(versionFile, "r")
    version_m_time = os.path.getmtime(versionFile)
    version_m_time_str = datetime.datetime.fromtimestamp(version_m_time).strftime("%B %d %Y\t%H:%M:%S")

    for line in file_Source:
        filename.writelines(line)
    file_Source.close()
    filename.writelines('\n->>> Versions data was update on: ' + version_m_time_str + ' \n')
    # Step 3
    if docType == "ATP":
        filename.writelines('\nATP procedure of ' + test_name + ':\n')
        filename.writelines('===============\n')
        filename.writelines('Step number\t\tStep name\t\tStep expected result\t\tImage path\n')
    elif docType == "comment":
        filename.writelines('\n \n' + test_name + ' ATP comment procedure :\n')
        filename.writelines('Step number \t  Step comment \t image path \n')
    else:
        filename.writelines('\n \n' + test_name + ' ATR procedure :\n')
        filename.writelines(
            'Step number\tStep name\tStep expected result\tImage path\tDifference from ATP\tStatus\n')


# input: "pointer" to open TXT file
# what does it do: write time + date + the machine name that run the script in the income TXT file
# output: none
def general_Data(filename):
    now = datetime.datetime.now()
    str_now = now.strftime("%B %d %Y\t%H:%M:%S")
    filename.writelines('General data:  \n')
    filename.writelines('===============\n')
    filename.writelines('This DOC was created in:\t\t' + str_now + '\n')
    filename.writelines('This DOC was created from:\t\t' + platform.uname().node + '\n\n')


def return_Dictionary(folder_path):
    new_dict = []
    # Walk through the folder and its sub folders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file has a .txt extension
            # if file.endswith("_ATP.txt") or file.endswith("_ATR.txt"):
            if "_ATP.txt" in file or "_ATR.txt" in file:
                # Print the full path to the txt file
                txt_file_path = os.path.join(root, file)
                # print(txt_file_path)
                temp = bring_Data(txt_file_path)
                if temp != "none":
                    # print (temp)
                    new_dict.append(temp)
    return new_dict


def bring_Data(File):
    my_dict = {
        "test_id": "v1",
        "main_version": "v2",
        "test_name": "v3",
        "test_summary": "v4",
        "test_threshold": "v5",
        "test_runtime": "v6",
        "test_prerequisite": "v7",
        "test_site": "v8"
    }
    create_time = os.path.getctime(File)
    try:
        test_log = open(File, "r")  # open the test list
        test_line = test_log.readlines()
        if len(test_line) < 2:
            return "none"
        for line in test_line:
            if "Test ID" in line:
                my_dict["test_id"] = re.sub(r"[\n\t\s]*", "", line).split(":")[1]
            if "IOS Version" in line:
                my_dict["main_version"] = re.sub(r"[\n\t\s]*", "", line).split(":")[1]
            if "Test name" in line:
                my_dict["test_name"] = re.sub(r"[\n\t\s]*", "", line).split(":")[1]
            if "Summary" in line:
                my_dict["test_summary"] = re.sub(r"[\n\t]*", "", line.split(":")[1])
            if "Threshold" in line:
                my_dict["test_threshold"] = re.sub(r"[\n\t]*", "", line.split(":")[2])
            if "Environment" in line:
                my_dict["test_environment"] = re.sub(r"[\n\t\s]*", "", line).split(":")[1]
            if "Prerequisite" in line:
                my_dict["test_prerequisite"] = re.sub(r"[\n\t\s]*", "", line).split(":")[1]
            if "TimeOut" in line:
                my_dict["test_runtime"] = re.sub(r"[\n\t\s]*", "", line).split(":")[1]
            if "Site" in line:
                my_dict["test_site"] = re.sub(r"[\n\t\s]*", "", line).split(":")[1]

    except:
        return "none"

    # if "IOS_WEB" in (my_dict["Name"]):
    #     my_dict["StartPoint"] = 'IOS_WEB'
    # elif "Desktop" in (my_dict["Name"]):
    #     my_dict["StartPoint"] = 'Desktop'
    # else:
    #     my_dict["StartPoint"] = 'Other'

    # print(my_dict)
    return my_dict


def whereIsIT(string, LineList):
    count = 0
    for line in LineList:
        count = count + 1
        if string in line:
            return count
    return 0


# input:
#   text = string - text to be written in the window
# what does it do:create and display TXT (status window) file with the income "text"  inside
#               use parameters from setting file in order to display the window correctly
# output: none
def open_Notification(text):
    GlobalVariables.stop_flag = False
    notification_window = Tk()
    notification_window.title("AutoTestNotification")
    notification_window.geometry("1000x30+2+2")
    notification_window.option_add('*Font', '19')
    notification_window.configure(background='light green')
    notification_window.attributes("-topmost", True)
    notification_window.lift()
    notification_label = Label(notification_window, text=text, bg="light green")
    notification_label.pack()
    notification_window.protocol("WM_DELETE_WINDOW", kill_Process)
    notification_window.mainloop()


# input: none
# what does it do: "find" the status window and close it
# output: none
def close_Notification():
    if not GlobalVariables.stop_flag:
        Notif_win1 = pygetwindow.getWindowsWithTitle('AutoTestNotification')
        # Check if the list is not empty
        if Notif_win1:
            # Pause for 2 seconds (you might want to adjust this delay as needed)
            time.sleep(2)

            # Close the first window with the specified title
            Notif_win1[0].close()
        else:
            print("No window with title 'AutoTestNotification' found.")


def kill_Process():
    pass
    GlobalVariables.stop_flag = True
    # pyautogui.press('esc')
    sys.exit()
