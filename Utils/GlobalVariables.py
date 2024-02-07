# GlobalVariables.py
import os

text_here = "Magniv"
user_selector = 0
toRec = 0
last_time = 0
test_time = 0
start_time = 0
PicOption = 0
Remote_window_location = (100, 100)
Remote_window_size = (1366, 768)
RecordVsRun = 1
stop_flag = False
Web_GUI = True
Web_user_test_name = ""
Web_user_test_summary = ""
Web_diff = 0
Web_stepProcess = ""
Web_stepResult = ""
Web_stepComment = ""
Web_Critic = ""
listA = ['accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
         'browserback', 'browserfavorites', 'browserforward', 'browserhome',
         'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
         'convert', 'ctrl', 'ctrlright', 'decimal', 'del', 'delete',
         'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
         'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
         'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
         'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
         'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
         'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
         'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
         'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
         'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
         'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
         'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
         'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
         'command', 'option', 'optionleft', 'optionright']

# with open("D:/ElbitProjects/ATH/GIT/AutoTest/Setup/Setting.txt", "r") as SettingFile:  # read the setting parameters

current_dir = os.path.dirname(__file__)

with open(os.path.join(current_dir, r"../Setup/Setting.txt"), "r") as setting_file:  # read the setting parameters
    # Snap point dimensions
    lines = setting_file.readlines()
    top_left_x = int(lines[1].split(" ")[0])
    top_left_y = int(lines[2].split(" ")[0])
    bottom_right_x = int(lines[3].split(" ")[0])
    bottom_right_y = int(lines[4].split(" ")[0])

    # files name and path
    parent_dir_test = lines[8].split(" ")[0]
    parent_dir_result = lines[9].split(" ")[0]
    setting_f = lines[10].split(" ")[0]
    test_list_f = lines[11].split(" ")[0]
    general_result = lines[12].split(" ")[0]
    version_file = lines[13].split(" ")[0]
    noti_file = lines[14].split(" ")[0]
    rsn = lines[15].split(" ")[0]
    script_path = lines[16].split(" ")[0]

    # Status Window dimensions and location
    trs_l_x = int(lines[18].split(" ")[0])
    trs_l_y = int(lines[19].split(" ")[0])
    window_width = int(lines[20].split(" ")[0])
    window_height = int(lines[21].split(" ")[0])

    # difference to define fail
    difference_static = int(lines[25].split(" ")[1])
    difference_dynamic = int(lines[26].split(" ")[1])
    difference_extreme = int(lines[27].split(" ")[1])

    progress_bar_timing = int(lines[31].split(" ")[1])
    mouse_scroll = int(lines[32].split(" ")[1])
    # data for the installation
    site_to_open = lines[36].split(" ")[0]
    chrome_driver = lines[37].split(" ")[0]
    chrome_path = lines[38].split("    ")[0]
    # image threshold in the greyscale images compare
    image_threshold = int(lines[40].split(" ")[0])

    # image threshold  in the greyscale images compare
    doc_folder = lines[43].split(" ")[0]

    f6_top_left_x = int(lines[47].split(" ")[0])
    f6_top_left_y = int(lines[48].split(" ")[0])
    f6_bottom_right_x = int(lines[49].split(" ")[0])
    f6_bottom_right_y = int(lines[50].split(" ")[0])

    f7_ip = lines[53].split(" ")[0]
    f8_ip = lines[54].split(" ")[0]
    f9_ip = lines[55].split(" ")[0]

    word_app_path = lines[57].split(" ")[0]

    general_similarity = lines[59].split(" ")[0]


def main():
    print("Running Global_SettingV_Var.py directly")


if __name__ == "__main__":
    main()
