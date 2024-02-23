# PrepareTest.py
import os
import subprocess
import threading
from datetime import datetime
from Utils import GlobalVariables, Utils
# from Utils import KeyboardUtils, MouseUtils
from Utils.KeyboardUtils import KeyboardUtils
from Utils.MouseUtils import MouseUtils
import pyautogui
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key
from pynput import keyboard, mouse
import time


class PrepareTest:
    def __init__(self):
        self.id = -1
        self.name = "na"
        self.last_key = "na"
        self.file_image_name = "na"
        self.file_image_number = 0


    def set_test_id(self, test_id) -> None:
        self.id = test_id

    def get_test_id(self) -> int:
        return self.id

    def set_test_name(self, test_name) -> None:
        self.name = test_name

    def get_test_name(self) -> str:
        return self.name

    def set_file_image_name(self, name):
        self.file_image_name = name

    def get_file_image_name(self):
        return self.file_image_name

    def set_file_image_number(self, number):
        self.file_image_number = number

    def get_file_image_number(self):
        return self.file_image_number

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
        # self.set_file_image_name(os.path.join(test_path, self.name))
        # print(self.get_file_image_name())
        # log_file.write("id=" + str(user_test_id))
        # TestLog.close()

        keyboard_utils = KeyboardUtils()
        keyboard_utils.set_test_log_name(log_file)
        keyboard_utils.set_file_image_path(os.path.join(test_path, self.name))

        mouse_utils = MouseUtils()
        mouse_utils.set_test_log_name(log_file)

        # Start recording
        GlobalVariables.toRec = 1

        stop_keyboard_listener = False

        # # Keyboard events:
        # with keyboard.Events() as kb_events:
        #     for event in kb_events:
        #         if event.__class__ == keyboard.Events.Press:
        #             print('Received event {}'.format(event))
        #             keyboard_utils.keyboard_press(event.key)
        #
        #
        # # Mouse events:
        # with mouse.Events() as mouse_events:
        #     for event in mouse_events:
        #         # if event.__class__ == mouse.Events.Click:
        #         print('Received event {}'.format(event))
        #         mouse_utils.mouse_click(event.x, event.y, event.button, event.pressed)

        # def checkMouseEvents():
        #     with mouse.Events() as mouseEvents:
        #         mouseEvent = mouseEvents.get(0.1)
        #         if mouseEvent is not None:
        #             if "Click" in str(mouseEvent):
        #                 print('Received event {}'.format(mouseEvent))
        #                 mouse_utils.mouse_click(mouseEvent.x, mouseEvent.y, mouseEvent.button, mouseEvent.pressed)
        #
        # def checkKeyboardEvents():
        #     with keyboard.Events() as keyboardEvents:
        #         keyboardEvent = keyboardEvents.get(0.1)
        #         if keyboardEvent is not None:
        #             if "Press" in str(keyboardEvent):
        #                 print('Received event {}'.format(keyboardEvent))
        #                 return keyboard_utils.keyboard_press(keyboardEvent.key)
        #             # elif "Release" in str(keyboardEvent):
        #             #     on_release()
        #
        # while True:
        #     # time.sleep(0.05)
        #     key = checkKeyboardEvents()
        #     print(key)
        #     checkMouseEvents()

        # start the thread listener keyboard and mouse
        K_listener = KeyboardListener(on_press=keyboard_utils.keyboard_press)
        # M_listener = MouseListener(on_click=mouse_utils.mouse_click, on_scroll=mouse_utils.mouse_scroll)
        M_listener = MouseListener(on_click=mouse_utils.mouse_click)

        K_listener.start()
        M_listener.start()

        # K_listener.join()
        # M_listener.join()

        last_key = str(keyboard_utils.get_last_pressed_key())

        while True:
            # print("last key pressed = {0}, get_last_pressed_key() = {1}", last_key, keyboard_utils.get_last_pressed_key())
            if log_file.closed:
                K_listener.stop()
                M_listener.stop()

            # if str(keyboard_utils.get_last_pressed_key()) is not last_key:
            #     last_key = str(keyboard_utils.get_last_pressed_key())
            #     print("last key pressed: " + last_key)
            #     keyboard_utils.set_last_pressed_key(last_key)
            #     if last_key == "Key.f6":
            #         pass
            #         # self.set_file_image_number(self.get_file_image_number() + 1)
            #     if last_key == "Key.esc":
            #         K_listener.stop()
            #         M_listener.stop()
            #         keyboard_utils.terminate_create_test()

    # print("Prepare Test, Last pressed key = " + keyboard_utils.get_last_pressed_key())

    # subprocess.Popen(["python", "Notification.py"])
