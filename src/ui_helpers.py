# ==================== BUILT-IN MODULE ====================
import tkinter as tk

# ==================== UI HELPERS ====================

# Move the UI window to the center of the screen
def center_window(window, width, height):
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# Make UI window appear in the center of screen and on top of all windows
def appear_root_window(root):
    center_window(root, 900, 600)
    root.attributes("-topmost", True)
    root.lift()
    root.attributes("-topmost", False)


# Make LOG IN card have rounded corners to make it look like Facebook's real login page
def round_rect(canvas, x1, y1, x2, y2, radius=20, **kwargs):
    points = [
        x1+radius, y1, x2-radius, y1, x2, y1,
        x2, y1+radius, x2, y2-radius, x2, y2,
        x2-radius, y2, x1+radius, y2, x1, y2,
        x1, y2-radius, x1, y1+radius, x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

# ==================== ENTRY WITH PLACEHOLDER ====================
#       Custom Tkinter Entry widget that supports placeholder text.
#       Used to simulate Facebook's email and password entry boxes.
#       Features:
#           - Displays placeholder text when the field is empty
#           - Changes text color based on focus state
#           - Supports password masking when input is active
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", is_password=False, **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder  # Text
        self.is_password = is_password  # Determines if password masking is needed
        self.default_fg = "#a0a0a0"
        self.text_fg = "#1c1e21"

        self.insert(0, self.placeholder)
        self.config(fg=self.default_fg, show="")

        # Focus events that mimick Facebook's login page
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

    # When user is typing in boxes
    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.text_fg)
            if self.is_password:
                self.config(show="*")

    # When user is not typing in boxes
    def _on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.default_fg, show="")