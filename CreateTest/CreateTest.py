# CreateTest.py
import os
from datetime import datetime
from Utils import GlobalVariables, Utils
import pyautogui


class CreateTest:
    def __init__(self):
        self.main_version = r"N\\A"
        self.name = r"N\\A"
        self.test_summary = r"N\\A"
        self.test_threshold = r"N\\A"
        self.prerequisite = r"N\\A"
        self.environment = r"N\\A"
        self.timeout = r"N\\A"
        self.site = r"N\\A"
        self.id = -1
        self.date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.id_arr = [0 for i in range(1000)]  # Create array to store test's id
        self.scan_id_in_test_path()

    def scan_id_in_test_path(self):

        def scanRecurse(baseDir):
            for entry in os.scandir(baseDir):
                if entry.is_file():
                    if ".id" in entry.name:
                        with open(os.path.join(baseDir, entry.name), "r") as id_file:
                            line = id_file.readline()
                            id_used = int(line.split('=')[1])
                            self.id_arr[id_used] = 1
                            id_file.close()
                else:
                    yield from scanRecurse(entry.path)

        for i in scanRecurse(os.path.join(os.path.dirname(__file__), r"..\Tests")):
            pass

    def set_test_main_version(self, test_main_version) -> None:
        self.main_version = test_main_version

    def get_test_main_version(self) -> str:
        return self.main_version

    # Create test name
    def set_test_name(self, test_name) -> None:
        self.name = test_name

    def get_test_name(self) -> str:
        return self.name

    def set_test_id(self, test_id) -> None:
        self.id = test_id

    def get_test_id(self) -> int:
        return self.id

    def set_test_date(self, test_date) -> None:
        self.date = test_date

    def get_test_date(self) -> str:
        return self.date

    def set_test_summary(self, test_summary):
        self.test_summary = test_summary

    def get_test_summary(self) -> str:
        return self.test_summary

    def set_test_threshold(self, test_threshold):
        self.test_threshold = test_threshold

    def get_test_threshold(self) -> str:
        return self.test_threshold

    def set_test_prerequisite(self, test_prerequisite):
        self.prerequisite = test_prerequisite

    def get_test_prerequisite(self) -> str:
        return self.prerequisite

    def set_test_environment(self, test_environment):
        self.environment = test_environment

    def get_test_environment(self) -> str:
        return self.environment

    def set_test_site(self, test_site):
        self.site = test_site

    def get_test_site(self) -> str:
        return self.site

    def set_test_timeout(self, test_timeout):
        self.timeout = test_timeout

    def get_test_timeout(self) -> str:
        return self.timeout

    def get_new_id(self):
        for index, value in enumerate(self.id_arr):
            if value == 1:
                pass
            else:
                self.id_arr[index] = 1
                return index

    def print_test_print_parameters(self) -> None:
        pass
        # print("Test name: " + self.name + ", Test id: " + str(self.id) + ", Test date: " + str(self.date))

    def do_main(self) -> str:
        pyautogui.FAILSAFE = False

        # user_test_name = user_test_name + TestAPP
        user_test_name = self.get_test_name()

        # user_test_start_point = self.get_test_environment()  # OmerK - Fix it

        # Create the test directory
        test_path = os.path.join(GlobalVariables.parent_dir_test, user_test_name)
        if os.path.exists(test_path):
            print(r"Test already exists. Can't create test!")
            return "Error", -1
        else:
            os.mkdir(test_path)

        user_main_version = self.get_test_main_version()
        user_test_summary = self.get_test_summary()
        user_test_threshold = self.get_test_threshold()
        user_test_prerequisite = self.get_test_prerequisite()
        user_test_environment = self.get_test_environment()
        user_test_timeout = self.get_test_timeout()
        user_test_site = self.get_test_site()
        user_test_id = self.get_new_id()

        fileNameImage = test_path + "/" + user_test_name  # prefix for the images file
        fileNameImage_number = 1  # suffix for the images file

        fileNameLog = test_path + "/" + user_test_name + ".id"  # user log file name
        TestLog = open(fileNameLog, "w+")  # open the file for writing the user operation
        TestLog.write("id=" + str(user_test_id))
        TestLog.close()

        # create ATP file
        fileNameATP = test_path + "/" + user_test_name + "_ATP.txt"  # user ATP file name
        ATP_file = open(fileNameATP, "w+")  # open the file for writing the ATP - data from user step form
        # create header for the ATP txt file
        Utils.CreateDocHeader(GlobalVariables.version_file, ATP_file, "ATP", str(user_test_id), user_main_version,
                              user_test_name, user_test_summary, user_test_threshold, user_test_prerequisite,
                              user_test_environment, user_test_timeout, user_test_site)
        ATP_file.close()

        return "Success", user_test_id

        # if not Web_GUI:
        #     user_test_name, user_test_summary, diff = DataWindow.gettestinput()  # gets test name and summary from user
        #     Global_Setting_Var.stop_flag = 0
        #     #terminte the process befor we start
        #     if user_test_name =="terminate":
        #         terminateTheprocess()
        # if GlobalVariables.Web_GUI:
        #     # create_test_data = "D:\ATH-AutoTestingSystem\AutoTestingSystem_TempData\create_test.ini"
        #     create_test_data = r"../../AutoTestingSystem_TempData\create_test.ini"
        #     CTD = open(create_test_data, "r")  # open the test file that is going to be executed
        #     Lines = CTD.readlines()
        #     user_test_name = Lines[5].split("=")[-1][:-1]
        #     user_test_summary = Lines[7].split("=")[-1][:-1]
        #     test_start_point = Lines[6].split("=")[-1][:-1]
        #     if test_start_point == 1:
        #         TestAPP = "_Desktop"
        #     elif test_start_point == 2:
        #         TestAPP = "_IOS_WEB"
        #     else:
        #         TestAPP = "_Other1"
        #     user_test_name = user_test_name + TestAPP
        #     diff = Lines[6].split("=")[-1][:-1]
        #     if diff == 0:
        #         Global_Setting_Var.diffrence = Global_Setting_Var.diffrence_static
        #     elif diff == 1:
        #         Global_Setting_Var.diffrence = Global_Setting_Var.diffrence_dynamic
        #     elif diff == 2:
        #         Global_Setting_Var.diffrence = Global_Setting_Var.diffrence_extreme
        #     else:
        #         Global_Setting_Var.diffrence = Global_Setting_Var.diffrence_static
        #
        # Global_Setting_Var.terminate = 0
        # test_name = Util.check_space(user_test_name)  # replaces the spaces with underscore
        # Util.check_name_exists(Global_Setting_Var.ParentDirTest, test_name,
        #                        1)  # check if the test directory is already existing, popup message if it is
        #
        # RandScenrioName = Util.CreateRandTestName(Global_Setting_Var.Notifile)
        #
        # # Create the test directory
        # path = os.path.join(Global_Setting_Var.ParentDirTest, test_name)
        # os.mkdir(path)
        #
        # fileNameImage = path + "/" + test_name  # prefix for the images file
        # fileNameImage_number = 1  # suffix for the images file
        #
        # fileNameLog = path + "/" + test_name + ".txt"  # user log file name
        # TestLog = open(fileNameLog, "w+")  # open the file for writing the user operation
        #
        # # create ATP file
        # fileNameATP = path + "/" + test_name + "_ATP.txt"  # user ATP file name
        # ATPfile = open(fileNameATP, "w+")  # open the file for writing the ATP - data from user step form
        # Util.CreateDocHeader(Global_Setting_Var.versionFile, ATPfile, "ATP", test_name,
        #                      user_test_summary)  # create header for the ATP txt file
        #
        # # create comment filedd
        # fileNameATPcomment = path + "/" + test_name + "_comment.txt"  # user ATP comment file name
        # CommentFile = open(fileNameATPcomment,
        #                    "w+")  # open the file for writing the ATP comment- data from user step form
        # Util.CreateDocHeader(Global_Setting_Var.versionFile, CommentFile, "comment",
        #                      test_name, user_test_summary)  # create header for the ATP commenttxt file
        # Global_Setting_Var.toRec = 1  # flag for define if need to updet the log file or not, 1 = update , 0 = dont update
        # Global_Setting_Var.start_time = time.time()  # start timer
        #
        # # create random string for IOS scenario name
        # RandScenrioName = Util.CreateRandTestName(Global_Setting_Var.RSN)
        # Util.copyRSN()
        # # go_2desktop()  # Goto desktop as the beginning of the test
        #
        # # for test that contaion the WEB suffix go to the IOS web , if contain Desktop suffix do to the desktop for the
        # # other do nothing
        # # if (user_test_name[len(user_test_name)-3:len(user_test_name)]) =="WEB":
        # if "WEB" in user_test_name:
        #     KillIOS()
        #     time.sleep(5)
        #     OpenSite(Global_Setting_Var.site2open)
        # # elif (user_test_name[len(user_test_name) - 3:len(user_test_name)]) == "Desktop":
        # elif "Desktop" in user_test_name:
        #     go_2desktop()
        # else:
        #     pass
        #
        # text_not = "Record test " + test_name
        # NotifThread = threading.Thread(target=Util.Open_Notefic, args=(text_not,), daemon=True)
        # NotifThread.start()  # presnt the status window
        #
        # Global_Setting_Var.toRec = 1  # start recording
        # # start the thread listener keyboard and mouse
        # K_listener = KeyboardListener(on_press=keyboard_press)
        # M_listener = MouseListener(on_click=mouse_click, on_scroll=mouse_scroll)
        #
        # K_listener.start()
        # M_listener.start()
        #
        # K_listener.join()
        # M_listener.join()
        #
        # subprocess.Popen(["python", "Notification.py"])
