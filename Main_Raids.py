from tkinter import *
from tkinter import ttk, tix
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
        self.button_search_left.place(relx=0.5, rely=0.75, anchor=CENTER)

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

        self.canvas_mid.place(relx=0.01, rely=0.01, relheight='', relwidth='', width=int(self.canvas_mid.winfo_width()), height=int(self.canvas_mid.winfo_height()))
        self.canvas_mid.update()

        #Création ligne/Rectangle
        for y in range(1,20):
            for x in range(1,20):
                x0 = (x)*(width/20)+2
                y0 = (y)*(height/20)+2
                x1 = (x+1)*(width/20)+2
                y1 = (y+1)*(height/20)+2

                #Rectangle
                if(x in range(13,17)) and (y in range(14, 19)):
                    #rec = self.canvas_mid.create_rectangle(x0,y0,x1,y1, fill='#EF9A9A', width=0)
                    rec = self.canvas_mid.create_rectangle(x0,y0,x1,y1, fill='blue', width=0)

                else:
                    if((x != 19) and (y != 19)):
                        rec = self.canvas_mid.create_rectangle(x0,y0,x1,y1, fill='#8fbc8f', width=0 , activefill="red", tag='rec')
                        self.canvas_mid.tag_bind(rec, '<Button-1>', self.item_left_click)
                        self.canvas_mid.tag_bind(rec, '<Enter>', self.evenement_entrer)
                        self.canvas_mid.tag_bind(rec, '<Leave>', self.evenement_sortir)

                #Ligne
                if(x != 19): #Ne pas avoir la colonne de droite
                    if (x not in range(13,17)) or (y not in range(15,20)): #Ne pas avoir les lignes inconstructibles
                        #Horizontal 
                        ligne_horizontale = self.canvas_mid.create_line(x0,y0,x1,y0, dash=[2,4], fill="white", width=3, activefill='black', activewidth=6, tag='ligne_horizontale')
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Button-1>', self.item_left_click)
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Enter>', self.evenement_entrer)
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Leave>', self.evenement_sortir)
                
                if(y != 19): #Ne pas avoir la ligne du bas
                    if (x not in range(14,17)) or (y not in range(14,20)): #Ne pas avoir les lignes inconstructibles
                        #Vertical
                        ligne_verticale = self.canvas_mid.create_line(x0,y0,x0,y1,dash=[2,4], fill="white", width=3, activefill='black', activewidth=6, tag='ligne_verticale')
                        self.canvas_mid.tag_bind(ligne_verticale, '<Button-1>', self.item_left_click)
                        self.canvas_mid.tag_bind(ligne_verticale, '<Enter>', self.evenement_entrer)
                        self.canvas_mid.tag_bind(ligne_verticale, '<Leave>', self.evenement_sortir)
        
        #Permet de passer l'objet et le type d'objet sélectionné
        self.item = 'None'
        self.item_type = 'None'


        #Inside right panel
        #Inside right top panel
        self.frame_right_top = Frame(self.frame_right, highlightbackground="black", highlightthickness=1)
        self.frame_right_top.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.search_right = Entry(self.frame_right_top)
        self.search_right.pack(padx=20, pady=20)

        self.button_search_right = Button(self.frame_right_top, text='Chercher')
        self.button_search_right.place(relx=0.5, rely=0.75, anchor=CENTER)

        #Inside right mid panel
        self.frame_right_mid = Frame(self.frame_right, highlightbackground="black", highlightthickness=1)
        self.frame_right_mid.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
        
        #Button
        self.frame_right_mid_buttons()



    def frame_right_mid_buttons(self):
        """
        Création bouton dans la frame right mid
        """
        for widgets in self.frame_right_mid.winfo_children():
            widgets.destroy()

        Button(self.frame_right_mid, text="Tout", command=lambda :self.need_def("Tout")).place(x=0, y=0, relwidth=1, height=50)
        Button(self.frame_right_mid, text="Sols & Murs", command=lambda :self.need_def("Sols & Murs")).place(x=0, y=50, relwidth=1, height=50)
        Button(self.frame_right_mid, text="Sols", command=lambda :self.need_def("Sols")).place(x=0, y=100, relwidth=1, height=50)
        Button(self.frame_right_mid, text="Murs", command=lambda :self.need_def("Murs")).place(x=0, y=150, relwidth=1, height=50)
        Button(self.frame_right_mid, text="Stockages", command=lambda :self.need_def("Stockages")).place(x=0, y=200, relwidth=1, height=50)
        Button(self.frame_right_mid, text="Établis", command=lambda :self.need_def("Établis")).place(x=0, y=250, relwidth=1, height=50)
        Button(self.frame_right_mid, text="Décorations", command=lambda :self.need_def("Décorations")).place(x=0, y=300, relwidth=1, height=50)
        Button(self.frame_right_mid, text="Autres", command=lambda :self.need_def("Autres")).place(x=0, y=350, relwidth=1, height=50)

        """list_text = []
        for x in self.frame_right_mid.winfo_children():
            list_text.append(x.cget('text'))

        print(list_text)"""


    #FIXME
    def need_def(self, button_txt):
        """
        Spprime bouton + appelle fct creation bouton
        """
        print('clicked:', button_txt)   #print(x.cget('text'))

        for widgets in self.frame_right_mid.winfo_children():
            widgets['state'] = DISABLED #Désactive bouton
            widgets.destroy()
            

        Button(self.frame_right_mid, text='<-', command=self.frame_right_mid_buttons).place(x=0, y=0, relwidth=0.25, height=40)
        Label(self.frame_right_mid, text=button_txt, borderwidth=1, relief='solid').place(relx=0.25, y=0, relwidth=0.5, height=40)

        self.create_button_dessin(button_txt)


    def create_button_dessin(self, button_txt):
        """
        Creer bouton en fct du type d'objet voulu (sol/murs/stockages/...)
        """

        Label(self.frame_right_mid, text=button_txt).place(relx=0, y=50, relwidth=1, height=40)
        Button(self.frame_right_mid, text='^^').place(relx=.80, y=17+50, relwidth=0.1, height=15)
        Label(self.frame_right_mid, text='', borderwidth=1, relief="solid").place(relx=0, y=80, relwidth=1, height=2)

        self.frame_mid_mid_sols = Frame(self.frame_right_mid, highlightbackground="black", highlightthickness=1).place(relx=0, y=80+1, relwidth=1, height=140)
        
        if(button_txt=='Sols'):
            print('dessin sol')
            
            for k in range(6):
                if (k < 3):
                    Button(self.frame_right_mid, text='sol '+str(k)).place(relx=k/3, y=50+50, relwidth=0.25, height=40)
                else:
                    Button(self.frame_right_mid, text='sol '+str(k)).place(relx=(k-3)/3, y=100+50, relwidth=0.25, height=40)
            """
            Button(self.frame_right_mid, text='sol 0').place(relx=0, y=50+50, relwidth=0.25, height=40)
            Button(self.frame_right_mid, text='sol 1').place(relx=1/3, y=50+50, relwidth=0.25, height=40)
            Button(self.frame_right_mid, text='sol 2').place(relx=2/3, y=50+50, relwidth=0.25, height=40)
            Button(self.frame_right_mid, text='sol 3').place(relx=0, y=100+50, relwidth=0.25, height=40)
            Button(self.frame_right_mid, text='sol 4').place(relx=1/3, y=100+50, relwidth=0.25, height=40)
            Button(self.frame_right_mid, text='sol 5').place(relx=2/3, y=100+50, relwidth=0.25, height=40)
            """


    
    def evenement_entrer(self, event):
        """
        Entrer dans un nouveau type d'objet: rectange/ligne
        """

        self.item = self.canvas_mid.find_closest(event.x, event.y)
        self.item_type = self.canvas_mid.type(self.item)
        #print("entrer:",self.item_type, '\n')

    #Potentiellement non nécessaire
    def evenement_sortir(self, event):
        """
        Sortir d'un objet: rectange/ligne
        """

        self.item = 'None'
        self.item_type = 'None'

    def item_left_click(self, event):
        """
        Clique gauche sur le canvas

        Colore l'item actif
        """
        colors_rec = ['#8fbc8f','#E8A857','#AC8C6A','#5E534F','#795A4C']
        colors_line = ['white','#E8A857','#AC8C6A','#5E534F','#795A4C']
        colors_list= []

        if (self.item_type == "rectangle"):
            colors_list = colors_rec
        else:
            colors_list = colors_line

        color = self.canvas_mid.itemcget(self.item, "fill")
        ind_color = colors_list.index(color)

        if (ind_color==len(colors_list)-1):
            new_indice = 0
        else:
            new_indice = ind_color+1

        self.canvas_mid.itemconfigure(self.item, fill=colors_list[new_indice])
        
    


def main():

    root = Tk()
    root.title("Fenêtre de Raids")
    root.geometry('1200x800+400+80')# Width x Height + X + Y
    app = Raids()
    root.mainloop()


if __name__ == '__main__':
    main()