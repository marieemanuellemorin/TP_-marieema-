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
    x = 20
    y = 20

    print(f'Légende: 1={état_jeu["joueurs"][0]["nom"]}, 2={état_jeu["joueurs"][1]["nom"]}'')
