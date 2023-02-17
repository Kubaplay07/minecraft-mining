import pyautogui
import keyboard

mouse_held = False

def hold_mouse():
    global mouse_held
    mouse_held = True
    pyautogui.mouseDown()
    print("Left mouse button held")

def release_mouse():
    global mouse_held
    mouse_held = False
    pyautogui.mouseUp()
    print("Left mouse button released")

keyboard.add_hotkey('o', hold_mouse)
keyboard.add_hotkey('i', release_mouse)

print("Press 'o' to hold left mouse button, 'i' to release")
keyboard.wait()
