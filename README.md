# LDOE-UI-Raids
Projet d'application pour créer/explorer des bases pour les raids dans LDOE.
<br>
<br>


<ins>**BUGS**</ins>:<br>
10/06/23 ==> **MAJOR BUG**
- Clique sur ligne (ligne active): Détecte rectangle (Potentiellement bug sur 1 ligne de pixel supérieur et inférieur) :
  - Expliquation supplémentaire :  Le pixel de souris est sur le rectangle mais la ligne est toujours considérée comme active.<br>
   => Problème de compréhension entre les objets pour savoir lequel est réellement actif. <br>
  !!! La fonction ligne s'applique au rectangle sous la souris !!!

11/06/23 ==> MINOR BUG
- Lag lors du redimensionnement de la fenêtre principale :
  - Expliquation supplémentaire : Test de repasser la taille du canvas en dure (non relative) non concluant
<br>


<ins>**TODO**</ins>:
- Permettre un changement d'angle du canvas (orientation)
  - Connexe avec une fonction zoom in/out
  - Connexe avec une posibilité d'avoir des sides barres
- Changement de l'aspect des sols (Images plutôt que couleurs)
- Frame _right_mid_ avec boutons de sélections pour :
  - Un niveau de sol/mur spécifique
  - Objets plaçables dans la base
- Liste des objets :
  - Pricipaux (établis de base(craftable), coffres, ..)
  - Secondaire (décos craftables : table, fauteuille, ..)
  - Tertiaire (frigo, entrepôt, ..) 
- Lier barre de recherche dans _left_top_ avec la BDD de _left_mid_
- Lier le texte dans la frame _mid_top_ et la table sélectionnée dans la BDD de _left_mid_
- Modifier l'ancre des boutons **Chercher** dans les Frames _left_top_ et _right_top_ pour être au centre
- Gestion de sauvegarde du "dessin" => Idée : Fichiers de configuration + BDD
<br>

- Etendre l'application aux spécificités de la colonie
<br>

================================ 10-11/06/23 ==============================
- Définition de la fonction **ligne_ckick_event(event)** :
  - Clique gauche sur une ligne change sa couleur parmis les 5 possibles : ['white','#E8A857','#AC8C6A','#5E534F','#795A4C'] => Boucle
  - Les 5 couleurs représentent le niveau d'un mur entre 0 et 5 => Idée : Image de mur plutôt que couleur
- Gestion de la zone rectangulaire non constructible (x0=13,y0=14,x1=17,y1=19)
<br>

================================ 07/06/23 ================================
- Création d'une Frame _mid_mid_ + ajout du canvas _canvas_mid_
- Taille de canvas responsive => Idée : Dessin responsive => Bouton UPDATE?
- Couleur canvas (_dark sea green_)
- Création de grille (18x18+1+1) avec lignes et rectangles (options _activefill_, _activewidth_)
- Définition de la fonction **rec_click_event(event)** :
  - Clique gauche sur un rectangle change sa couleur parmis les 5 possibles : ['#8fbc8f','#E8A857','#AC8C6A','#5E534F','#795A4C'] => Boucle
  - Les 5 couleurs représentent le niveau d'un sol entre 0 et 5 => Idée : Image de sol plutôt que couleur
<br>

- Modification mineur de la largeur des Frames _left_ et _mid_
- Création du fichier _**DB_access.py**_ pour stocker les identifiants de connections à la BDD
- Modification majeur du fichier _**README.md**_
<br>

================================ 06/06/23 ================================
- Liaison entre la BDD et le Treeview
- Création Frame _right_top_
- Ajout de 2 barres de recherches + bouton **Chercher** dans les Frames _left_top_ et _right_top_
- Modification mineur de l'aspect des Frames
- Modification de la taille de la fenêtre principale (augmentation ~50%)
<br>

================================ 05/06/23 ================================
- Lecture doc _MySQL_, _mysql.connector_
- Création d'une BDD avec MySQL Workbench : **base_raids** et la table **noname_1**
- Liaison entre la BDD et Main_Raids.py
<br>

================================ 29/05/23 ================================
- Dessin papier de l'UI
<br>

- Création _**Main_Raids.py**_
- Création d'une première fenêtre avec la Bibliothèque Tkinter
- Disposition des principales Frames : _left_, _mid_, _right_
- Disposition d'autres Frames : _mid_top_, _left_top_, _left_mid_
- Ajout d'un treeview dans _left_mid_


