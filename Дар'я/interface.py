from tkinter import Entry, Tk, Label, Frame, Menu
from tkinter.ttk import Style, Button
import random 

col = ["red", "blue", "green", "white", "yellow"]
val = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
val_trans = random.randint(0, len(val))
n_bg = random.randint(0, len(col))
n_fg = random.randint(0, len(col))

title = "Моя програма"
WIDTH = 500
HEIGHT = 200
bg = col[n_bg]
fg = col[n_fg]
center = "center"

root = Tk()
frame = Frame(root, width=WIDTH, height=HEIGHT, bg=bg)
skills_list = []


class Window:

    def __init__(self, frame, root):
        self.root = root
        self.frame = frame

    def clear(self):
        if self.frame.winfo_children():
            for i in self.frame.winfo_children():
                self.frame.winfo_children()[0].destroy()

    def create_window(self):
        win = self.root
        transparency = val[val_trans]
        width = WIDTH
        height = HEIGHT

        root.title(title)
        root.wait_visibility(win)
        root.wm_attributes('-alpha', transparency)
        root.minsize(width, height)
        root.resizable(width=False, height=False)
        root.configure(background=bg)

        style = Style()
        style.configure("BW.TButton", foreground=fg, background=bg, relief='groove')

    def create_button(self, title, move, x, y):
        button = Button(self.frame, text=title, style="BW.TButton", command=move)
        button.place(relx = x, rely = y, anchor='center')

    def create_label(self, Text, x, y, align=center):
        label = Label(self.frame, text=Text, fg=fg, bg=bg)
        label.place(relx = x, rely = y, anchor=align)
   
    def create_entry(self, txt, btn_txt, x, y):
        self.entry = Entry(self.frame, fg=fg, bg=bg, width=20)
        self.entry.insert(0, txt)
        self.entry.place(relx = x, rely = y, anchor='center')
        self.create_button(btn_txt, self.get_entry, x + .4, y)
        

class MainWindow(Window):

    def __init__(self, frame, root):
        super().__init__(frame, root)

    def main(self):
        self.menu()
        
        MB = Menu(self.root)
        MN = Menu(MB)

        MN.add_command(label=u"Admin", command=self.window_1)
        MN.add_command(label=u"Settings", command=self.window_2)
        MN.add_command(label=u"Menu", command=self.menu)

        self.frame.pack()
        
        root.focus_force()
        root.mainloop()
    
    def menu(self):
        self.clear()

        self.create_label("Назва: %s" % title, .5, .1)

        self.create_button("Кнопка", self.window_1, .5, .7)
        self.create_button("Кнопка", self.window_2, .5, .8)

    
    def window_1(self):
        self.clear()

        self.create_label("Вікно один", .5, .1)

        self.create_button("Назад", self.main, .5, .9)    

    def window_2(self):
        self.clear()

        self.create_label("Вікно два", val[val_trans], .1)

        self.create_button("Назад", self.menu, val[val_trans], .9)


if __name__ == "__main__":
    GameWindow = MainWindow(frame, root)
    GameWindow.create_window()
    GameWindow.main()

    root.mainloop()
