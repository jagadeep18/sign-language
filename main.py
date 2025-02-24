from tkinter import Tk as IndianSignLanguage, Frame, Label, SUNKEN, W, BOTTOM, TOP, X
from tkinter import ttk
from PIL import Image, ImageTk

# Post Login Window
window2 = IndianSignLanguage()
window2.geometry("400x400+420+170")
window2.resizable(False, False)

f1 = Frame(window2)
f2 = Frame(window2)
f3 = Frame(window2)
f4 = Frame(window2)

for frame in (f1, f2, f3, f4):
    frame.place(x=0, y=0, width=400, height=400)

def swap(frame):
    frame.tkraise()

class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever
        self._is_running = False
        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)
                i += 1
                im.seek(i)
        except EOFError:
            pass
        self._last_index = len(self._frames) - 1
        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100
        self._callback_id = None
        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running: return
        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])
        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running: return
        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None
        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])
        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()
        super(AnimatedGIF, self).pack(**kwargs)

# Adding Background Animation
bg_animation = AnimatedGIF(f1, "files/gif2.gif")
bg_animation.pack()
bg_animation.start_animation()

label3 = Label(f1, text="User Panel", font=("arial", 20, "bold"), bg="grey16", fg="white", relief=SUNKEN)
label3.pack(side=TOP, fill=X)

# Main Buttons
btn3w2 = ttk.Button(f1, text="Translate speech")
btn3w2.place(x=125, y=150, width=150, height=30)

btn9w2 = ttk.Button(f1, text="Exit", command=window2.destroy)
btn9w2.place(x=125, y=200, width=150, height=30)

f1.tkraise()
window2.mainloop()
