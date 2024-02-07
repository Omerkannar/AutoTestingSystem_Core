# MouseUtils.py
from . import Listener
from . import GlobalVariables


# input:
#   x = integer - mouse X location
#   y = integer - mouse Y location
#   button = string - type of button
#   press = bool - press= true , release = false
# what does it do: write the "TestLog" the mouse location + button type + if press or release with running time
# output: none
def mouse_click(x, y, button, pressed, file_pointer):
    if GlobalVariables.toRec == 1:
        # OmerK - Fix function parameters for listener_mouse_click
        Listener.listener_mouse_click(x, y, button, pressed, GlobalVariables.start_time, GlobalVariables.last_time, file_pointer)
    else:
        pass


# input:
#   x = integer - mouse X location
#   y = integer - mouse Y location
#   dx = integer - number of click in scroll
#   dy = integer - scroll direction 1 = up , -1 = down  with running time
# what does it do: write the "TestLog" the mouse scroll operation
# output: none
def mouse_scroll(x, y, dx, dy, file_pointer):
    if toRec == 1:
        Listener.listener_mouse_scroll(x, y, dx, dy, GlobalVariables.start_time, GlobalVariables.last_time, file_pointer)
    else:
        pass
