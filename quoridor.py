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
H_PleinCase2a9 = '----'
#Cases pour une ligne du tableau pour afficher un position avec mur horizontal vide
H_VideCase1 = '  '
H_VideCase2a9= '    '

#Cases pour une ligne du tableau pour afficher un position avec mur vertical plein(et celle de la ligne suivante)
V_IdulCase1 = ' 1'
V_IdulCase2a9= '   1'
V_AutoCase1 = ' 2'
V_AutoCase2a9= '   2'
V_PleinCase1 = ' |'
V_PleinCase2a9 = '   |'
#Cases pour une ligne du tableau pour afficher un position avec mur horizontal vide
V_VideCase1 = ' .'
V_VideCase2a9= '   .'

#Afficher Tableau
print(LHead1)

for NoLigne in range (1, 10):
#control l'affichage inversé avec NoLigne
    #Noligne = 9 - i
    LigneTabVer = f'{NoLigne}' + VDebut
    LigneTabHor = HDebut
    for NoPos in range(1, 10):
    # Controller affichage pour la position 1 de la ligne
        if NoPos == 1:
            if (position_idul[0] == NoLigne) and (position_idul[1] == NoPos):
                LigneTabVer=LigneTabVer + V_IdulCase1 
            if (position_auto[0] == NoLigne) and (position_auto[1] == NoPos):
                LigneTabVer= LigneTabVer + V_AutoCase1
                else:
                VertTrouve = False
                for x in murv:
                    if (x[0] == NoPos) and x[1] == NoLigne: 
                        VertTrouve == True
                if VertTrouve == True:        
                    LigneTabVer= LigneTabVer + V_PleinCase1
                    LigneTabHor= LigneTabHor + V_PleinCase1 
   
                else:
                    LigneTabVer= LigneTabVer + V_VideCase1
                 
                HorTrouve = False
                for x in murh:
                    if x[0] == NoPos and x[1] == NoLigne:
                        HorTrouve == True
                if HorTrouve == True:
                    LigneTabHor = LigneTabHor + H_PleinCase1
                else:
                    LigneTabHor = H_VideCase1

      #Affichage des lignes 2 a 9
        else:
            if (position_idul[0] == NoLigne) and (position_idul[1] == NoPos):
                LigneTabVer=LigneTabVer + V_IdulCase2a9 
            if (position_auto[0] == NoLigne) and (position_auto[1] == NoPos):
                LigneTabVer= LigneTabVer + V_AutoCase2a9
            else:
                VertTrouve = False
                for x in murv:
                    if (x[0] == NoPos) and (x[1] == NoLigne): 
                        VertTrouve = True
                if VertTrouve == True:
                    LigneTabVer= LigneTabVer + V_PleinCase2a9 
                    LigneTabHor= LigneTabHor + V_PleinCase2a9  
                    
                else:
                    LigneTabVer= LigneTabVer + V_VideCase2a9
                        
                HorTrouve = False
                for x in murh:
                    if x[0] == NoPos and x[1] == NoLigne:
                        HorTrouve = True
                if HorTrouve == True:  
                     LigneTabHor = LigneTabHor + H_PleinCase2a9
                else:
                    LigneTabHor = H_VideCase2a9
# On a fini d'itérer dans les position For NoPos alors on affiche nos lignes
    print(LigneTabVer)
    print(LigneTabHor)
#On a fii d'itérer dans les Lignes on affiche les 2 lignes de footer
print(LFoot1)
print(LFoot2)

    print(f'Légende: 1={état_jeu["joueurs"][0]["nom"]}, 2={état_jeu["joueurs"][1]["nom"]}'')
