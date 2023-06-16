import tkinter


# bibliotek do aplikacji okienkowych

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label2 = tkinter.Label(self.main_window, text="Program w Pythonie")
        self.label3 = tkinter.Label(self.main_window, text="Góra")
        self.label4 = tkinter.Label(self.main_window, text="Dół")

        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='top')
        self.label4.pack(side='bottom')

        tkinter.mainloop()


my_gui = MyGui()
