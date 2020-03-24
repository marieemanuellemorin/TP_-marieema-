import requests

url_base = 'https://python.gel.ulaval.ca/quoridor/api'

def lister_parties(idul):
    rep = requests.get(f'{url_base}/lister/', params={'idul': f'{idul}'})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        
        rep = rep.json()
        
        if "message" in rep.keys():
            raise RuntimeError(rep['message'])
        else:
            return rep
    
    else:
        print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")

#fonction initialiser_partie
def initialiser_partie(idul):
    rep = requests.post(f'{url_base}/initialiser/', data={'idul': f'{idul}'})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        
        if "message" in rep.keys():
            raise RuntimeError(rep['message'])
        else:
            identifiant = rep['id'] 
            etat = rep['état']

            return((identifiant, etat))
    
    else:
        print(f"Le POST sur {url_base+'initialiser'} a produit le code d'erreur {rep.status_code}.")

#Fonction jouer_coup
def jouer_coup(id_partie, type_coup, position):
    rep = requests.post(f'{url_base}/jouer/', data={'id': id_partie, 'type': type_coup, 'pos': position}) 
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json() 
        if "message" in rep.keys():
            raise RuntimeError(rep['message']) 
        
        if "état" in rep.keys():
            return rep["état"]
   
        if "gagnant" in rep.keys():
            raise StopIteration(rep["gagnant"])
        
    else:
        print(f"Le POST sur {url_base+'jouer coup'} a produit le code d'erreur {rep.status_code}.")
