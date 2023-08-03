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

        #Couleur des rectangles et lignes
        self.colors_rec = ['#8fbc8f','#E8A857','#E8E857','#ADADAA','#5E534F','#795A4C']
        self.colors_line = ['white','#E8A857','#E8E857','#ADADAA','#5E534F','#795A4C']

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
                        self.canvas_mid.tag_bind(rec, '<Button-3>', self.item_right_click)
                        self.canvas_mid.tag_bind(rec, '<Enter>', self.evenement_entrer)
                        self.canvas_mid.tag_bind(rec, '<Leave>', self.evenement_sortir)

                #Ligne
                if(x != 19): #Ne pas avoir la colonne de droite
                    if (x not in range(13,17)) or (y not in range(15,20)): #Ne pas avoir les lignes inconstructibles
                        #Horizontal 
                        ligne_horizontale = self.canvas_mid.create_line(x0,y0,x1,y0, dash=[2,4], fill="white", width=3, activefill='black', activewidth=6, tag='ligne_horizontale')
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Button-1>', self.item_left_click)
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Button-3>', self.item_right_click)
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Enter>', self.evenement_entrer)
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Leave>', self.evenement_sortir)
                
                if(y != 19): #Ne pas avoir la ligne du bas
                    if (x not in range(14,17)) or (y not in range(14,20)): #Ne pas avoir les lignes inconstructibles
                        #Vertical
                        ligne_verticale = self.canvas_mid.create_line(x0,y0,x0,y1,dash=[2,4], fill="white", width=3, activefill='black', activewidth=6, tag='ligne_verticale')
                        self.canvas_mid.tag_bind(ligne_verticale, '<Button-1>', self.item_left_click)
                        self.canvas_mid.tag_bind(ligne_verticale, '<Button-3>', self.item_right_click)
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
        self.frame_right_mid = self.frame_right_mid_principal_bis(self.frame_right)
        self.frame_right_mid.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
        
        self.list_sols = ["Sans sol", "T1", "T2", "T3", "T4", "T5"]
        self.list_murs = ["Sans murs", "T1", "T2", "T3", "T4", "T5"]
        self.list_stockages = {"Craftable":["Petite boîte", "Coffre", "Malle", "Râtelier (lvl X)"], 
                          "Non craftable":["Coffre-fort","Entrepôt", "Réfrigérateur", "Une autre tournée", "Triomphe", "Armoire pharmacie", "Étagère", "Dépôt déchets",
                                           "Boîte compartimenté", "Caisse élec"]}
        
        self.list_etablis = {"Craftable":["Feu de camp", "Potager", "Établi Bois", "Fourneau", "Collecteur pluie", "Chevalet tannage", "Séchoir viande", "Table pierre",
                                     "Cuisinière", "Établi armes", "Table couture", "Établi (Plaque)", "Recycleur", "Table médicale", "Fourneau raffiné","Pompe manuelle",
                                     "Presse", "Labo élec", "Station chimie", "Système Hydroponique"], 
                        "Non craftable":["Goût sûr"]}
        
        self.list_decorations = {"Craftable":["Plante d'intérieur", "Table", "Canapé douillet", "lampadaire", "Lit comfortable", "Mangeoire", "Râtelier armes", "Épicéa",
                                        "Parterre fleurs pneu", "Bain fleurs", "Étang décoratif", "Sculpture"], 
                            "Non craftable":["Mannequin", "Hologramme", "Gramophone", "Tête sorcière"]}
        
        self.list_autres = {"Craftable":["Radios", "Chopper", "Douche", "Piège piques", "Cage chien", "Garage", "Garde-robe", "Miroir", "Piège fil", "Fil barbelé",
                                    "Générateur élec", "Bain acide", "Bateau moteur", "ATV", "Tourelle", "Drone station", "Établi up drone", "Toilettes exté"],
                        "Non craftable":["Pompe"]}

        self.list_all =[self.list_sols, self.list_murs, self.list_stockages, self.list_etablis, self.list_decorations, self.list_autres]


    def clear_frame(self, frame):
        """
        Supprime tous les éléments d'une Frame
        """
        for widgets in frame.winfo_children():
            widgets.destroy()

    #FIXME  => REGROUPER PRINCIPAL et PRINCIPAL BIS: Use try/except?
    def frame_right_mid_principal(self):
        """
        Création de la frame right mid principale
        """
        self.clear_frame(self.frame_right_mid)
        try:
            del self.last #Supprime la variable qui représente le dernier bouton sélectionné de la frame frame_right_mid_XXX
        except:
            pass

        self.frame_right_mid = self.frame_right_mid_principal_bis(self.frame_right)
        self.frame_right_mid.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
    
    def frame_right_mid_principal_bis(self, from_frame):
        """
        Création des boutons dans la frame right mid principale
        """        
        frame = Frame(from_frame, highlightbackground="black", highlightthickness=1)

        Button(frame, text="Tout", command=lambda :self.frame_right_mid_secondary("Tout")).place(x=0, y=0, relwidth=1, height=50)
        Button(frame, text="Sols & Murs", command=lambda :self.frame_right_mid_secondary("Sols & Murs")).place(x=0, y=50, relwidth=1, height=50)
        Button(frame, text="Sols", command=lambda :self.frame_right_mid_secondary("Sols")).place(x=0, y=100, relwidth=1, height=50)
        Button(frame, text="Murs", command=lambda :self.frame_right_mid_secondary("Murs")).place(x=0, y=150, relwidth=1, height=50)
        Button(frame, text="Stockages", command=lambda :self.frame_right_mid_secondary("Stockages")).place(x=0, y=200, relwidth=1, height=50)
        Button(frame, text="Établis", command=lambda :self.frame_right_mid_secondary("Établis")).place(x=0, y=250, relwidth=1, height=50)
        Button(frame, text="Décorations", command=lambda :self.frame_right_mid_secondary("Décorations")).place(x=0, y=300, relwidth=1, height=50)
        Button(frame, text="Autres", command=lambda :self.frame_right_mid_secondary("Autres")).place(x=0, y=350, relwidth=1, height=50)

        return frame

    def frame_right_mid_secondary(self, button_txt):
        """
        Création bouton dans la frame right mid principale
        """
        
        self.clear_frame(self.frame_right_mid)
        try:
            del self.last #Supprime la variable qui représente le dernier bouton sélectionné de la frame frame_right_mid_XXX
        except:
            pass

        Button(self.frame_right_mid, text='<-', command=self.frame_right_mid_principal).place(x=0, y=0, relwidth=0.25, height=40)
        Label(self.frame_right_mid, text=button_txt, borderwidth=1, relief='solid').place(relx=0.25, y=0, relwidth=0.5, height=40)

        if(button_txt!="Tout" and button_txt!="Sols & Murs"):
            Label(self.frame_right_mid, text=button_txt).place(relx=0, y=50, relwidth=1, height=40)
            Button(self.frame_right_mid, text='^^').place(relx=.80, y=17+50, relwidth=0.1, height=15) #FIXME command => fct
            Label(self.frame_right_mid, text='', borderwidth=1, relief="solid").place(relx=0, y=80, relwidth=1, height=2)

            self.frame_right_mid_XXX = Frame(self.frame_right_mid, highlightbackground="red", highlightthickness=3)

            if(button_txt=='Sols') or (button_txt=='Murs'):
                relwidth = 0.25     # Largeur des boutons
                x = relwidth/(2*3)  # Position x des boutons
                y = 25              # Position y des boutons
                height = 40         # Hauteur des boutons
                
                self.frame_right_mid_XXX.place(relx=0, y=80+1, relwidth=1, height=150)

                if(button_txt=='Sols'):
                    Button(self.frame_right_mid_XXX, text=self.list_sols[0], name='sols '+self.list_sols[0], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='sols '+self.list_sols[0])).place(relx=0+x, y=y, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_sols[1], name='sols '+self.list_sols[1], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='sols '+self.list_sols[1])).place(relx=1/3+x, y=y, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_sols[2], name='sols '+self.list_sols[2], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='sols '+self.list_sols[2])).place(relx=2/3+x, y=y, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_sols[3], name='sols '+self.list_sols[3], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='sols '+self.list_sols[3])).place(relx=0+x, y=y+50, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_sols[4], name='sols '+self.list_sols[4], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='sols '+self.list_sols[4])).place(relx=1/3+x, y=y+50, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_sols[5], name='sols '+self.list_sols[5], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='sols '+self.list_sols[5])).place(relx=2/3+x, y=y+50, relwidth=relwidth, height=height)

                else:
                    Button(self.frame_right_mid_XXX, text=self.list_murs[0], name='murs '+self.list_murs[0], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='murs '+self.list_murs[0])).place(relx=0+x, y=y, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_murs[1], name='murs '+self.list_murs[1], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='murs '+self.list_murs[1])).place(relx=1/3+x, y=y, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_murs[2], name='murs '+self.list_murs[2], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='murs '+self.list_murs[2])).place(relx=2/3+x, y=y, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_murs[3], name='murs '+self.list_murs[3], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='murs '+self.list_murs[3])).place(relx=0+x, y=y+50, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_murs[4], name='murs '+self.list_murs[4], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='murs '+self.list_murs[4])).place(relx=1/3+x, y=y+50, relwidth=relwidth, height=height)
                    Button(self.frame_right_mid_XXX, text=self.list_murs[5], name='murs '+self.list_murs[5], command=lambda :self.button_left_click_frame_right_mid_XXXX(name='murs '+self.list_murs[5])).place(relx=2/3+x, y=y+50, relwidth=relwidth, height=height)

            else:
                relwidth = .40      # Largeur des boutons
                x = 0.05            # Position x du premier bouton de départ
                y = 30              # Position y du premier bouton de départ
                height = 20         # Hauteur des boutons

                # Gauche
                Label(self.frame_right_mid_XXX, text='Non craftable', font=('Helvetica 11 underline')).place(relx=0, y=10, relwidth=relwidth, height=height)
                #Droite
                Label(self.frame_right_mid_XXX, text='Craftable', font=('Helvetica 11 underline')).place(relx=x+relwidth, y=10, relwidth=relwidth, height=height)

                if(button_txt=='Stockages'):
                    self.frame_right_mid_XXX.place(relx=0, y=80+1, relwidth=1, height=max([len(self.list_stockages['Non craftable']),len(self.list_stockages['Craftable'])])*20+50)

                    for k in range (len(self.list_stockages['Non craftable'])):
                        Button(self.frame_right_mid_XXX, text=self.list_stockages['Non craftable'][k], name='stockages ' +self.list_stockages['Non craftable'][k], anchor="w",
                            command=lambda k=k:self.button_left_click_frame_right_mid_XXXX(name='stockages ' +self.list_stockages['Non craftable'][k])).place(relx=x, y=y+k*height, relwidth=relwidth, height=height)

                    for k in range (len(self.list_stockages['Craftable'])):
                        Button(self.frame_right_mid_XXX, text=self.list_stockages['Craftable'][k], name='stockages ' +self.list_stockages['Craftable'][k],  anchor="w",
                            command=lambda k=k:self.button_left_click_frame_right_mid_XXXX(name='stockages ' +self.list_stockages['Craftable'][k])).place(relx=3*x+relwidth, y=y+k*height, relwidth=relwidth, height=height)
                
                elif(button_txt=='Établis'):
                    self.frame_right_mid_XXX.place(relx=0, y=80+1, relwidth=1, height=max([len(self.list_etablis['Non craftable']),len(self.list_etablis['Craftable'])])*20+50)

                    for k in range (len(self.list_etablis['Non craftable'])):
                        Button(self.frame_right_mid_XXX, text=self.list_etablis['Non craftable'][k], name='établis ' +self.list_etablis['Non craftable'][k], anchor="w",
                            command=lambda k=k:self.button_left_click_frame_right_mid_XXXX(name='établis ' +self.list_etablis['Non craftable'][k])).place(relx=x, y=y+k*height, relwidth=relwidth, height=height)

                    for k in range (len(self.list_etablis['Craftable'])):
                        Button(self.frame_right_mid_XXX, text=self.list_etablis['Craftable'][k], name='établis ' +self.list_etablis['Craftable'][k],  anchor="w",
                            command=lambda k=k:self.button_left_click_frame_right_mid_XXXX(name='établis ' +self.list_etablis['Craftable'][k])).place(relx=3*x+relwidth, y=y+k*height, relwidth=relwidth, height=height)
                
                elif(button_txt=='Décorations'):
                    self.frame_right_mid_XXX.place(relx=0, y=80+1, relwidth=1, height=max([len(self.list_decorations['Non craftable']),len(self.list_decorations['Craftable'])])*20+50)

                    for k in range (len(self.list_decorations['Non craftable'])):
                        Button(self.frame_right_mid_XXX, text=self.list_decorations['Non craftable'][k], name='décorations ' +self.list_decorations['Non craftable'][k], anchor="w",
                            command=lambda k=k:self.button_left_click_frame_right_mid_XXXX(name='décorations ' +self.list_decorations['Non craftable'][k])).place(relx=x, y=y+k*height, relwidth=relwidth, height=height)

                    for k in range (len(self.list_decorations['Craftable'])):
                        Button(self.frame_right_mid_XXX, text=self.list_decorations['Craftable'][k], name='décorations ' +self.list_decorations['Craftable'][k],  anchor="w",
                            command=lambda k=k:self.button_left_click_frame_right_mid_XXXX(name='décorations ' +self.list_decorations['Craftable'][k])).place(relx=3*x+relwidth, y=y+k*height, relwidth=relwidth, height=height)
                
                elif(button_txt=='Autres'):
                    self.frame_right_mid_XXX.place(relx=0, y=80+1, relwidth=1, height=max([len(self.list_autres['Non craftable']),len(self.list_autres['Craftable'])])*20+50)

                    for k in range (len(self.list_autres['Non craftable'])):
                        Button(self.frame_right_mid_XXX, text=self.list_autres['Non craftable'][k], name='autres ' +self.list_autres['Non craftable'][k], anchor="w",
                            command=lambda k=k:self.button_left_click_frame_right_mid_XXXX(name='autres ' +self.list_autres['Non craftable'][k])).place(relx=x, y=y+k*height, relwidth=relwidth, height=height)

                    for k in range (len(self.list_autres['Craftable'])):
                        Button(self.frame_right_mid_XXX, text=self.list_autres['Craftable'][k], name='autres ' +self.list_autres['Craftable'][k],  anchor="w",
                            command=lambda k=k:self.button_left_click_frame_right_mid_XXXX(name='autres ' +self.list_autres['Craftable'][k])).place(relx=3*x+relwidth, y=y+k*height, relwidth=relwidth, height=height)
                

        else:
            raise NameError
    


        print('clicked:', button_txt)


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

        Colore l'item actif en fct du bouton cliqué
        """
        colors_list = []
        flag = False

        try:
            self.last #test si la variable qui représente le dernier bouton sélectionné de la frame frame_right_mid_XXX existe (= bouton appuyé)
        except:
            flag = True
        
        if(flag):
            if (self.item_type == "rectangle"):
                colors_list = self.colors_rec
            else:
                colors_list = self.colors_line

            color = self.canvas_mid.itemcget(self.item, "fill")
            ind_color = colors_list.index(color)

            if (ind_color==len(colors_list)-1):
                new_indice = 0
            else:
                new_indice = ind_color+1
            
        else:
            name=self.last.name
            names=name.split(" ",1)

            if(names[0] == 'sols') and (self.item_type == "rectangle"):
                colors_list = self.colors_rec
                new_indice = self.list_sols.index(names[1])
            elif(names[0] == 'murs') and (self.item_type == "line"):
                colors_list = self.colors_line
                new_indice = self.list_murs.index(names[1])
            else:
                return False

            
        self.canvas_mid.itemconfigure(self.item, fill=colors_list[new_indice])

    def item_right_click(self, event):
        """
        Clique droit sur le canvas

        Colore l'item actif
        """
        colors_list = []

        if (self.item_type == "rectangle"):
            colors_list = self.colors_rec
        else:
            colors_list = self.colors_line

        color = self.canvas_mid.itemcget(self.item, "fill")
        ind_color = colors_list.index(color)

        if (ind_color==len(colors_list)+1):
            new_indice = 0
        else:
            new_indice = ind_color-1

        self.canvas_mid.itemconfigure(self.item, fill=colors_list[new_indice])
    
    def button_left_click_frame_right_mid_XXXX(self, name):
        """
        Clique gauche sur un bouton de la frame_right_mid_XXXX
        """
        try:
            self.last.config(relief=RAISED, state='normal') #test si la variable qui représente le dernier bouton sélectionné de la frame frame_right_mid_XXX est configurable (donc existe)
        except:
            pass

        butt = self.frame_right_mid_XXX.nametowidget(name)
        names=name.split(" ",1)
        print(names)
        butt.config(relief=SUNKEN, state='disabled')

        self.last = butt
        self.last.name=name

    


def main():

    root = Tk()
    root.title("Fenêtre de Raids")
    root.geometry('1200x800+400+80')# Width x Height + X + Y
    app = Raids()
    root.mainloop()


if __name__ == '__main__':
    main()
