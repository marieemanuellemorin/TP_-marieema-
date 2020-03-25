import quoridor
import api
#Liaison entre les différents modules
if __name__ == "__main__":
    REP = vars(quoridor.analyser_commande())
    idul = REP['idul']
    x = api.initialiser_partie(idul)
    y = x[1]
    id_partie = x[0]
    print(id_partie)
    QUITTER = False
    while QUITTER != True:
        quoridor.afficher_damier_ascii(y)
        type_coup = quoridor.demander_typecoup()
        if type_coup == 'Q':
            QUITTER = True
            print('Au revoir')
            break
        position = quoridor.demander_position()
        y = api.jouer_coup(id_partie, type_coup, position)
