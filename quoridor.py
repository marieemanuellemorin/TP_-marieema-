import argparse


def analyser_commande():
    # analyser la ligne de commande qui devrait être python main.py nom_du_joueur
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument(
        "idul", type=str, help='IDUL du joueur'
        )

    parser.add_argument(
        '-l', "--lister", action="store_true",
        help="lister les identifiants de vos 20 dernières parties"
    )
    return parser.parse_args()

def afficher_damier_ascii(état_jeu):
    position_idul = état_jeu["joueurs"][0]["pos"]
    position_auto = état_jeu["joueurs"][1]["pos"]
    murh = état_jeu["murs"]["horizontaux"]
    murv = état_jeu["murs"]["verticaux"]
    lhead1 = '   -----------------------------------'
    lfoot1 = '--|-----------------------------------'
    lfoot2 = '  | 1   2   3   4   5   6   7   8   9 '
    vdebut = ' |'
    hdebut = '  |'
    full = [[' . '] * 9, [' . '] * 9, [' . '] * 9, [' . '] * 9, [' . '] * 9, [' . '] * 9, [' . '] * 9, [' . '] * 9, [' . '] * 9]
    half = [['   '] * 9, ['   '] * 9, ['   '] * 9, ['   '] * 9, ['   '] * 9, ['   '] * 9, ['   '] * 9, ['   '] * 9, ['   '] * 9]
    full[position_idul[1]-1][position_idul[0]-1] = ' 1 '
    #AUTOMATE
    full[position_auto[1]-1][position_auto[0]-1] = ' 2 '
    #MUR VERTICAL
    l = len(murv)
    for i in range(l):
        full[murv[i][1]-1][murv[i][0]-1] = '| . '
        half[murv[i][1]][murv[i][0]-1] = '|   '
        full[murv[i][1]][murv[i][0]-1] = '| . '
    #MUR HORIZONTAL
    l = len(murh)
    for i in range(l):
        if half[murh[i][1]-1][murh[i][0]-1] == '|   ':
            half[murh[i][1]-1][murh[i][0]-1] = '|---'
        else:
            half[murh[i][1]-1][murh[i][0]-1] = '---'
        half[murh[i][1]-1][murh[i][0]] = '----'
    #AFFICHER TABLEAU
    print(f'Légende: 1={état_jeu["joueurs"][0]["nom"]}, 2={état_jeu["joueurs"][1]["nom"]}')
    print(lhead1)
    for y in range(9, 0, -1):
        lignefull= f'{y}' + vdebut
        lignehalf = hdebut
        for x in range(1, 10):
            if (len(f'{full[y-1][x-1]}') == 3) and (x > 1):
                lignefull += ' '
            lignefull += f'{full[y-1][x-1]}'
            if (len(f'{half[y-1][x-1]}') == 3) and (x > 1):
                lignehalf += ' '
            lignehalf += f'{half[y-1][x-1]}'
        lignefull += '|'
        lignehalf += '|'
        print(lignefull)
        if y > 1:
            print(lignehalf)
    print(lfoot1)
    print(lfoot2)

def demander_typecoup():
    type_coup = input("Entrez type de coup:'Q': quitter, 'D': déplacer, 'MH': mur horizontal ou 'MV' mur vertical: ")
    return type_coup
def demander_position():
    position = input("Entrez la position (x,y) du coup: ")
    return position
