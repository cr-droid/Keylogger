class FileManager:
    def __init__(self, filename):
        self.filename = filename    # File that saves output
    
    # Output to file (for keyboard and mouse click logging)
    def save(self, data):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                for entry in data:
                    # Check if entry is a tuple (key, timestamp)
                    if isinstance(entry, tuple):
                        f.write(f"[{entry[1]}] {entry[0]}\n")
                    else:
                        f.write(str(entry) + "\n")
        except Exception as error:
            print("File error:", error)

    # Output to file without overwriting data (for process_key function)
    def save_without_overwrite(self, data):
        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                for entry in data:
                    # Check if entry is a tuple (key, timestamp)
                    if isinstance(entry, tuple):
                        f.write(f"[{entry[1]}] {entry[0]}\n")
                    else:
                        f.write(str(entry) + "\n")
        except Exception as error:
            print("File error:", error)