import socket, Interaction, GrapheTAILLE = 128separateur = b'|'def preparer():    try:        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        print('Description socket : ',s)    except OSError:        print('Création socket échouée')        return(-1)    else:        print('Création socket réussie')        return(s)def connecter(sockd):    coord_S = ('127.0.0.1', 65432)    try:        s.connect(coord_S)    except ConnectionRefusedError:        print('Connexion au serveur',coord_S,'échouée')        return(-1)    else:        print('Connexion au serveur',coord_S,'réussie')        return(0)def construire(indice):    bloc = interaction.questionReponse(indice)    print('Requête =',bloc)    return(str(bloc).encode())def utiliser(bloc):    print('Réponse reçue = ',bloc)    print('Utilisation de la réponse effectuée')def echanger(s, indice):    code_sortie = 0    requete = construire(indice)    try:        qte = s.send(requete)    except (ConnectionResetError,ConnectionAbortedError):        print('send() : le serveur a quitté sauvagement')        return(-1)    else:            print('Taille requête envoyée = ',qte)        try:            reponse = s.recv(TAILLE)        except ConnectionResetError:            print('recv(): le serveur a quitté sauvagement')            return(-1)        else:            if (len(reponse) == 0):                print('recv(): le serveur a quitté proprement')                return(-1)            else:                indice = reponse                utiliser(reponse)                return indice   def arreter(s):    try:        s.close()    except OSError:        print('Socket encore ouverte !')    else:        print('Socket correctement fermée')# programme principalinteraction = Interaction.Interaction(Graphe.Graphe())indice = 0nbquestion = 0s = preparer()on_continue = 0if (s != -1):    if (connecter(s) == 0):        while (nbquestion != 2):            nbquestion += 1            indice = echanger(s, indice)        print("Fin")    arreter(s)