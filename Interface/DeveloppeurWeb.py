import socket, Interaction, Graphe

TAILLE = 128

separateur = b'|'


def preparer():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print('Description socket : ',s)
    except OSError:
        print('Developer connection failed')
        return(-1)
    else:
        # print('Création socket réussie')
        return(s)


def connecter(sockd, ipClient):
    coord_S = (ipClient, 65432)
    try:
        s.connect(coord_S)
    except ConnectionRefusedError:
        print('Failed to connect to customer')
        return(-1)
    else:
        # print('Connexion au serveur',coord_S,'réussie')
        return(0)


def construire(indice):
    bloc = interaction.questionReponse(indice)
    print("------------------------------------------")
    print("| Waiting for a answer from the customer |")
    print("------------------------------------------\n")
    # print('Requête =',bloc)
    return(str(bloc).encode())


# def utiliser(bloc):
    # print('Réponse reçue = ',bloc)


def echanger(s, indice):
    code_sortie = 0
        
    requete = construire(indice)
    try:
        qte = s.send(requete)
    except (ConnectionResetError,ConnectionAbortedError):
        print('The web developer left unexpectedly')
        return(-1)
    else:    
        # print('Taille requête envoyée = ',qte)
        try:
            reponse = s.recv(TAILLE)
        except ConnectionResetError:
            print('The customer left unexpectedly')
            return(-1)
        else:
            if (len(reponse) == 0):
                print('The customer left the exchange')
                return(-1)
            else:
                indice = reponse
                # utiliser(reponse)
                return indice
   

def arreter(s):
    try:
        s.close()
    except OSError:
        print("---------------\nEND OF THE GAME\n---------------\n")
    else:
        print("---------------\nEND OF THE GAME\n---------------\n")


# programme principal
interaction = Interaction.Interaction(Graphe.Graphe(), 1)
indice = 0

ipDevOk = False
while (not ipDevOk) :
    ipClient = input('Enter the customer\'s IP address - ')
    ipDevOk = input("Is the IP address right for you ? (YES OR NO) - ")
    
    while (ipDevOk != "YES") :
        ipClient = input('Enter the customer\'s IP address - ')
        ipDevOk = input("Is the IP address right for you ? (YES OR NO) - ")
    
    ipDevOk = True

nbquestion = 0
s = preparer()
on_continue = 0
if (s != -1):
    if (connecter(s, ipClient) == 0):
        while (nbquestion != 2):
            nbquestion += 1
            indice = echanger(s, indice)
        interaction.affiche(indice)
        print("End of the exchange")
    arreter(s)