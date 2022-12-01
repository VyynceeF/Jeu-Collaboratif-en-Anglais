import socket, Interaction, Graphe

TAILLE = 128

separateur = b'|' 

def preparer():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print(s)
    except OSError:
        print('Socket creation failed')
        return(-1)
    else:
        # print('Création socket réussie')
        coord_S = ('127.0.0.1', 65432)
        try:
            s.bind(coord_S)
        except OSError:
            print('bind() failed')
            s.close()
            return(-1)
        else:
            # print('bind() réussi')
            try: 
                s.listen(1)
            except OSError:
                print('listen() failed')
                s.close()
                return(-1)
            else:
                # print('listen() réussi')
                return(s)


def accepter(sockd):
    print("Waiting for a web developer")
    try:
        (s, coord_C)= sockd.accept()
    except OSError:
        print('accept() failed')
        return(-1)
    else:
        # print('accept() réussi pour le client', coord_C)
        print('The web developer is connected')
        return(s)


def analyser(bloc):
    # print('Requête reçue = ',bloc.decode())
    return(bloc.decode())


def construire(message):
    rep = interaction.questionReponse(message)
    # print('Construction réponse effectuée')
    return str(rep).encode()


def echanger(s_comm):
    code_sortie = 0
    print("------------------------------------------------")
    print("| Waiting for a question from the web developer |")
    print("------------------------------------------------\n")
    try:
        requete = s_comm.recv(TAILLE)
    except ConnectionResetError:
        print('The web developer left unexpectedly')
        return(-1)
    else:
        if (len(requete) == 0):
            print('The web developer left the exchange')
            return(-1)
        else:
            message = analyser(requete)
            reponse = construire(message)
            try:
                print('\n')
                qte = s_comm.send(reponse)
            except (ConnectionResetError,ConnectionAbortedError):
                print('The web developer left unexpectedly')
                return(-1)
            else:
                # print('Taille réponse envoyée = ',qte)
                return(code_sortie)


def arreter(s, nom):
    try:
        s.close()
    except OSError:
        print(nom,'still connected !')
    else:
        print(nom + " disconnected : end of exchange")


# programme principal

interaction = Interaction.Interaction(Graphe.Graphe())

cpt = 0
s1 = preparer()
on_continue = 0
if (s1 != -1 ):
    s2 = accepter(s1)
    if (s2 != -1 ):
        while (on_continue == 0):
            on_continue = echanger(s2)
        arreter(s2,'Web developer')
    arreter(s1,'Player')