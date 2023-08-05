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
        self.frame_left = Frame()
        self.frame_left.place(relx=0, rely=0, relwidth=0.15, relheight=1)

        #Mid panel
        self.frame_mid = Frame()
        self.frame_mid.place(relx=0.15, rely=0, relwidth=0.60, relheight=1)

        #Right panel
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
        #Hauteur/Largeur relative
        self.canvas_mid.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)
        self.canvas_mid.update()

        #Hauteur/Largeur en dure
        self.canvas_mid.place(relx=0.01, rely=0.01, relheight='', relwidth='', width=int(self.canvas_mid.winfo_width()), height=int(self.canvas_mid.winfo_height()))
        self.canvas_mid.update()

        #Couleur des rectangles et lignes pour le canvas
        self.colors_rec = ['#8fbc8f','#E8A857','#E8E857','#ADADAA','#5E534F','#795A4C']
        self.colors_line = ['white','#E8A857','#E8E857','#ADADAA','#5E534F','#795A4C']

        self.create_canvas()
        
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
        
        #{"catégorie:{objet:[nb, max, val_sol_min]}"}
        self.list_stockages = {
            "Craftable":{"Petite boîte":{"nb":0, "max":40, "val_sol_min":1}, "Coffre":{"nb":0, "max":40, "val_sol_min":1}, "Malle":{"nb":0, "max":40, "val_sol_min":2}, 
                         "Râtelier (lvl X)":{"nb":0, "max":40, "val_sol_min":3}}, 
            "Non craftable":{"Coffre-fort":{"nb":0, "max":5, "val_sol_min":1},"Entrepôt":{"nb":0, "max":1, "val_sol_min":0}, "Réfrigérateur":{"nb":0, "max":1, "val_sol_min":3}, 
                             "Une autre tournée":{"nb":0, "max":1, "val_sol_min":0}, "Triomphe":{"nb":0, "max":1, "val_sol_min":3}, "Armoire pharmacie":{"nb":0, "max":1, "val_sol_min":3}, 
                             "Étagère":{"nb":0, "max":1, "val_sol_min":2}, "Dépôt déchets":{"nb":0, "max":1, "val_sol_min":2}, "Boîte compartimenté":{"nb":0, "max":1, "val_sol_min":3}, 
                             "Caisse élec":{"nb":0, "max":1, "val_sol_min":3}}
            }

        self.list_etablis = {
            "Craftable":{"Feu de camp":{"nb":0, "max":2, "val_sol_min":0}, "Potager":{"nb":0, "max":2, "val_sol_min":0}, "Établi Bois":{"nb":0, "max":2, "val_sol_min":1}, 
                         "Fourneau":{"nb":0, "max":2, "val_sol_min":1}, "Collecteur pluie":{"nb":0, "max":2, "val_sol_min":0}, "Chevalet tannage":{"nb":0, "max":2, "val_sol_min":0}, 
                         "Séchoir viande":{"nb":0, "max":2, "val_sol_min":1}, "Table pierre":{"nb":0, "max":2, "val_sol_min":1}, "Cuisinière":{"nb":0, "max":1, "val_sol_min":3}, 
                         "Établi armes":{"nb":0, "max":1, "val_sol_min":2}, "Table couture":{"nb":0, "max":2, "val_sol_min":2}, "Établi (Plaque)":{"nb":0, "max":2, "val_sol_min":2}, 
                         "Recycleur":{"nb":0, "max":2, "val_sol_min":2}, "Table médicale":{"nb":0, "max":2, "val_sol_min":2}, "Fourneau raffiné":{"nb":0, "max":2, "val_sol_min":0}, 
                         "Pompe manuelle":{"nb":0, "max":1, "val_sol_min":0}, "Presse":{"nb":0, "max":2, "val_sol_min":4}, "Labo élec":{"nb":0, "max":1, "val_sol_min":3}, 
                         "Station chimie":{"nb":0, "max":1, "val_sol_min":4}, "Système Hydroponique":{"nb":0, "max":1, "val_sol_min":4}}, 
            "Non craftable":{"Goût sûr":{"nb":0, "max":2, "val_sol_min":0}}
            }
        
        self.list_decorations = {
            "Craftable":{"Plante d'intérieur":{"nb":0, "max":15, "val_sol_min":1}, "Table":{"nb":0, "max":3, "val_sol_min":2}, "Canapé douillet":{"nb":0, "max":4, "val_sol_min":2}, 
                         "lampadaire":{"nb":0, "max":10, "val_sol_min":1}, "Lit comfortable":{"nb":0, "max":3, "val_sol_min":3}, "Mangeoire":{"nb":0, "max":4, "val_sol_min":0}, 
                         "Râtelier armes":{"nb":0, "max":3, "val_sol_min":3}, "Épicéa":{"nb":0, "max":3, "val_sol_min":1}, "Parterre fleurs pneu":{"nb":0, "max":3, "val_sol_min":0}, 
                         "Bain fleurs":{"nb":0, "max":3, "val_sol_min":0}, "Étang décoratif":{"nb":0, "max":3, "val_sol_min":0}, "Sculpture":{"nb":0, "max":1, "val_sol_min":0}}, 
            "Non craftable":{"Mannequin":{"nb":0, "max":1, "val_sol_min":0}, "Hologramme":{"nb":0, "max":1, "val_sol_min":0}, "Gramophone":{"nb":0, "max":1, "val_sol_min":0}, 
                             "Tête sorcière":{"nb":0, "max":1, "val_sol_min":0}}
            }
        
        self.list_autres = {
            "Craftable":{"Radios":{"nb":0, "max":1, "val_sol_min":1}, "Chopper en contru":{"nb":0, "max":1, "val_sol_min":1}, "Chopper fonctionnel":{"nb":0, "max":1, "val_sol_min":0}, 
                         "Douche":{"nb":0, "max":2, "val_sol_min":0}, "Piège piques":{"nb":0, "max":80, "val_sol_min":0}, "Cage chien":{"nb":0, "max":1, "val_sol_min":0}, 
                         "Garage":{"nb":0, "max":1, "val_sol_min":0}, "Garde-robe":{"nb":0, "max":1, "val_sol_min":1}, "Miroir":{"nb":0, "max":1, "val_sol_min":1}, 
                         "Piège fil":{"nb":0, "max":1, "val_sol_min":0}, "Fil barbelé":{"nb":0, "max":20, "val_sol_min":0}, "Générateur élec":{"nb":0, "max":1, "val_sol_min":1}, 
                         "Bain acide":{"nb":0, "max":1, "val_sol_min":3}, "Bateau en contru":{"nb":0, "max":1, "val_sol_min":3}, "ATV en contru":{"nb":0, "max":1, "val_sol_min":3}, 
                         "ATV fonctionnel":{"nb":0, "max":1, "val_sol_min":0}, "Tourelle":{"nb":0, "max":4, "val_sol_min":3}, "Drone station":{"nb":0, "max":1, "val_sol_min":3}, 
                         "Établi up drone":{"nb":0, "max":1, "val_sol_min":3}, "Toilettes exté":{"nb":0, "max":1, "val_sol_min":0}},
            "Non craftable":{"Pompe":{"nb":0, "max":1, "val_sol_min":0}}
            }

        self.list_all =[self.list_sols, self.list_murs, self.list_stockages, self.list_etablis, self.list_decorations, self.list_autres]


    def create_canvas(self):
        #Création ligne/Rectangle
        width = int(self.canvas_mid.winfo_width())-4
        height = int(self.canvas_mid.winfo_height())-4
    
        for y in range(1,20):
            for x in range(1,20):
                x0 = (x)*(width/20)+2
                y0 = (y)*(height/20)+2
                x1 = (x+1)*(width/20)+2
                y1 = (y+1)*(height/20)+2

                #Rectangle
                if(x in range(13,17)) and (y in range(14, 19)):
                    rec = self.canvas_mid.create_rectangle(x0,y0,x1,y1, fill=self.colors_rec[0], width=0)

                else:
                    if((x != 19) and (y != 19)):
                        rec = self.canvas_mid.create_rectangle(x0,y0,x1,y1, fill='#8fbc8f', width=0 , activefill="red", tag='rec')
                        self.canvas_mid.tag_bind(rec, '<Button-1>', self.item_left_click)
                        self.canvas_mid.tag_bind(rec, '<Button-3>', self.item_right_click)
                        self.canvas_mid.tag_bind(rec, '<Enter>', self.event_enter)
                        self.canvas_mid.tag_bind(rec, '<Leave>', self.event_get_out)

                #Ligne
                if(x != 19): #Ne pas avoir la colonne de droite
                    if (x not in range(13,17)) or (y not in range(15,20)): #Ne pas avoir les lignes inconstructibles
                        #Horizontal 
                        ligne_horizontale = self.canvas_mid.create_line(x0,y0,x1,y0, dash=[2,4], fill="white", width=3, activefill='black', activewidth=6, tag='ligne_horizontale')
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Button-1>', self.item_left_click)
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Button-3>', self.item_right_click)
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Enter>', self.event_enter)
                        self.canvas_mid.tag_bind(ligne_horizontale, '<Leave>', self.event_get_out)
                
                if(y != 19): #Ne pas avoir la ligne du bas
                    if (x not in range(14,17)) or (y not in range(14,20)): #Ne pas avoir les lignes inconstructibles
                        #Vertical
                        ligne_verticale = self.canvas_mid.create_line(x0,y0,x0,y1,dash=[2,4], fill="white", width=3, activefill='black', activewidth=6, tag='ligne_verticale')
                        self.canvas_mid.tag_bind(ligne_verticale, '<Button-1>', self.item_left_click)
                        self.canvas_mid.tag_bind(ligne_verticale, '<Button-3>', self.item_right_click)
                        self.canvas_mid.tag_bind(ligne_verticale, '<Enter>', self.event_enter)
                        self.canvas_mid.tag_bind(ligne_verticale, '<Leave>', self.event_get_out)
        
    def clear_frame(self, frame):
        """
        Supprime tous les éléments d'une Frame
        """
        for widgets in frame.winfo_children():
            widgets.destroy()

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
                    
                    k=0
                    for item in (self.list_stockages['Non craftable']):
                        Button(self.frame_right_mid_XXX, text=item, name='stockages non_craftable ' +item, anchor="w",
                            command=lambda item=item:self.button_left_click_frame_right_mid_XXXX(name='stockages non_craftable ' +item)).place(relx=x, y=y+k*height, relwidth=relwidth, height=height)
                        k+=1
                    
                    k=0
                    for item in (self.list_stockages['Craftable']):
                        Button(self.frame_right_mid_XXX, text=item, name='stockages craftable ' +item,  anchor="w",
                            command=lambda item=item:self.button_left_click_frame_right_mid_XXXX(name='stockages craftable ' +item)).place(relx=3*x+relwidth, y=y+k*height, relwidth=relwidth, height=height)
                        k+=1

                elif(button_txt=='Établis'):
                    self.frame_right_mid_XXX.place(relx=0, y=80+1, relwidth=1, height=max([len(self.list_etablis['Non craftable']),len(self.list_etablis['Craftable'])])*20+50)

                    k=0
                    for item in (self.list_etablis['Non craftable']):
                        Button(self.frame_right_mid_XXX, text=item, name='établis non_craftable ' +item, anchor="w",
                            command=lambda item=item:self.button_left_click_frame_right_mid_XXXX(name='établis non_craftable ' +item)).place(relx=x, y=y+k*height, relwidth=relwidth, height=height)
                        k+=1

                    k=0
                    for item in (self.list_etablis['Craftable']):
                        Button(self.frame_right_mid_XXX, text=item, name='établis craftable ' +item,  anchor="w",
                            command=lambda item=item:self.button_left_click_frame_right_mid_XXXX(name='établis craftable ' +item)).place(relx=3*x+relwidth, y=y+k*height, relwidth=relwidth, height=height)
                        k+=1

                elif(button_txt=='Décorations'):
                    self.frame_right_mid_XXX.place(relx=0, y=80+1, relwidth=1, height=max([len(self.list_decorations['Non craftable']),len(self.list_decorations['Craftable'])])*20+50)

                    k=0
                    for item in (self.list_decorations['Non craftable']):
                        Button(self.frame_right_mid_XXX, text=item, name='décorations non_craftable ' +item, anchor="w",
                            command=lambda item=item:self.button_left_click_frame_right_mid_XXXX(name='décorations non_craftable ' +item)).place(relx=x, y=y+k*height, relwidth=relwidth, height=height)
                        k+=1

                    k=0
                    for item in (self.list_decorations['Craftable']):
                        Button(self.frame_right_mid_XXX, text=item, name='décorations craftable ' +item,  anchor="w",
                            command=lambda item=item:self.button_left_click_frame_right_mid_XXXX(name='décorations craftable ' +item)).place(relx=3*x+relwidth, y=y+k*height, relwidth=relwidth, height=height)
                        k+=1

                elif(button_txt=='Autres'):
                    self.frame_right_mid_XXX.place(relx=0, y=80+1, relwidth=1, height=max([len(self.list_autres['Non craftable']),len(self.list_autres['Craftable'])])*20+50)

                    k=0
                    for item in (self.list_autres['Non craftable']):
                        Button(self.frame_right_mid_XXX, text=item, name='autres non_craftable ' +item, anchor="w",
                            command=lambda item=item:self.button_left_click_frame_right_mid_XXXX(name='autres non_craftable ' +item)).place(relx=x, y=y+k*height, relwidth=relwidth, height=height)
                        k+=1

                    k=0
                    for item in (self.list_autres['Craftable']):
                        Button(self.frame_right_mid_XXX, text=item, name='autres craftable ' +item,  anchor="w",
                            command=lambda item=item:self.button_left_click_frame_right_mid_XXXX(name='autres craftable ' +item)).place(relx=3*x+relwidth, y=y+k*height, relwidth=relwidth, height=height)
                        k+=1

        else:
            raise NameError
    

        print('clicked:', button_txt)

    
    def generate_item(self, name, x1, y1, orientation, val_sol):
        """
        Vérifie que l'item à poser ne déroge pas aux conditions de pose (max item)


        """
        #{'Craftable':{'item':[pos x, pos y, orientation(n/o/s/e), taille[nb_case x, nb_case y], sol(Nv.)###taille(relx, rely)]}}
        names=name.split(" ",2)
        categorie=' '.join(names[1].split("_",1)).capitalize()

        if(names[0]=='stockages'):
            if(categorie=='Craftable'):
                total=0
                vals = self.list_stockages[categorie].values()
                
                for val in vals:
                    total+=val['nb']

                if(total<self.list_stockages[categorie][names[2]]['max']):
                    self.list_stockages[categorie][names[2]]['nb']+=1
                else:
                    print('Nombre max. d\'objets atteint:', names[2])
            
            else:
                if(self.list_stockages[categorie][names[2]]['nb']<self.list_stockages[categorie][names[2]]['max']):
                    self.list_stockages[categorie][names[2]]['nb']+=1
                else:
                    print('Nombre max. d\'objets atteint:', names[2])
                    
        elif(names[0]=='établis'):
            if(self.list_etablis[categorie][names[2]]['nb']<self.list_etablis[categorie][names[2]]['max']):
                self.list_etablis[categorie][names[2]]['nb']+=1
            else:
                print('Nombre max. d\'objets atteint:', names[2])
        
        elif(names[0]=='décorations'):
            if(self.list_decorations[categorie][names[2]]['nb']<self.list_decorations[categorie][names[2]]['max']):
                self.list_decorations[categorie][names[2]]['nb']+=1
            else:
                print('Nombre max. d\'objets atteint:', names[2])
        
        elif(names[0]=='autres'):
            if(self.list_autres[categorie][names[2]]['nb']<self.list_autres[categorie][names[2]]['max']):
                self.list_autres[categorie][names[2]]['nb']+=1
            else:
                print('Nombre max. d\'objets atteint:', names[2])

        return True


    def event_enter(self, event):
        """
        Entrer dans un nouveau type d'objet: rectange/ligne
        """
        self.item = self.canvas_mid.find_closest(event.x, event.y)
        self.item_type = self.canvas_mid.type(self.item)
        #print("entrer:",self.item_type, '\n')

    #Potentiellement non nécessaire
    def event_get_out(self, event):
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
            names=name.split(" ",2)

            if(names[0] == 'sols') and (self.item_type == "rectangle"):
                colors_list = self.colors_rec
                new_indice = self.list_sols.index(names[2])

            elif(names[0] == 'murs') and (self.item_type == "line"):
                colors_list = self.colors_line
                new_indice = self.list_murs.index(names[2])

            elif(self.item_type == "rectangle"):
                x1, y1, x2, y2 = self.canvas_mid.coords(self.item)
                val_nv = self.colors_rec.index(self.canvas_mid.itemcget(self.item, 'fill'))

                self.generate_item(name,x1,y1,'n',val_nv)
                return False
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

        Définit self.last, modifie le relief et le state de certains boutons
        """
        try:
            self.last.config(relief=RAISED, state='normal') #test si la variable qui représente le dernier bouton sélectionné de la frame frame_right_mid_XXX est configurable (donc existe)
        except:
            pass

        butt = self.frame_right_mid_XXX.nametowidget(name)
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
