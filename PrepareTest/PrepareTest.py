# PrepareTest.py
import os
import subprocess
import threading
from datetime import datetime
from Utils import GlobalVariables, Utils
# from Utils import KeyboardUtils, MouseUtils
from Utils.KeyboardUtils import KeyboardUtils
import pyautogui
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key


class PrepareTest:
    def __init__(self):
        self.id = -1
        self.name = "na"

    def set_test_id(self, test_id) -> None:
        self.id = test_id

    def get_test_id(self) -> int:
        return self.id

    def set_test_name(self, test_name) -> None:
        self.name = test_name

    def get_test_name(self) -> str:
        return self.name

    def get_test_data(self):
        test_path = os.path.join(GlobalVariables.parent_dir_test, self.name)
        if not os.path.exists(test_path):
            return "Error"
        with open(os.path.join(test_path, self.name + "_ATP.txt"), "r") as test_file:  # read the setting parameters
            lines = test_file.readlines()
            print(lines)

    def do_main(self) -> str:
        path = self.get_test_data()

        text_notification = "Record test " + self.name
        NotifThread = threading.Thread(target=Utils.open_Notification, args=(text_notification,), daemon=True)
        # Present the status window
        NotifThread.start()

        test_path = os.path.join(GlobalVariables.parent_dir_test, self.name)
        log_file = open(os.path.join(test_path, self.name + ".txt"), "w+")  # open the file for writing the user operation
        # log_file.write("id=" + str(user_test_id))
        # TestLog.close()

        keyboard_utils = KeyboardUtils()
        keyboard_utils.set_test_log_name(log_file)

        # Start recording
        GlobalVariables.toRec = 1
        # start the thread listener keyboard and mouse
        K_listener = KeyboardListener(on_press=keyboard_utils.keyboard_press)
        # M_listener = MouseListener(on_click=MouseUtils.mouse_click, on_scroll=MouseUtils.mouse_scroll)

        K_listener.start()
        # M_listener.start()

        K_listener.join()
        # M_listener.join()

        subprocess.Popen(["python", "Notification.py"])
