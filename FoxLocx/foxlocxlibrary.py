import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import datetime, time as dt_time
import threading

class LockScreenApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("FoxLocx")

        self.locked = False
        self.lock_duration = 15 * 60  # Default lock duration is 15 minutes
        # make max lock duration 8 hours!!
        self.current_lock_duration = 0
        self.lock_time = None
        self.lock_image_path = ""

        self.create_widgets()

    def create_widgets(self):
        self.lock_label = tk.Label(self.master, text="FoxLocx", font=("Helvetica", 36))
        self.lock_label.pack(pady=20)

        self.timer_label = tk.Label(self.master, text="", font=("Helvetica", 36))
        self.timer_label.pack(pady=20)

        self.lock_button = tk.Button(self.master, text="Lock screen now", command=self.lock_screen)
        self.lock_button.pack(pady=10)

        self.set_lock_time_button = tk.Button(self.master, text="Set lock time", command=self.set_lock_time)
        self.set_lock_time_button.pack(pady=10)

        self.set_lock_screen_button = tk.Button(self.master, text="Set lock screen background", command=self.set_lock_screen)
        self.set_lock_screen_button.pack(pady=10)

        self.change_time_format_button = tk.Button(self.master, text="Change time format", command=self.change_time_format)
        self.change_time_format_button.pack(pady=10)

        self.exit_button = tk.Button(self.master, text="Exit FoxLocx", command=self.master.destroy)
        self.exit_button.pack(pady=10)

    def lock_screen(self):
        if not self.locked:
            self.locked = True
            self.current_lock_duration = self.lock_duration
            self.master.attributes("-topmost", True)
            self.master.iconify()  #minimize

            # To-Do make timer
            self.update_timer()

    def update_timer(self):
        if self.locked:
            self.current_lock_duration -= 1
            minutes, seconds = divmod(self.current_lock_duration, 60)
            timer_text = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=timer_text)

            if self.current_lock_duration <= 0:
                self.unlock_screen()
                return

            self.master.after(1000, self.update_timer)

    def unlock_screen(self):
        self.locked = False
        self.timer_label.config(text="")
        self.master.attributes("-topmost", False)
        self.master.deiconify()  # Restore

    def set_lock_time(self):
        # To-DO button set user-specified lock time
        pass

    def set_lock_screen(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.lock_image_path = file_path
            # Load and display the selected image
            image = Image.open(file_path)
            image = image.resize((400, 400), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.lock_label.config(image=photo)
            self.lock_label.image = photo

    def change_time_format(self):
        # To-Do button to change the time format
        pass