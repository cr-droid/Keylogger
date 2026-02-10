# ==================== SUPER CLASS ====================
class BaseLogger:
    def __init__(self):
        self.logs = []      # logs array for logging key/mouse entries

    # ==================== ADD ENTRY TO LOGS ====================
    def add(self, entry):
        self.logs.append(entry)

# ==================== SUB CLASS ====================
class InteractionLogger(BaseLogger):
    def __init__(self, file_manager):
        super().__init__()
        self.file_manager = file_manager

    # ==================== SAVE LOGS TO FILE ====================
    def save_all(self):
        self.file_manager.save(self.logs)