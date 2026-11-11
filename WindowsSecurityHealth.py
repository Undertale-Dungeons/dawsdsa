import tkinter as tk
from tkinter import ttk
import random

# Harmless visual-only prank. Does not scan, modify, encrypt, or access files.
BG = "#07111f"
PANEL = "#0d1b2a"
CYAN = "#38d9ff"
RED = "#ff5364"
GREEN = "#55e6a5"
WHITE = "#e8f1fa"
MUTED = "#8ea4b8"

root = tk.Tk()
root.title("Windows Security Center")
root.configure(bg=BG)
root.geometry("900x620")
root.minsize(760, 540)

# Escape always exits. Window is not forced above other apps or made persistent.
root.bind("<Escape>", lambda _event: root.destroy())

top = tk.Frame(root, bg="#10243a", height=54)
top.pack(fill="x")
top.pack_propagate(False)
tk.Label(top, text="◈  SECURITY CENTER", bg="#10243a", fg=WHITE,
         font=("Segoe UI", 14, "bold")).pack(side="left", padx=22)
tk.Label(top, text="LOCAL DEMO  •  SIMULATION", bg="#10243a", fg=CYAN,
         font=("Segoe UI", 9, "bold")).pack(side="right", padx=22)

main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=28, pady=24)

header = tk.Frame(main, bg=BG)
header.pack(fill="x")
tk.Label(header, text="Threat protection", bg=BG, fg=WHITE,
         font=("Segoe UI", 23, "bold")).pack(anchor="w")
tk.Label(header, text="Your device status overview", bg=BG, fg=MUTED,
         font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 18))

alert = tk.Frame(main, bg="#351923", highlightbackground="#7f2e40",
                 highlightthickness=1)
alert.pack(fill="x", pady=(0, 18))
tk.Label(alert, text="⚠", bg="#351923", fg=RED,
         font=("Segoe UI", 28, "bold")).pack(side="left", padx=18, pady=12)
alert_text = tk.Frame(alert, bg="#351923")
alert_text.pack(side="left", fill="x", expand=True, pady=12)
tk.Label(alert_text, text="Potential threats detected",
         bg="#351923", fg="#ffb7c0",
         font=("Segoe UI", 14, "bold")).pack(anchor="w")
tk.Label(alert_text, text="This is a visual-only prank simulation. No threats were found.",
         bg="#351923", fg="#e8cbd0",
         font=("Segoe UI", 9)).pack(anchor="w", pady=(3, 0))

cards = tk.Frame(main, bg=BG)
cards.pack(fill="x", pady=(0, 18))

def card(parent, title, value, sub, color=CYAN):
    box = tk.Frame(parent, bg=PANEL, highlightbackground="#1d3850",
                   highlightthickness=1)
    box.pack(side="left", fill="both", expand=True, padx=(0, 10))
    tk.Label(box, text=title.upper(), bg=PANEL, fg=MUTED,
             font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=15, pady=(14, 5))
    tk.Label(box, text=value, bg=PANEL, fg=color,
             font=("Segoe UI", 19, "bold")).pack(anchor="w", padx=15)
    tk.Label(box, text=sub, bg=PANEL, fg=MUTED,
             font=("Segoe UI", 8)).pack(anchor="w", padx=15, pady=(3, 14))
    return box

card(cards, "Protection status", "Attention", "Demo alert only", RED)
card(cards, "Last scan", "Not run", "No files are accessed", CYAN)
card(cards, "Firewall", "Enabled", "Display status only", GREEN)

scan_box = tk.Frame(main, bg=PANEL, highlightbackground="#1d3850",
                    highlightthickness=1)
scan_box.pack(fill="both", expand=True)
tk.Label(scan_box, text="QUICK SCAN", bg=PANEL, fg=WHITE,
         font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=18, pady=(16, 4))
status = tk.Label(scan_box, text="Ready to run visual demo",
                  bg=PANEL, fg=MUTED, font=("Segoe UI", 9))
status.pack(anchor="w", padx=18, pady=(0, 10))

progress = ttk.Progressbar(scan_box, mode="determinate", maximum=100, length=500)
style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", troughcolor="#172b3e", background=CYAN,
                bordercolor="#172b3e", lightcolor=CYAN, darkcolor=CYAN)
progress.pack(fill="x", padx=18, pady=(0, 14))

buttons = tk.Frame(scan_box, bg=PANEL)
buttons.pack(fill="x", padx=18, pady=(0, 16))

running = False
value = 0

def tick():
    global value
    if not running:
        return
    value = min(100, value + random.randint(3, 8))
    progress["value"] = value
    status.config(text=f"Simulated scan animation… {value}%  |  No files are being scanned")
    if value >= 100:
        status.config(text="Demo complete. No changes were made to your computer.")
        start_btn.config(state="normal")
        return
    root.after(180, tick)

def start_demo():
    global running, value
    if running:
        return
    running = True
    value = 0
    progress["value"] = 0
    start_btn.config(state="disabled")
    status.config(text="Starting visual-only animation…")
    tick()

def close_demo():
    root.destroy()

start_btn = tk.Button(buttons, text="Start demo scan", command=start_demo,
                       bg="#123d55", fg=WHITE, activebackground="#1b5875",
                       activeforeground=WHITE, relief="flat", padx=18, pady=9,
                       font=("Segoe UI", 9, "bold"), cursor="hand2")
start_btn.pack(side="left")
tk.Button(buttons, text="Exit prank", command=close_demo,
          bg="#263747", fg=WHITE, activebackground="#354b60",
          activeforeground=WHITE, relief="flat", padx=18, pady=9,
          font=("Segoe UI", 9, "bold"), cursor="hand2").pack(side="right")

footer = tk.Frame(root, bg="#10243a", height=34)
footer.pack(fill="x", side="bottom")
footer.pack_propagate(False)
tk.Label(footer, text="Harmless visual demo • Press ESC to close",
         bg="#10243a", fg="#9db2c5", font=("Segoe UI", 8)).pack(side="left", padx=22, pady=8)

root.mainloop()
