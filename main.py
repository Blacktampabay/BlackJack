from tkinter import Button, Frame, Label, LEFT, RIGHT
import tkinter as tk
import random
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Game on 21 points")
root.geometry("585x500")
root.resizable(False, False)

count = 0
deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_interface()
        self.image()
        self.deck_shuffle()
        self.reset_game()

    def reset_game(self):
        global count
        count = 0
        self.window_point.config(text="{}".format(count))

    def deck_shuffle(self):
        global count
        global deck
        random.shuffle(deck)
        current = deck.pop()
        count += current
        self.window_point.config(text="card %d" % current)
        self.window_point.config(text="{}".format(count))
        if count > 21:
            self.window_point.config(text="%d Lose" % count)
        elif count == 21:
            self.window_point.config(text="%d Win!" % count)
        else:
            self.window_point.config(text="%d " % count)

    def create_interface(self):
        self.f_top = Frame()
        self.f_bot = Frame()
        self.info = "0"
        self.window_point = Label(self.f_bot, text=self.info,
                                  font=("Times New Roman", 20),
                                  width=9)
        self.quit = Button(self.f_top, text="Rage Quit",
                           background="pink",
                           activebackground="tomato",
                           bd=2.3, width=39,
                           command=self.master.destroy)
        self.start = Button(self.f_bot, text="Yes, Let's go!",
                            background="lightgray",
                            activebackground="darkgray",
                            bd=2.3, command=lambda: self.deck_shuffle())
        self.stop = Button(self.f_bot, text="Go, again!",
                           background="lightgray",
                           activebackground="darkgray",
                           bd=2.3, command=lambda: self.reset_game())

        self.f_top.pack()
        self.f_bot.pack()
        self.start.pack(side=LEFT)
        self.quit.pack(side=RIGHT)
        self.window_point.pack(side=LEFT)
        self.stop.pack(side=LEFT)
        return self.f_bot, self.f_top

    def image(self):
        self.img = Image.open('Image.jpeg')
        self.render = ImageTk.PhotoImage(self.img)
        self.initil = tk.Label(root, image=self.render)
        self.initil.image = self.render
        self.initil.pack()


app = Application(master=root)
app.mainloop()
