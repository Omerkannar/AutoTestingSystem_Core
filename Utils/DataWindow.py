# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 13:41:25 2022

@author: AZucker
"""
import random
# import tkinter
import tkinter as tk
from tkinter import messagebox
# from tkinter import constants
# from tkinter import *
# from tkinter import messagebox
# import random
# import sys
# import GlobalVariables
# #from Code import MainAutoTest
# import MainAutoTest
from Utils import *
import Utils
from datetime import date
# import CreateDoc
# import UpdateImages
# from DuplicateTest import getNewtestName
from PIL import Image, ImageDraw, ImageFont


# import ImageProcess


# import TranslateUserDifftoValue from Util
# subprocess imort Popen

# input: strings
# what does it do: update variables from GUI window to global
# output: none

class DataWindow:
    def __init__(self):
        self.step_process = r"N\\A"
        self.step_result = r"N\\A"
        self.step_comment = r"N\\A"
        self.step_critic = r"N\\A"

    def set_out_step(self, text1, text2, text3, text4):
        self.step_process = text1
        self.step_result = text2
        self.step_comment = text3
        self.step_critic = text4

    # input:
    #   ATPFileName = string - path for the relevant ATP.txt file
    #   StepProcess = string - from UI form
    #   StepResult = string - from UI form
    #   Stepnumber = integer - number of the current picture \ control press in this test
    #   fileNameImage = string - the path of the current snapshot image
    # what does it do: add line with all the data for the ATP.txt file
    # output: none
    def update_ATP(self, ATP_file_name, step_process, step_result, step_number, file_name_image):
        ATP_file_name.writelines(
            str(step_number) + '\t' + step_process + '\t' + step_result + '\t' + file_name_image + 'P\n')

    # input:
    #   CommentFileName = string - path for the relevant comment.txt file
    #   StepProcess = string - from UI form
    #   StepResult = string - from UI form
    #   Stepnumber = integer - number of the current picture \ control press in this test
    #   StepComment = string - from UI form
    #   fileNameImage = string - the path of the current snapshot image
    # what does it do: add line with all the data for the comment.txt file
    # output: none
    def update_comment_ATP(self, comment_file_name, step_process, step_result, step_number, step_comment,
                           file_name_image):
        comment_file_name.writelines(
            str(step_number) + '\t' + step_process + '\t' + step_result + '\t' + step_comment + '\t' + file_name_image +
            'P\n')

    # input:
    #   CommentFileName = string - path for the relevant comment.txt file
    #   critics = string - if the step is critic
    #   StepProcess = string - from UI form
    # what does it do: add line with all the data for the comment.txt file
    # output: none
    # def update_log(self, log_file_name, critics, step_process):
    #     log_file_name.writelines(critics + '\t' + step_process + '\n')

    def add_text_to_image(self, input_image_path, output_image_path, text_to_add):
        # Open the image file
        image = Image.open(input_image_path)

        # Create a drawing object
        draw = ImageDraw.Draw(image)

        # Choose a font and size
        font = ImageFont.truetype("arial.ttf", 136)

        # Choose a color for the text
        text_color = (0, 0, 0)  # White color in RGB

        # Choose the position to place the text (x, y)
        text_position = (300, 300)

        # Add text to the image
        draw.text(text_position, text_to_add, font=font, fill=text_color)

        # Save the modified image
        image.save(output_image_path)

    # input:
    #   ATPFileName = string - path for the relevant ATP.txt file
    #   CommentFileName = string - path for the relevant comment.txt file
    #   fileNameImage = string - the path of the current snapshot image
    #   TestName = string -current test name
    # what does it do:
    #   Step 1 build UI form for collect the data for the current step
    #   Step 2 callSetout() - update global data
    #   Step 3 UpdateATP() - update the ATP file
    #   Step 4 UpdateComnetATP() - update the comment file
    #   Step 5 close() - terminate the UI form
    # output:
    #   stepProcess = string - from UI form
    #   stepResult = string - from UI form
    #   stepComment = string - from UI form
    def get_input(self, ATPFileName, comment_file_name, fileNameImage, test_name, Step_number):
        # step_number = Step_number
        # StepProcess = TestName + "_" + str(step_number)
        # StepResult = TestName + "_" + str(step_number) + "_done"
        # fileNameImage = fileNameImage + "_step_" + str(step_number)
        # Critic = ""
        step_number = ""
        StepProcess = ""
        StepResult = ""
        fileNameImage = ""
        Critic = ""

        step_input = tk.Tk()
        step_input.configure(background='light blue')
        step_input.title("Auto Test - step information ")
        step_input.option_add('*Font', '19')

        # create a UI form o out it on top the other open windows
        step_input.geometry("600x300")
        step_input.attributes("-topmost", True)

        Test_Name_Label = tk.Label(step_input, text=test_name, bg="light blue")  # create a Step Process label
        Step_Number_Label = tk.Label(step_input, text=" Step number - " + str(Step_number),
                                  bg="light blue")  # create a Step Process label
        Step_Process_Label = tk.Label(step_input, text="Step Process", bg="light blue")  # create a Step Process label
        Step_Result_Label = tk.Label(step_input, text="Step Result", bg="light blue")  # create a Step Result label

        # placing the widgets at respective positions in table like structure .
        Test_Name_Label.place(x=10, y=10)
        Step_Number_Label.place(x=300, y=10)
        Step_Process_Label.place(x=10, y=50)
        Step_Result_Label.place(x=10, y=100)

        # create a text entry box
        step_process_from_entry = tk.Entry(step_input, width=30)
        step_process_from_entry.insert(0, StepProcess)
        step_result_from_entry = tk.Entry(step_input, width=30)
        step_result_from_entry.insert(0, StepResult)

        # placing the widgets at respective positions in table like structure .
        step_process_from_entry.place(x=150, y=50)
        step_result_from_entry.place(x=150, y=100)

        # terminate the UI form
        def close_step():
            step_input.destroy()

        # On button press does step 2 - 5
        def my_click():
            # step_process_update = self.step_process.get()
            # step_result = step_result.get()
            # critic = drop_critic.get()
            self.set_out_step(step_process_from_entry.get(), step_result_from_entry.get(), "none", self.step_critic)
            self.update_ATP(ATPFileName, self.step_process, self.step_result, step_number, fileNameImage)
            close_step()

        # get user comment for tis test
        def comment_click():
            commentWin = tk.Tk()
            commentWin.configure(background='light green')
            commentWin.title("Auto Test")
            commentWin.option_add('*Font', '19')
            commentWin.geometry("550x150")
            commentWin.attributes("-topmost", True)
            Comment_Label = Label(commentWin, text="Add comment for this step",
                                  bg="light green")  # create a Step comment label
            Comment_Label.pack()  # grid(row=1, column=1)
            Comment = tk.Entry(commentWin, width=50)
            Comment.pack()  # .grid(row=2, column=1, ipadx="100")

            def close_comment():
                commentWin.destroy()

            def save_comment():
                StepComment = Comment.get()
                self.update_comment_ATP(comment_file_name, "", "", step_number, self.step_comment, fileNameImage)
                text_to_add = "failed step \n " + StepComment + "\n" + Utils.create_random_test_name(
                    GlobalVariables.RSN)
                full_file_name_image = fileNameImage + "P.jpg"
                self.add_text_to_image(full_file_name_image, full_file_name_image, text_to_add)
                close_comment()

            save_comment_button = tk.Button(commentWin, text="save comment", height=2, width=12, command=save_comment)
            save_comment_button.pack()  # grid(row=3, column=0)

            commentWin.protocol("WM_DELETE_WINDOW", close_comment)

            commentWin.mainloop()

        # placing the widgets at respective positions in table like structure .
        myButton = tk.Button(step_input, text="save", height=2, width=7, command=my_click)
        myButton.place(x=50, y=200)

        commentButton = tk.Button(step_input, text="comment", height=2, width=7, command=comment_click)
        commentButton.place(x=200, y=200)

        linkButton = tk.Button(step_input, text="link", height=2, width=7)
        linkButton.place(x=350, y=200)

        critic_option = ["normal", "show stopper"]

        # data type of menu text
        drop_critic = tk.StringVar(step_input)
        # initial menu text
        drop_critic.set(critic_option[0])
        # Create Dropdown menu
        drop = tk.OptionMenu(step_input, drop_critic, *critic_option)
        drop.place(x=50, y=150)

        # Bind the on_close function to the window close event
        step_input.protocol("WM_DELETE_WINDOW", my_click)

        step_input.mainloop()
        return self.step_process, self.step_result, self.step_comment, self.step_critic

    # # input: strings
    # # what does it do: update variables from GUI window to global
    # # output: none
    # def set_out_test(self, text1, text2, num1) -> (str, str, int):
    #     return text1, text2, num1
    #
    # # input: none
    # # what does it do:
    # #   Step 1 build UI form for collect the name of the test
    # #   Step 2 callSetout() - update global data
    # #   Step 3 close() - save ot terminate the UI form
    # # output:
    # #   test name  = string - from UI form
    #
    # def get_test_input(self):
    #     Env = ""
    #     test_name = "Test_" + str(random.randint(1, 9999))  # create default test name
    #     type_difference_test = 9
    #
    #     test_input = Tk()
    #     test_input.configure(background='light blue')
    #     test_input.title("Auto Test  - Create ")
    #     test_input.option_add('*Font', '19')
    #
    #     # def open_WebIOS():
    #     #     Popen("webIOS.py")
    #
    #     # create a UI form o out it on top the other open windows
    #     test_input.geometry("820x360")
    #     test_input.lift()
    #
    #     # create a text entry box and  placing the widgets at respective positions in table like structure .
    #     Test_Name_Label = Label(test_input, text="Insert test name below - use only letters or numbers or spaces",
    #                             bg="light blue")  # create a test name label
    #     Test_Name_Label.grid(row=1, column=1)
    #     Test_Summary_Label = Label(test_input, text="Insert test Prerequisite",
    #                                bg="light blue")  # create a test name label
    #     Test_Summary_Label.grid(row=3, column=1)
    #
    #     Test_Space_Label = Label(test_input, text="******************************************",
    #                              bg="light blue")  # create a test name label
    #     Test_Space_Label.grid(row=5, column=1)
    #
    #     Test_Trash_hold_Label = Label(test_input, text="Test trash hold: Static, Dynamic or Extreme",
    #                                   bg="light blue")  # create a test name label
    #     Test_Trash_hold_Label.grid(row=6, column=1)
    #
    #     Test_Environment_Label = Label(test_input, text="Test environment",
    #                                    bg="light blue")  # create a test name label
    #     Test_Environment_Label.grid(row=8, column=1)
    #
    #     # create a text entry box and  placing the widgets at respective positions in table like structure .
    #     Test_Name = tk.Entry(test_input, width=20)
    #     Test_Name.insert(0, test_name)
    #     Test_Name.grid(row=2, column=1, ipadx="100")
    #
    #     Test_Summary = tk.Entry(test_input, width=20)
    #     Test_Summary.insert(0, test_name)
    #     Test_Summary.grid(row=4, column=1, ipadx="100")
    #
    #     # terminate the UI form
    #     def close_test():
    #         test_input.destroy()
    #
    #     # On button press does step 2 - 3
    #     def click_to_save() -> (str, str, int):
    #         TestName = Test_Name.get()
    #         TestSummary = Test_Summary.get()
    #         select_difference()
    #         select_environment()
    #         text_name, test_summary, diff = set_out_test(TestName + GlobalVariables.test_app, TestSummary,
    #                                                      GlobalVariables.difference)
    #         close_test()
    #         return text_name, test_summary, diff
    #
    #     # terminate the procedure of the testing
    #     def exit_process() -> (str, str, int):
    #         TestName = "terminate"
    #         TestSummary = "terminate"
    #         text_name, test_summary, diff = set_out_test(TestName, TestSummary, 5000)
    #         close_test()
    #         return text_name, test_summary, diff
    #
    #     def select_difference():
    #         difference_type = var.get()
    #         GlobalVariables.difference = translate_user_diff_to_value(difference_type)
    #
    #     def select_environment():
    #         environment_type = var_env.get()
    #         if environment_type == 0:
    #             GlobalVariables.TestAPP = "_Desktop"
    #         elif environment_type == 1:
    #             GlobalVariables.TestAPP = "_IOS_WEB"
    #         elif environment_type == 2:
    #             GlobalVariables.TestAPP = "_Other1"
    #         else:
    #             GlobalVariables.TestAPP = "_Other1"
    #
    #     def translate_user_diff_to_value(num):
    #
    #         if num == 0:
    #             difference = GlobalVariables.difference_static
    #         elif num == 1:
    #             difference = GlobalVariables.difference_dynamic
    #         elif num == 2:
    #             difference = GlobalVariables.difference_extreme
    #         else:
    #             difference = 0
    #         return difference
    #
    #     # placing the widgets at respective positions in table like structure .
    #     myButton = tk.Button(test_input, text="save", height=2, width=8, command=click_to_save)
    #     myButton.grid(row=3, column=0)
    #
    #     # placing the widgets at respective positions in table like structure .
    #     myButton = tk.Button(test_input, text="terminate", height=2, width=8, command=exit_process)
    #     myButton.grid(row=3, column=2)
    #
    #     var = tk.IntVar()
    #
    #     R1 = tk.Radiobutton(test_input, text="Static", bg="light blue", variable=var, value=0,
    #                         command=select_difference)
    #     R1.grid(row=7, column=0, padx="10", pady="10", sticky="W")
    #     R2 = tk.Radiobutton(test_input, text="Dynamic", bg="light blue", variable=var, value=1,
    #                         command=select_difference)
    #     R2.grid(row=7, column=1, padx="200", pady="10", sticky="W")
    #     R3 = tk.Radiobutton(test_input, text="Extreme", bg="light blue", variable=var, value=2,
    #                         command=select_difference)
    #     R3.grid(row=7, column=2, sticky="W")
    #
    #     # Testinput.mainloop()
    #
    #     var_env = tk.IntVar()
    #
    #     R1_E1 = tk.Radiobutton(test_input, text="Desktop", bg="light blue", variable=var_env, value=0,
    #                            command=select_environment)
    #     R1_E1.grid(row=9, column=0, padx="10", pady="10", sticky="W")
    #     R2_E2 = tk.Radiobutton(test_input, text="IOS_WEB", bg="light blue", variable=var_env, value=1,
    #                            command=select_environment)
    #     R2_E2.grid(row=9, column=1, padx="200", pady="10", sticky="W")
    #     R3_E3 = tk.Radiobutton(test_input, text="Other1", bg="light blue", variable=var_env, value=2,
    #                            command=select_environment)
    #     R3_E3.grid(row=9, column=2, sticky="W")
    #
    #     # Bind the on_close function to the window close event
    #     test_input.protocol("WM_DELETE_WINDOW", exit_process)
    #
    #     test_input.mainloop()
    #
    #     return (test_name, test_summary, diffrence_value)
    #
    # def startupprocedure(self):
    #     startupform = tk.Tk()
    #     startupform.title("Auto Test start up")
    #     startupform.option_add('*Font', '19')
    #     startupform.geometry("1300x950+50+50")
    #
    #     #
    #     start_up_form_Label = Label(startupform,
    #                                 text="what would you like to do? ,  Create new test,  Run tests plan from "
    #                                      "Library or Create report  ")  # create a test name label
    #     start_up_form_Label.place(x=10, y=10)
    #     Library_Label = Label(startupform, text="Test Library")  # create a test name label
    #     Library_Label.place(x=100, y=50)
    #     Library_Result_Label = Label(startupform, text="Test Result Library")  # create a test name label
    #     Library_Result_Label.place(x=870, y=50)
    #
    #     myTestList = os.listdir(GlobalVariables.parent_dir_test)
    #     myTestListBox = tk.Listbox(startupform, height=10, selectmode=tk.constants.MULTIPLE)
    #     myTestListBox.place(x=30, y=80, width=500, height=500)
    #
    #     scrollbarTest = tk.Scrollbar(startupform, orient=tk.constants.VERTICAL, command=myTestListBox.yview)
    #     myTestListBox['yscrollcommand'] = scrollbarTest.set
    #     scrollbarTest.place(x=520, y=80, width=10, height=500)
    #
    #     myResList = os.listdir(GlobalVariables.parent_dir_result)
    #     myResListBox = tk.Listbox(startupform, height=10, selectmode=tk.constants.MULTIPLE)
    #     myResListBox.place(x=750, y=80, width=500, height=500)
    #
    #     scrollbarRes = tk.Scrollbar(startupform, orient=tk.constants.VERTICAL, command=myResListBox.yview)
    #     myResListBox['yscrollcommand'] = scrollbarRes.set
    #     scrollbarRes.place(x=1270, y=80, width=10, height=500)
    #
    #     def ts_to_dt(ts):
    #         date_time = datetime.datetime.fromtimestamp(ts)
    #         str_date_time = date_time.strftime(" %d-%m-%y, %H:%M")
    #         return str_date_time
    #
    #     # created by list box of the tests sorted by time
    #     testlist = []
    #     for file in myTestList:
    #         if not ("." in file):
    #             i = (os.path.getctime(GlobalVariables.parent_dir_test + file), file)
    #             testlist.append(i)
    #     testlist.sort(reverse=tk.constants.TRUE, key=lambda x: x[0])
    #
    #     for i in range(len(testlist)):
    #         fulldata = str(ts_to_dt(testlist[i][0])) + "    " + testlist[i][1]
    #         myTestListBox.insert(tk.constants.END, fulldata)
    #
    #     # created by list box of the tests resualt  sorted by time
    #     ResList = []
    #     for Resfile in myResList:
    #         if not ("." in Resfile):
    #             i = (os.path.getctime(GlobalVariables.parent_dir_result + Resfile), Resfile)
    #             ResList.append(i)
    #     ResList.sort(reverse=tk.constants.TRUE, key=lambda x: x[0])
    #
    #     for i in range(len(ResList)):
    #         fulldata = str(ts_to_dt(ResList[i][0])) + "    " + ResList[i][1]
    #         myResListBox.insert(tk.constants.END, fulldata)
    #
    #     def createTest():
    #         GlobalVariables.user_selector = 1
    #         startupform.destroy()
    #
    #     def clearLoogger():
    #         text_widget.delete('1.0', tk.END)
    #         with open((GlobalVariables.parent_dir_result + "/currentresult.txt"), 'w') as file:
    #             pass
    #         with open(GlobalVariables.parent_dir_result + "/currentresult.txt") as file:
    #             content = file.read()
    #             text_widget.insert(tk.END, content)
    #             # Insert new content
    #             new_content = "Report review was deleted."
    #             text_widget.insert(tk.END, new_content)
    #
    #     def presentpreview(event):
    #         # Get the index of the clicked position
    #         index = text_widget.index(tk.CURRENT)
    #
    #         # Find the start and end indices of the current line
    #         line_start = text_widget.index(f"{index} linestart")
    #         line_end = text_widget.index(f"{index} lineend")
    #
    #         # Get the raw data of the entire line
    #         raw_line_data = text_widget.get(line_start, line_end)
    #         stepname = raw_line_data.split(' ')
    #         folderName = stepname[0][1:]
    #         fileName = stepname[9][1:-4]
    #         Diffimage_path = (GlobalVariables.parent_dir_result + folderName + "/" + fileName + "_N_Diff.jpg")
    #         Cutimage_path = (GlobalVariables.parent_dir_result + folderName + "/" + fileName + "_Cut.jpg")
    #         concatenate_path = (GlobalVariables.parent_dir_result + folderName + "/" + "concatenate.jpg")
    #
    #         ImageProcess.concatenate_images_vertically(Diffimage_path, Cutimage_path, concatenate_path)
    #
    #         # Use the default associated program to open the file
    #         try:
    #             os.startfile(concatenate_path)
    #         except FileNotFoundError:
    #             messagebox.showinfo("Error", "the DIff file and \ or the cut file weren't found .")
    #         except Exception as e:
    #             messagebox.showinfo("Error", f"An error occurred: {e}")
    #
    #     def runTests():
    #         GlobalVariables.userSellector = 2
    #         selected_indices = myTestListBox.curselection()
    #         tempList = []
    #         for i in selected_indices:
    #             t_selected = myTestListBox.get(i).split(" ")[-1:]
    #             tempList = tempList + t_selected
    #
    #         selected = ",".join(tempList)
    #         # selected = ",".join([myTestListBox.get(i).split(" ")[-1:].sp for i in selected_indices])
    #         if selected != "":
    #             create_file(selected)
    #             startupform.destroy()
    #         else:
    #             messagebox.showinfo('Auto Test', 'you need to define at least one test')
    #
    #     def reportATP():
    #         T = date.today().strftime("%B%d%Y")
    #         fileName = GlobalVariables.doc_folder + "\ATP_" + str(T) + ".docx"
    #         CreateDoc.createDocx(myTestListBox, "ATP", fileName)
    #
    #     def reportATR():
    #         T = date.today().strftime("%B%d%Y")
    #         fileName = GlobalVariables.doc_folder + "\ATR_" + str(T) + ".docx"
    #         CreateDoc.createDocx(myResListBox, "ATR", fileName)
    #
    #     # def duplicate_test():
    #     #     get_new_test_name(myTestListBox)
    #
    #     def UpdatePic():
    #         UpdateImages.copy_jpg_files(myResListBox)
    #
    #     def close():
    #         GlobalVariables.user_selector = 0
    #         startupform.destroy()
    #         sys.exit()
    #
    # def create_file(string): TestLog = open(GlobalVariables.test_list_f, "w")  # open the test list TestLog.write(
    # "# this file contain the list of Test_Name (similar name to the one in test folder). Add space + ""Test" "after
    # the test name \n") TestList = string.split(',') for test in range(len(TestList)): TestLog.write(TestList[test]
    # + " Test\n") TestLog.write(
    # "*********************************************EOF**************************************\n") TestLog.close()
    #
    #     def PicStatus():
    #         picture_status = var_doc.get()
    #         GlobalVariables.PicOption = picture_status
    #         # print(GlobalVariables.PicOption)
    #
    #     def set_scroll_to_end():
    #         text_widget.insert("end", "---------->\n")
    #         text_widget.see("end")
    #
    #     # placing the widgets at respective positions in table like structure .
    #     create_button = tk.Button(startupform, text="Create", fg='green', height=1, width=12, command=createTest)
    #     create_button.place(x=580, y=120)
    #
    #     # placing the widgets at respective positions in table like structure .
    #     run_button = tk.Button(startupform, text="Run", fg='green', height=1, width=12, command=runTests)
    #     run_button.place(x=580, y=180)
    #
    #     # placing the widgets at respective positions in table like structure .
    #     report_ATP_button = tk.Button(startupform, text="ATP", fg='blue', height=1, width=12, command=reportATP)
    #     report_ATP_button.place(x=580, y=280)
    #
    #     # placing the widgets at respective positions in table like structure .
    #     report_ATR_button = tk.Button(startupform, text="ATR", fg='blue', height=1, width=12, command=reportATR)
    #     report_ATR_button.place(x=580, y=340)
    #
    #     # duplicate_test_button = tk.Button(startupform, text="Duplicate Test", fg='black', height=1, width=12,
    #     #                                   command=duplicate_test)
    #     # duplicate_test_button.place(x=580, y=480)
    #
    #     update_picture_button = tk.Button(startupform, text="Update Pic", fg='black', height=1, width=12,
    #                                       command=UpdatePic)
    #     update_picture_button.place(x=580, y=540)
    #
    #     # placing the widgets at respective positions in table like structure .
    #     close_button = tk.Button(startupform, text="Close", fg='red', height=1, width=12, command=close)
    #     close_button.place(x=580, y=620)
    #
    #     # placing the widgets at respective positions in table like structure .
    #     clear_logger_button = tk.Button(startupform, text="Clear", fg='red', height=1, width=12, command=clearLoogger)
    #     clear_logger_button.place(x=1100, y=750)
    #
    #     var_doc = tk.IntVar()
    #
    #     R1 = tk.Radiobutton(startupform, text="0-Pic", variable=var_doc, value=0, command=PicStatus)
    #     R1.place(x=600, y=410)
    #
    #     R1 = tk.Radiobutton(startupform, text="1-Pic", variable=var_doc, value=1, command=PicStatus)
    #     R1.place(x=550, y=440)
    #
    #     R1 = tk.Radiobutton(startupform, text="2-Pic", variable=var_doc, value=2, command=PicStatus)
    #     R1.place(x=670, y=440)
    #
    #     start_up_form_report_label = Label(startupform, text="Report Viewer - click on the step to open review ")
    #     start_up_form_report_label.place(x=50, y=660)
    #
    #     text_widget = tk.Text(startupform, wrap="word", width=120, height=10)
    #     text_widget.place(x=50, y=700, width=1000, height=210)
    #     text_widget.bind("<Button-1>", presentpreview)
    #
    #     scroll_bar_text_widget = tk.Scrollbar(startupform, orient=tk.constants.VERTICAL, command=text_widget.yview)
    #     text_widget['yscrollcommand'] = scroll_bar_text_widget.set
    #     scroll_bar_text_widget.place(x=1070, y=700, width=20, height=195)
    #
    #     with open(GlobalVariables.parent_dir_result + "/currentresult.txt", 'r') as file:
    #         content = file.read()
    #         text_widget.insert(tk.END, content)
    #
    #     set_scroll_to_end()
    #
    #     # Bind the on_close function to the window close event
    #     startupform.protocol("WM_DELETE_WINDOW", close)
    #
    #     startupform.mainloop()
    #
    #     return GlobalVariables.user_selector


def end_massage():
    tk.messagebox.showinfo('Auto Test', 'End of procedure')


def main():
    print("Running DataWindow.py directly")


if __name__ == "__main__":
    main()
