from tkinter import filedialog, messagebox
from tkinter import *
from PIL import Image, ImageTk
import subprocess

class A_ctl:
    def __init__(self, window):
        self.window = window

    def home(self):
        self.window.destroy()
        subprocess.run(["python", "main.py"])

    def open_image(self):
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
        )
        if not file_path:
            return None

        img = Image.open(file_path)
        img = img.resize((480, 350), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
