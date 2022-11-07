import socket

def preparer():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print('Description socket : ',s)
    except OSError :
        print('Création socket échouée')
        return(-1)
    else:
        coord_S = ('127.0.0.1', 65432)
        try:
            s.bind(coord_S)
        except OSError:
            print('bind() échoué')
            s.close()
            return(-1)
        else:
            print('bind() réussi')
            s.listen(1)
            return s
            
def accepter(s):
    try:
        (s_comm, coord_C) = s.accept()
    except OSError:
        print('Erreur acceptation')
    else:
        print('Acceptation effectuer')
        return s_comm

def analyser(requete):
    print('Requête reçue = ',requete)
    print('Analyse requête effectuée')
    return requete # pas d'analyse, on retourne ce qu'on a reçu

def construire(s_comm):
    try:
        requete = s_comm.recv(1024)
    except OSError or ConnectionResetError:
        print('Construction impossible')
    else:
        reponse = requete
        print('Construction réponse effectuée')
        return reponse # on retourne ce qu'on a reçu car "écho"

def echanger(s):
    try:
        s_comm = accepter(s)
        requete = s_comm.recv(1024)
    except ConnectionResetError: # Note : spécifique Windows et avec adresse de rebouclage
        print('recv(): le client est absent ou parti')
        return(-1)
    except OSError:
        print('Requête reçue refusée car trop volumineuse')
        return(-1)
    else:
        requete = analyser(requete)
        reponse = construire(s_comm)
        try:
            qte = s_comm.send(reponse)
        except OSError: # Note : ne devrait jamais arriver ici car réponse = requête et requête déjà filtrée
            print('Envoi réponse refusé car réponse trop volumineuse')
            return(-1)
        else:    
            print('Taille réponse envoyée = ',qte)
            return(0)
    

def arreter(s):
    try:
        s_comm.close()
        s.close()
    except OSError:
        print('Socket encore ouverte !')
    else:
        print('Socket correctement fermée')


# programme principal
s = preparer()
if (s!=-1):
    echanger(s)
    arreter(s)