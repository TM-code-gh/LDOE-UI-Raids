from tkinter import *
from tkinter import ttk

class Raids(Frame):

    def __init__(self):
        super().__init__()
        self.initUi()


    def initUi(self):
        
        #Left panel
        frame_left = Frame(background='red')
        frame_left.place(relx=0, rely=0, relwidth=0.25, relheight=1)

        #Mid panel
        frame_mid = Frame(background="green")
        frame_mid.place(relx=0.25, rely=0, relwidth=0.5, relheight=1)

        #Right panel
        frame_right = Frame(background='blue')
        frame_right.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)


        #Inside mid panel
        #Inside mid Top panel
        frame_mid_top = Frame(frame_mid, background='yellow')
        frame_mid_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        label_base = Label(frame_mid_top, text='Base XXXXX')
        label_base.place(relx=0.5, rely=0.5, anchor=CENTER)


        #Inside left panel
        #Inside left Top panel
        frame_left_top = Frame(frame_left)
        frame_left_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)


        #Inside left mid panel
        frame_left_mid = Frame(frame_left)
        frame_left_mid.place (relx=0, rely=0.1, relwidth=1, relheight=0.8)

        tree = ttk.Treeview(frame_left_mid)
        tree.heading('#0', text='BDD des bases', anchor=W)
        tree.place(relx=0, rely=0, relwidth=1)







def main():

    root = Tk()
    root.title("Fenêtre de Raids")
    # width x height + x + y
    root.geometry('800x600+600+200')
    app = Raids()

    root.mainloop()


if __name__ == '__main__':
    main()