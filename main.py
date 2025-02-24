from tkinter import *
import sqlite3
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
from creating_dataset import cd_main
from Prediction import pred_main
from Reverse_Recognition import rr_main

# ===================== Create Database =============================
def createdb():
    conn = sqlite3.connect('files/users_info.db')
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS users (name TEXT , passs TEXT, sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
    conn.commit()
    conn.close()

createdb()

# ===================== Tkinter Window ==============================
window2 = Tk()
window2.title("ISL")
window2.geometry("420x420+410+160")
window2.resizable(False, False)

# ===================== Load Indian Flag as Background ==========================
flag_image = Image.open("files/flag.png")  # Ensure "flag.png" is in the "files" folder
flag_image = flag_image.resize((420, 420))  # Resize to fit the window
bg_image = ImageTk.PhotoImage(flag_image)

bg_label = Label(window2, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set background

# ===================== Main Frame ==========================
f1 = Frame(window2, bd=5, relief="solid", bg="white")
f1.place(x=0, y=0, width=420, height=420)

label3 = Label(f1, text="Indian Sign Language", font=("arial", 20, "bold"), bg="orange", fg="white", relief=SUNKEN, bd=5)
label3.pack(side=TOP, fill=X)

# ===================== Animated GIF Class ==========================
class AnimatedGIF(Label):
    def __init__(self, master, path, forever=True):
        Label.__init__(self, master, bg="white")  # Keep white to blend with frame
        self._master = master
        self._loc = 0
        self._forever = forever
        self._is_running = False
        self._frames = []

        im = Image.open(path)
        try:
            while True:
                self._frames.append(ImageTk.PhotoImage(im.copy().convert('RGBA')))
                im.seek(len(self._frames))
        except EOFError:
            pass

        self._last_index = len(self._frames) - 1
        self._delay = im.info.get('duration', 100)
        self._callback_id = None

        self.configure(image=self._frames[0])

    def start_animation(self):
        if not self._is_running:
            self._is_running = True
            self._animate_GIF()

    def stop_animation(self):
        if self._is_running and self._callback_id:
            self.after_cancel(self._callback_id)
            self._callback_id = None
        self._is_running = False

    def _animate_GIF(self):
        if not self._is_running:
            return
        self._loc = (self._loc + 1) % len(self._frames)
        self.configure(image=self._frames[self._loc])
        self._callback_id = self.after(self._delay, self._animate_GIF)

# ===================== Load and Start GIF Animation ==========================
gif_label = AnimatedGIF(f1, "files/gif2.gif")
gif_label.pack(expand=True, fill=BOTH)
gif_label.start_animation()  # Ensuring animation starts

# ===================== Buttons (Centered) ==========================
btn3w2 = ttk.Button(f1, text="Translate Speech", command=rr_main)
btn3w2.place(relx=0.5, rely=0.55, anchor=CENTER, width=150, height=30)

btn9w2 = ttk.Button(f1, text="Exit", command=window2.destroy)
btn9w2.place(relx=0.5, rely=0.75, anchor=CENTER, width=150, height=30)

window2.mainloop()
