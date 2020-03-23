import argparse


def analyser_commande():
    python main.py nom_du_joueur
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'nom_du_joueur', nargs='1', dest='idul', help='IDUL du joueur'
        )
    parser.add_argument(
        '-h','--help',
        metavar='TYPE', dest='help' help="show this help message and exit"
    )
    parser.add_argument(
        '-l', '--lister',
        metavar='TYPE', dest='lister', help='lister les identifiants de vos 20 dernières parties'
    )
    return parser.parse_args()

def afficher_damier_ascii(état_jeu):
    état_jeu = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [5, 5]}, 
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ], 
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [8, 6]], 
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
}
position_idul = état_jeu["joueurs"][0]["pos"]
position_auto = état_jeu["joueurs"][1]["pos"]
murh = état_jeu["murs"]["horizontaux"]
murv = état_jeu["murs"]["verticaux"]
LHead1 ='   -----------------------------------'
LFoot1 ='--|-----------------------------------'
LFoot2 ='  | 1   2   3   4   5   6   7   8   9 '


VDebut = ' |'
HDebut = '  |'

# Cases du tableau
#Cases pour une ligne du tableau pour afficher un position avec mur horizontal plein
H_PleinCase1 = '--'
H_PleinCase2a9 = '-------'
#Cases pour une ligne du tableau pour afficher un position avec mur horizontal vide
H_VideCase1 = '  '
H_VideCase2a9= '   '

#Cases pour une ligne du tableau pour afficher un position avec mur vertical plein(et celle de la ligne suivante)
V_IdulCase1 = ' 1'
V_IdulCase2a9= '   1'
V_AutoCase1 = ' 2'
V_AutoCase2a9= '   2'
V_PleinCase1 = ' |'
V_PleinCase2a9 = ' | .'
V2_PleinCase2a9= ' |  '
#Cases pour une ligne du tableau pour afficher un position avec mur horizontal vide
V_VideCase1 = ' .'
V_VideCase2a9= '   .'

Full = [[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',],[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',],
        [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',],[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',],
        [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',],[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',],
        [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',],[' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',],
        [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',]]

Half = [['   ','   ','   ','   ','   ','   ','   ','   ','   '],['   ','   ','   ','   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   ','   ','   ','   '],['   ','   ','   ','   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   ','   ','   ','   '],['   ','   ','   ','   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   ','   ','   ','   '],['   ','   ','   ','   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   ','   ','   ','   ']]

#IDUL
Full[position_idul[1]-1][position_idul[0]-1] = ' 1 '

#AUTOMATE
Full[position_auto[1]-1][position_auto[0]-1] = ' 2 '

#MUR VERTICAL
l = len(murv)
for i in range(l):
    Full[murv[i][1]-1][murv[i][0]-1] = '| . '
    Half[murv[i][1]-1][murv[i][0]-1] = '|   '
    Full[murv[i][1]][murv[i][0]-1] = '| . '

#MUR HORIZONTAL
l = len(murh)
for i in range(l):
    Half[murh[i][1]-1][murh[i][0]-1] = '---'
    Half[murh[i][1]-1][murh[i][0]] = '----'
    
    ####SUR L'AFFICHAGE GÉRER LA LONGUEURE DE LA POSITION SI 3, AJOUTER UN ESPACE.

#AFFICHER TABLEAU
print(LHead1)
     
for i in range(9, 0, -1):
    Ligne_Full= f'{Y}' + VDebut
    Ligne_Half = HDebut
    for j in range(0, 9):
        
        Ligne_Full += Full[i]

for Y in range (1, 10):
#control l'affichage inversé avec NoLigne
    #Noligne = 9 - i
    LigneTabVer = f'{Y}' + VDebut
    LigneTabHor = HDebut
    for X in range(1, 10):
    # Controller affichage pour la position 1 de la ligne
        if X == 1:
            if (position_idul[1] == Y) and (position_idul[0] == X):
                LigneTabVer=LigneTabVer + V_IdulCase1 
            elif (position_auto[1] == Y) and (position_auto[0] == X):
                LigneTabVer= LigneTabVer + V_AutoCase1
            else:
                VertTrouve = False
                for x in murv:
                    if (x[0] == X) and x[1] == Y: 
                        VertTrouve == True
                if VertTrouve == True:        
                    LigneTabVer= LigneTabVer + V_PleinCase1
                    LigneTabHor= LigneTabHor + V_PleinCase1 
   
                else:
                    LigneTabVer= LigneTabVer + V_VideCase1
            
                HorTrouve = False
                for x in murh:
                    if x[0] == X and x[1] == Y:
                        HorTrouve == True
                if HorTrouve == True:
                    LigneTabHor = LigneTabHor + H_PleinCase1
                elif LigneTabHor[len(LigneTabHor)-1] == '-':
                    LigneTabHor += ' '
                else:
                    LigneTabHor += H_VideCase1

      #Affichage des lignes 2 a 9
        else:
            if (position_idul[1] == Y) and (position_idul[0] == X):
                LigneTabVer=LigneTabVer + V_IdulCase2a9 
            elif (position_auto[1] == Y) and (position_auto[0] == X):
                LigneTabVer= LigneTabVer + V_AutoCase2a9
            else:
                VertTrouve = False
                for x in murv:
                    if (x[0] == X) and (x[1] == Y): 
                        VertTrouve = True
                if VertTrouve == True:
                    LigneTabVer= LigneTabVer + V_PleinCase2a9 
                    LigneTabHor= LigneTabHor + V2_PleinCase2a9  
                    
                else:
                    LigneTabVer= LigneTabVer + V_VideCase2a9
                    
            HorTrouve = False
            for x in murh:
                if x[0] == X and x[1] == Y:
                    HorTrouve = True
            if HorTrouve == True:
                LigneTabHor = LigneTabHor + H_PleinCase2a9
            elif LigneTabHor[len(LigneTabHor)-1] == '-':
                LigneTabHor += ' '
            else:
                LigneTabHor += H_VideCase2a9
# On a fini d'itérer dans les position For NoPos alors on affiche nos lignes
    print(LigneTabVer)
    print(LigneTabHor)
#On a fii d'itérer dans les Lignes on affiche les 2 lignes de footer
print(LFoot1)
print(LFoot2)

    print(f'Légende: 1={état_jeu["joueurs"][0]["nom"]}, 2={état_jeu["joueurs"][1]["nom"]}'')
