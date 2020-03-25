import requests
#url du jeu
URL = 'https://python.gel.ulaval.ca/quoridor/api'
#fonction lister_parties
def lister_parties(idul):
    rep = requests.get(f'{URL}/lister/', params={'idul': f'{idul}'})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if "message" in rep.keys():
            raise RuntimeError(rep['message'])
        return rep
    print(f"Le GET sur {URL+'lister'} a produit le code d'erreur {rep.status_code}.")
#fonction initialiser_partie
def initialiser_partie(idul):
    rep = requests.post(f'{URL}/initialiser/', data={'idul': f'{idul}'})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if "message" in rep.keys():
            raise RuntimeError(rep['message'])
        identifiant = rep['id']
        etat = rep['état']
        return(identifiant, etat)
    print(f"Le POST sur {URL+'initialiser'} a produit le code d'erreur {rep.status_code}.")
#Fonction jouer_coup
def jouer_coup(id_partie, type_coup, position):
    rep = requests.post(f'{URL}/jouer/', data={'id': id_partie, 'type': type_coup, 'pos': position})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if "message" in rep.keys():
            raise RuntimeError(rep['message'])
        if "état" in rep.keys():
            return rep["état"]
        if "gagnant" in rep.keys():
            raise StopIteration(rep["gagnant"])
    print(f"Le POST sur {URL+'jouer coup'} a produit le code d'erreur {rep.status_code}.")
