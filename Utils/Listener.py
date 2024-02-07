# Listener.py

import time


# input:
#   x = integer - mouse X location
#   y = integer - mouse Y location
#   button = string - type of button
#   press = bool - press= true , release = false
# what does it do: write the "file" the mouse location + button type + if press or release with running time
# output: none
def listener_mouse_click(x, y, button, pressed, start_time, last_time, file_pointer):
    if pressed:
        total_time = time.time() - start_time
        gap_time = round(total_time - last_time, 4)
        file_pointer.writelines(str(gap_time) + ' mouse down at ({0},{1}) with {2} \n'.format(x, y, button))

    if not pressed:
        total_time = time.time() - start_time
        gap_time = round(total_time - last_time, 4)
        file_pointer.writelines(str(gap_time) + ' mouse up at ({0},{1}) with {2} \n'.format(x, y, button))

    last_time = total_time

    return last_time


# input:
#   x = integer - mouse X location
#   y = integer - mouse Y location
#   dx = integer - number of click in scroll
#   dy = integer - scroll direction 1 = up , -1 = down  with running time
# what does it do: write the "file" the mouse scroll operation
# output: none
def listener_mouse_scroll(x, y, dx, dy, start_time, last_time, file_pointer):
    total_time = time.time() - start_time
    gap_time = round(total_time - last_time, 4)
    file_pointer.writelines(str(gap_time) + ' scrolled at ({0},{1}), ({2},{3}) \n'.format(x, y, dx, dy))
    last_time = total_time

    return last_time


# input: key = string - keyboard mouse X operation
# what does it do: in case ESC was p press change the Global_Setting_Var.terminate to 1 else
# write the "ATRLogfilePointer" the keyboard click with running time output: none
def listener_keyboard_press(key, start_time, last_time, file_pointer):
    total_time = time.time() - start_time
    gap_time = round(total_time - last_time, 4)
    file_pointer.writelines(str(gap_time) + ' keyboard pressed with {0} \n'.format(key))
    last_time = total_time

    return last_time


def close_file(file):
    file.close()
