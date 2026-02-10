# ==================== BUILT-IN MODULES ====================
from datetime import datetime
from pynput import keyboard

# Inputhandlers for keyboard strokes and mouse clicks
class InputHandlers:
    # ==================== CONSTRUCTOR ====================
    def __init__(self, logger, organized_file, status_label):
        self.logger = logger                    # Saves to logs.txt
        self.organized_file = organized_file    # Saves to organized_keys.txt
        self.status_label = status_label        # Status of logger on UI
        self.current_sentence = ""


    # ==================== KEY ORGANIZER ====================
    #       Logs & organizes the key that was pressed, along with a timestamp. 
    #       Output is saved to organized_keys.txt
    def organize_keys(self, key_entry, timestamp):
        # Ignore mouse clicks
        if not key_entry.startswith("KEY:"):
            return

        # Normalize key entry
        key_value = key_entry.replace("KEY:", "").strip()
        key_upper = key_value.upper()

        # Ignore special keys
        if key_upper.startswith("KEY."):
            return

        # Determine how to organize & save SPACE, BACKSPACE, ENTER key entries
        if key_upper == "SPACE":
            self.current_sentence += " "
        elif key_upper == "BACKSPACE":
            self.current_sentence = self.current_sentence[:-1]
        elif key_upper == "ENTER":
            if self.current_sentence.strip():
                self.organized_file.save_without_overwrite([f"[{timestamp}] {self.current_sentence.strip()}"])
            self.current_sentence = ""
        # Organize & save normal keys (letters, numbers, symbols)
        else:
            self.current_sentence += key_value
            self.organized_file.save_without_overwrite([f"[{timestamp}] {key_value}"])


    # ==================== KEYBOARD ====================
    #       Logs the key that was pressed, along with a timestamp. 
    #       Output is saved to logs.txt
    def on_key_press(self, key):
        try:
            # Handle normal characters (letters, numbers, symbols)
            if hasattr(key, "char") and key.char:
                entry = f"KEY: {key.char}"
            # Handle special keys (space, enter, backspace, Ctrl, Shift, Alt, etc.)
            elif key == keyboard.Key.space:
                entry = "KEY: SPACE"
            elif key == keyboard.Key.enter:
                entry = "KEY: ENTER"
            elif key == keyboard.Key.backspace:
                entry = "KEY: BACKSPACE"
            else:
                entry = f"KEY: {key}"

            # Create timestamp (millisecond precision)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

            # Save output
            self.logger.add((entry, timestamp))
            self.logger.save_all()

            # Organize and save normal keys
            self.organize_keys(entry, timestamp)

            # Display status of logger in UI
            self.status_label.config(text=f"Live input: {entry}")
        except Exception as error:
            print("Keyboard error:", error)


    # ==================== MOUSE ====================
    #       Logs the mouse click position and button used, 
    #       along with a timestamp. Output is saved to logs.txt
    def on_click(self, x, y, button, pressed):
        if not pressed:
            return

        # Create timestamp (millisecond precision)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        # Create log entry for mouse click
        entry = f"MOUSE CLICK at ({x},{y}) with {button}"

        #Save output
        self.logger.add((entry, timestamp))
        self.logger.save_all()

        # Display status of logger in UI
        self.status_label.config(text="Mouse activity detected")

    
    # ==================== SAVE OUTPUT BEFORE CLOSING PROGRAM ====================
    #       Helps end_program properly save keys onto organized_keys.txt
    def flush_sentence(self):
        if self.current_sentence.strip():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            self.organized_file.save_without_overwrite([f"[{timestamp}] {self.current_sentence.strip()}"])
            self.current_sentence = ""