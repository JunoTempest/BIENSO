import tkinter as tk
from View.mainview import Mainview
from Controller.ctl import A_ctl

if __name__ == "__main__":
    window = tk.Tk()
    controller = A_ctl()
    app = Mainview(window, controller)
    window.mainloop()
