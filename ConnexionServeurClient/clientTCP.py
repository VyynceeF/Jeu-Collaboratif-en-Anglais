import socket

def preparer():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Description socket : ',s)
    except OSError:
        print('Création socket échouée')
        return(-1)
    else:
        print('Création socket réussie')
        coord_S = ('127.0.0.1', 65432)
        return s

def connecter(coord_S):
    try:   
        s.connect(coord_S)
    except ConnectRefuseError:
        print('Erreur')
    else:
        print('Connection Ok')
    

def construire():
    requete = input('Saisie requete : ')
    print('Construction réponse effectuée')
    return requete # on retourne ce qu'on a reçu car "écho"

def utiliser(reponse):
    print('reponse = ' + reponse)

def echanger(s):
    coord_S = ('127.0.0.1', 65432)
    connecter(coord_S)
    requete = construire()
    qte = s.send(requete.encode())
    print('Taille requete envoyée = ',qte)
    try:
        reponse = s.recv(1024)
    except ConnectionResetError: # Note : spécifique Windows et avec adresse de rebouclage
        print('recvfrom(): le serveur est absent ou parti')
        return(-1)
    else:
        utiliser(reponse)

def arreter(s):
    try:
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
