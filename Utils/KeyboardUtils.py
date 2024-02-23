# KeyboardUtils.py
# import Listener
# import GlobalVariables
import time

from . import Listener, GlobalVariables, Utils
from pynput.keyboard import Key


class KeyboardUtils:
    def __init__(self):
        self.test_log = "na"
        self.last_pressed_key = "na"
        self.file_name_image_path = "na"
        self.file_name_image_number = 0

    def set_test_log_name(self, name):
        self.test_log = name

    def get_test_log_name(self) -> str:
        return self.test_log

    def get_last_pressed_key(self) -> str:
        return self.last_pressed_key

    def set_last_pressed_key(self, key):
        self.last_pressed_key = key

    def get_file_image_path(self) -> str:
        return self.file_name_image_path

    def set_file_image_path(self, path):
        self.file_name_image_path = path

    def get_file_image_number(self) -> int:
        return self.file_name_image_number

    def set_file_image_number(self, number: int):
        self.file_name_image_number = number

    def keyboard_press(self, key):
        # global fileNameImage_number
        # self.set_last_pressed_key(key)
        # step 1
        if key == Key.f6 or key == Key.ctrl_l:

            print('Start Step ...')
            a = format(key)
            Listener.listener_keyboard_press(a, self.test_log)
            # total_time = round((time.time() - GlobalVariables.start_time), 2)
            # # TestLog.writelines(str(total_time) + ' keyboard pressed with {0} \n'.format(key))
            stepImageName = self.get_file_image_path()
            StepImageNumber = self.get_file_image_number()
            #
            Utils.take_snapshot(stepImageName, GlobalVariables.top_left_x, GlobalVariables.top_left_y,
                                GlobalVariables.bottom_right_x, GlobalVariables.bottom_right_y, StepImageNumber)
            self.set_file_image_number(self.get_file_image_number() + 1)

            # DataWindow.UpdateLog(TestLog, Critic, stepProcess)
            # time.sleep(0.5)  # wait for the user form to close before continue
            # timeoutofgui = time.time()
            # timeingui = timeoutofgui - timestartgui
            # Global_Setting_Var.start_time = Global_Setting_Var.start_time + timeingui
            # fileNameImage_number = fileNameImage_number + 1
            # Global_Setting_Var.toRec = 1

        # remote desktop to CGF 1
        elif key == Key.f7:
            a = format(key)
            Listener.listener_keyboard_press(a, self.test_log)
            Utils.open_remote_desktop(GlobalVariables.f7_ip, GlobalVariables.Remote_window_location,
                                      GlobalVariables.Remote_window_size)

        # remote desktop to TC
        elif key == Key.f8:
            a = format(key)
            Listener.listener_keyboard_press(a, self.test_log)
            Utils.open_remote_desktop(GlobalVariables.f8_ip, GlobalVariables.Remote_window_location,
                                      GlobalVariables.Remote_window_size)
        # remote desktop to Own1
        elif key == Key.f9:
            a = format(key)
            Listener.listener_keyboard_press(a, self.test_log)
            Utils.open_remote_desktop(GlobalVariables.f9_ip, GlobalVariables.Remote_window_location,
                                      GlobalVariables.Remote_window_size)

        # simulate alt tab function
        elif key == Key.f2 or Key == Key.ctrl_r:
            a = format(key)
            Listener.listener_keyboard_press(a, self.test_log)
            Utils.alt_Tab()

        # step 2
        elif key == Key.esc:
            a = format(key)
            Listener.listener_keyboard_press(a, self.test_log)
            GlobalVariables.test_time = time.time() - GlobalVariables.start_time
            GlobalVariables.terminate = 1
            Utils.close_Notification()
            # self.test_log.writelines("close the file")
            Listener.close_file(self.test_log)

        # step3
        else:
            if GlobalVariables.toRec == 1:
                a = format(key)
                Listener.listener_keyboard_press(a, self.test_log)

    def terminate_create_test(self):
        # Zucker comment
        # Omer Ka
        pass

