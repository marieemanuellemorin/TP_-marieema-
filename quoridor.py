import argparse


def analyser_commande():
    # analyser la ligne de commande qui devrait être python main.py nom_du_joueur
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - phase 1")
    parser.add_argument(
        "idul", type = str, help='IDUL du joueur'
        )

    parser.add_argument(
        '-l', "--lister", action = "store_true",
         help="lister les identifiants de vos 20 dernières parties"
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
        Half[murv[i][1]][murv[i][0]-1] = '|   '
        Full[murv[i][1]][murv[i][0]-1] = '| . '

    #MUR HORIZONTAL
    l = len(murh)
    for i in range(l):
        if Half[murh[i][1]-1][murh[i][0]-1] == '|   ':
            Half[murh[i][1]-1][murh[i][0]-1] = '|---'
        else:
            Half[murh[i][1]-1][murh[i][0]-1] = '---'
        Half[murh[i][1]-1][murh[i][0]] = '----'
    

    #AFFICHER TABLEAU
    print(f'Légende: 1={état_jeu["joueurs"][0]["nom"]}, 2={état_jeu["joueurs"][1]["nom"]}')
    print(LHead1)
     
    for Y in range(9, 0, -1):
          Ligne_Full= f'{Y}' + VDebut
          Ligne_Half = HDebut
        
          for X in range(1, 10):
            if (len(f'{Full[Y-1][X-1]}') == 3) and (X > 1):
                Ligne_Full += ' '
            Ligne_Full += f'{Full[Y-1][X-1]}'
        
            if (len(f'{Half[Y-1][X-1]}') == 3) and (X > 1):
                Ligne_Half += ' '
            Ligne_Half += f'{Half[Y-1][X-1]}'
        Ligne_Full += '|'
        Ligne_Half += '|'
        print(Ligne_Full)
        if Y > 1:
            print(Ligne_Half)
    print(LFoot1)
    print(LFoot2)
