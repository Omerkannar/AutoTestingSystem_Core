# KeyboardUtils.py
# import Listener
# import GlobalVariables
import time

from . import Listener, GlobalVariables
from pynput.keyboard import Key
from pynput.keyboard import Listener as KeyboardListener


class KeyboardUtils:
    def __init__(self):
        self.test_log = "na"
        self.keyboard_listener = KeyboardListener()

    def set_test_log_name(self, name):
        self.test_log = name

    def get_test_log_name(self) -> str:
        return self.test_log

    def keyboard_press(self, key):
        # global fileNameImage_number

        # step 1
        if key == Key.f6 or key == Key.ctrl_l:

            print('Start Step ...')
            a = format(key)
            Listener.listener_keyboard_press(a, GlobalVariables.start_time, GlobalVariables.last_time, self.test_log)
            # total_time = round((time.time() - Global_Setting_Var.start_time), 2)
            # TestLog.writelines(str(total_time) + ' keyboard pressed with {0} \n'.format(key))
            StepNameImage = fileNameImage

            # Util.take_snapshot(StepNameImage, Global_Setting_Var.TopLeft_X, Global_Setting_Var.TopLeft_Y,
            #                    Global_Setting_Var.ButtomRight_X, Global_Setting_Var.ButtomRight_Y, fileNameImage_number)

            time.sleep(0.1)  # wait for the snppoint image to end before continue
            GlobalVariables.toRec = 0
            time_start_gui = time.time()
            if not GlobalVariables.Web_GUI:
                stepProcess, stepResult, stepComment, Critic = DataWindow.getinput(TestLog, ATPfile, CommentFile,
                                                                                   fileNameImage, test_name,
                                                                                   fileNameImage_number)
            else:
                WEB_Income_data = "D:\ATH-AutoTestingSystem\AutoTestingSystem_TempData\Income_data.ini"
                WEB_Step_data = "D:\ATH-AutoTestingSystem\AutoTestingSystem_TempData\Step_data.ini"
                Util.replace_line(WEB_Income_data, 5, "CreateStep   		=1")
                CreateStep = "1"
                while CreateStep == "1":
                    time.sleep(1)
                    with open(WEB_Income_data, "r") as ID:  # open the Income data for decide what to do
                        Lines = ID.readlines()
                        CreateStep = Lines[4].split("=")[-1][:-1]
                        # ChromeIssue.OpenSite("http://127.0.0.1:5000/docs")
                        print("here we should deal with the step data")

                if CreateStep == "0":
                    with open(WEB_Step_data, "r") as SD:  # open the Income data for decide what to do
                        Lines = SD.readlines()
                        stepProcess = Lines[1].split("=")[-1][:-1]
                        stepResult = Lines[2].split("=")[-1][:-1]
                        stepComment = Lines[3].split("=")[-1][:-1]
                        Critic = Lines[4].split("=")[-1][:-1]
                        fileNameImagenum = fileNameImage + "_step_" + str(fileNameImage_number)
                        DataWindow.UpdateATP(ATPfile, stepProcess, stepResult, fileNameImage_number, fileNameImagenum)

            DataWindow.UpdateLog(TestLog, Critic, stepProcess)
            time.sleep(0.5)  # wait for the user form to close before continue
            timeoutofgui = time.time()
            timeingui = timeoutofgui - timestartgui
            Global_Setting_Var.start_time = Global_Setting_Var.start_time + timeingui
            fileNameImage_number = fileNameImage_number + 1
            Global_Setting_Var.toRec = 1

        # remote desktop to CGF 1
        elif key == Key.f7:
            a = format(key)
            Listener.Listener_keyboard_press(a, Global_Setting_Var.start_time, TestLog)
            open_remote_desktop(Global_Setting_Var.F7_IP, Global_Setting_Var.Remote_window_location,
                                Global_Setting_Var.Remote_window_size)

        # remote desktop to TC
        elif key == Key.f8:
            a = format(key)
            Listener.Listener_keyboard_press(a, Global_Setting_Var.start_time, TestLog)
            open_remote_desktop(Global_Setting_Var.F8_IP, Global_Setting_Var.Remote_window_location,
                                Global_Setting_Var.Remote_window_size)
        # remote desktop to Own1
        elif key == Key.f9:
            a = format(key)
            Listener.Listener_keyboard_press(a, Global_Setting_Var.start_time, TestLog)
            open_remote_desktop(Global_Setting_Var.F9_IP, Global_Setting_Var.Remote_window_location,
                                Global_Setting_Var.Remote_window_size)

        # simulate alt tab function
        elif key == Key.f2 or Key == Key.ctrl_r:
            a = format(key)
            Listener.Listener_keyboard_press(a, Global_Setting_Var.start_time, TestLog)
            alt_Tab()


        # step 2
        elif key == Key.esc:
            GlobalVariables.test_time = time.time() - GlobalVariables.start_time
            GlobalVariables.terminate = 1
            # TestLog.writelines("close the file")
            # M_listener.stop()
            K_listener.stop()
            # TestLog.close()
            # ATPfile.close()
            # CommentFile.close()
            Util.close_Notefic()
            Listener.close_file(self.test_log)
            go_2desktop()
            if Global_Setting_Var.Web_GUI == False:
                runMainAutoScript()

            # return False
        # step3
        else:
            if GlobalVariables.toRec == 1:
                a = format(key)
                Listener.listener_keyboard_press(a, GlobalVariables.start_time, GlobalVariables.last_time, self.test_log)
