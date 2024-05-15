# pip install pyautogui | ONLY IF YOU DO NOT HAVE IT INSTALLED/CODE IS NOT WORKING
# pip install keyboard| ONLY IF YOU DO NOT HAVE IT INSTALLED/CODE IS NOT WORKING
import pyautogui
import keyboard

# HOTKEYS + LOCATIONS
key_coordinates = {
    'a': (685, 511),
    's': (779, 511),
    'd': (879, 511),
    'f': (979, 511),
    'g': (1079, 511),
    'h': (1139, 511),
    'i': (1259, 511)
}

# Click function
def click_at_coordinates(coordinates):
    pyautogui.rightClick(coordinates[0], coordinates[1])

# Hotkey registration and handling
def register_hotkeys():
    current_key = None
    while True:
        key_event = keyboard.read_event(suppress=True)
        if key_event.event_type == keyboard.KEY_DOWN:
            current_key = key_event.name
            if current_key in key_coordinates:
                coordinates = key_coordinates[current_key]
                pyautogui.moveTo(coordinates[0], coordinates[1])
                click_at_coordinates(coordinates)
            else:
                current_key = None

# Start hotkey registration
register_hotkeys()

# End when 'esc' is pressed
keyboard.wait('esc')
