import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui
import webbrowser

# --- Functions ---

def start_typing():
    global typing
    typing = True
    status_label.config(text="Status: Typing...")
    # Run typing in a separate thread to keep GUI responsive
    typing_thread = threading.Thread(target=auto_type)
    typing_thread.start()

def stop_typing():
    global typing
    typing = False
    status_label.config(text="Status: Stopped")

def auto_type():
    text = input_text.get("1.0", tk.END)
    try:
        delay = float(delay_entry.get())
    except ValueError:
        delay = 0.05  # default delay
    # Wait 3 seconds so user can focus desired window
    for i in range(3, 0, -1):
        status_label.config(text=f"Status: Typing starts in {i}...")
        time.sleep(1)
    status_label.config(text="Status: Typing...")
    for char in text:
        if not typing:
            break
        pyautogui.typewrite(char)
        time.sleep(delay)
    status_label.config(text="Status: Done or Stopped")

def open_channel():
    webbrowser.open_new("https://www.youtube.com/@mrhaycker")

# --- Main GUI ---

root = tk.Tk()
root.title("Auto Typing Tool by @mrhaycker")
root.geometry("500x400")

# Text input
tk.Label(root, text="Type or paste your text here:").pack()
input_text = tk.Text(root, height=8, width=58)
input_text.pack(pady=5)

# Delay input
tk.Label(root, text="Typing Delay (seconds, e.g. 0.05):").pack()
delay_entry = tk.Entry(root)
delay_entry.insert(0, "0.05")
delay_entry.pack(pady=5)

# Start/Stop buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
start_btn = tk.Button(button_frame, text="Start Typing", command=start_typing, bg="lightgreen")
start_btn.pack(side="left", padx=10)
stop_btn = tk.Button(button_frame, text="Stop", command=stop_typing, bg="tomato")
stop_btn.pack(side="left", padx=10)

# Status label
status_label = tk.Label(root, text="Status: Waiting")
status_label.pack(pady=10)

# Channel link in footer
footer = tk.Label(root, text="Subscribe: @mrhaycker", fg="blue", cursor="hand2")
footer.pack(side="bottom", pady=10)
footer.bind("<Button-1>", lambda e: open_channel())

# Typing flag global
typing = False

root.mainloop()