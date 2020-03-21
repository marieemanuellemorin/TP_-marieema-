def lister_parties(idul):

    import requests

    url_base = 'https://python.gel.ulaval.ca/quoridor/api'

    rep = requests.get(f'{url_base}/lister/', params={'idul': 'xxxxx'})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        
        rep = rep.json()
        print(rep)
    
    else:
        print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")
