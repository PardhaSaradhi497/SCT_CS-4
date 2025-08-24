import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

LOG_FILE = "keystroke_log.txt"   

def write_header():
    start = f"\n--- Session start: {datetime.now().isoformat(sep=' ', timespec='seconds')} ---\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(start)
        f.flush()

def on_key(event):
    if event.char and ord(event.char) >= 32:
        key_str = event.char
    else:
        key_str = f"[{event.keysym}]"

    line = f"{datetime.now().isoformat(sep=' ', timespec='seconds')} {key_str}\n"
    print("Logged:", line.strip())   

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)
        f.flush()

    root.key_count += 1
    root.status_var.set(f"Keys logged: {root.key_count}  |  Log file: {os.path.abspath(LOG_FILE)}")

def clear_text():
    text.delete("1.0", tk.END)

def show_log_path():
    messagebox.showinfo("Log File", f"Saved to:\n{os.path.abspath(LOG_FILE)}")

root = tk.Tk()
root.title("Keystroke Logger (Safe - App Only)")
root.geometry("700x420")
root.key_count = 0

write_header()

# UI
tk.Label(root, text="Type here. Only keys inside this window are logged to file.",
         font=("Segoe UI", 11)).pack(pady=8)

text = tk.Text(root, wrap="word", font=("Consolas", 12), height=16)
text.pack(fill="both", expand=True, padx=12, pady=4)
text.focus_set()
text.bind("<Key>", on_key)

btns = tk.Frame(root)
btns.pack(pady=6)
tk.Button(btns, text="Clear Text", command=clear_text).pack(side="left", padx=6)
tk.Button(btns, text="Show Log Path", command=show_log_path).pack(side="left", padx=6)

root.status_var = tk.StringVar(value="Keys logged: 0")
tk.Label(root, textvariable=root.status_var, anchor="w").pack(fill="x", padx=12, pady=4)

root.mainloop()
