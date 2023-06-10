from tkinter import *
from tkinter import ttk
import mysql.connector

import DB_access

class Raids(Frame):

    def __init__(self):
        super().__init__()
        self.initUi()
        

    def initUi(self):

        #SQL connection
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user=DB_access.user,
            password=DB_access.password,
            database='base_raids')
        
        cur = connection.cursor()
        query = "SELECT * FROM noname_1"
        cur.execute(query)
        

        #Left panel
        #frame_left = Frame(background='red')
        self.frame_left = Frame()
        self.frame_left.place(relx=0, rely=0, relwidth=0.15, relheight=1)

        #Mid panel
        #frame_mid = Frame(background="green")
        self.frame_mid = Frame()
        self.frame_mid.place(relx=0.15, rely=0, relwidth=0.60, relheight=1)

        #Right panel
        #frame_right = Frame(background='blue')
        self.frame_right = Frame()
        self.frame_right.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)


        #Inside left panel
        #Inside left Top panel
        self.frame_left_top = Frame(self.frame_left, highlightbackground="black", highlightthickness=1)
        self.frame_left_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.search_left = Entry(self.frame_left_top)
        self.search_left.pack(padx=20, pady=20)

        self.button_search_left = Button(self.frame_left_top, text='Chercher')
        self.button_search_left.place(relx=0.35, rely=0.6)

        #Inside left mid panel
        self.frame_left_mid = Frame(self.frame_left, highlightbackground="black", highlightthickness=1)
        self.frame_left_mid.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)

                            ### Treeview ###
        tree = ttk.Treeview(self.frame_left_mid)
        tree.heading('#0', text='BDD des bases', anchor=W)
        tree.place(relx=0, rely=0, relwidth=1)

        for RaidsID in cur:
            tree.insert('', END,text= RaidsID, open=False)

        cur.close()
        connection.close()
                            ### Treeview ###


        #Inside mid panel
        #Inside mid Top panel
        #frame_mid_top = Frame(frame_mid, background='yellow')
        self.frame_mid_top = Frame(self.frame_mid, highlightbackground="black", highlightthickness=1)
        self.frame_mid_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.label_base = Label(self.frame_mid_top, text='Base XXXXX')
        self.label_base.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Inside mid mid panel
        self.frame_mid_mid = Frame(self.frame_mid, highlightbackground="black", highlightthickness=1)
        self.frame_mid_mid.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)

        self.canvas_mid = Canvas(self.frame_mid_mid, bg='dark sea green')
        self.canvas_mid.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

        self.canvas_mid.update()
        width = int(self.canvas_mid.winfo_width())-4
        height = int(self.canvas_mid.winfo_height())-4

        for i in range(1,20):
            for k in range(1,20):
                x0 = (k)*(width/20)+2
                y0 = (i)*(height/20)+2
                x1 = (k+1)*(width/20)+2
                y1 = (i+1)*(height/20)+2

                if(i != 19):
                    if(k != 19):
                        rec = self.canvas_mid.create_rectangle(x0,y0,x1,y1, fill='#8fbc8f', activefill="red", width=0)
                        self.canvas_mid.tag_bind(rec, '<Button-1>', self.rec_click_event)
                        #Horizontal 
                        ligne = self.canvas_mid.create_line(x0,y0,x1,y0,dash=[2,4], width=3, activefill='black', activewidth=6)
                        self.canvas_mid.tag_bind(ligne, '<Button-1>', self.ligne_ckick_event)
                    #Vertical
                    ligne = self.canvas_mid.create_line(x0,y0,x0,y1,dash=[2,4], width=3, activefill='black', activewidth=6)
                    self.canvas_mid.tag_bind(ligne, '<Button-1>', self.ligne_ckick_event)

                else:
                    if(k != 19):
                        #Bottom
                        ligne = self.canvas_mid.create_line(x0,y0,x1,y0,dash=[2,4], width=3, activefill='black', activewidth=6)
                        self.canvas_mid.tag_bind(ligne, '<Button-1>', self.ligne_ckick_event)
                    

        #Inside right panel
        #Inside right top panel
        self.frame_right_top = Frame(self.frame_right, highlightbackground="black", highlightthickness=1)
        self.frame_right_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.search_right = Entry(self.frame_right_top)
        self.search_right.pack(padx=20, pady=20)

        self.button_search_right = Button(self.frame_right_top, text='Chercher')
        self.button_search_right.place(relx=0.35, rely=0.6)

    
    def rec_click_event(self, event):
        list_colors = ['#8fbc8f','#E8A857','#AC8C6A','#5E534F','#795A4C']
        
        item = event.widget.find_closest(event.x, event.y)
        #print(item, 'rec')
        color = self.canvas_mid.itemcget(item, "fill")
        ind_color = list_colors.index(color)

        if (ind_color==len(list_colors)-1):
            new_indice = 0
        else:
            new_indice = ind_color+1

        self.canvas_mid.itemconfigure(item, fill=list_colors[new_indice])


    def ligne_ckick_event(self, event):
        list_colors = ['black','#E8A857','#AC8C6A','#5E534F','#795A4C']

        item = event.widget.find_closest(event.x, event.y)
        #print(item, 'ligne')
        color = self.canvas_mid.itemcget(item, "fill")
        ind_color = list_colors.index(color)

        if (ind_color==len(list_colors)-1):
            new_indice = 0
        else:
            new_indice = ind_color+1

        self.canvas_mid.itemconfigure(item, fill=list_colors[new_indice])


def main():

    root = Tk()
    root.title("Fenêtre de Raids")
    # Width x Height + X + Y
    root.geometry('1200x800+400+80')
    app = Raids()

    root.mainloop()


if __name__ == '__main__':
    main()