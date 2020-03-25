import quoridor
import api

if __name__ == "__main__":
    repo = vars(quoridor.analyser_commande())
    idul = repo['idul']
    x = api.initialiser_partie(idul)
    y = x[1]
    id_partie = x[0]
    print(id_partie)
    quitter = False
    while quitter != True:
        quoridor.afficher_damier_ascii(y)
        type_coup = quoridor.demander_typecoup()
        if type_coup == 'Q':
            quitter = True
            print('Au revoir')
            break
        position = quoridor.demander_position()
        y = api.jouer_coup(id_partie, type_coup, position)
