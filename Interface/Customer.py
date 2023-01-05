import socket, Interaction, Graphe

TAILLE = 128

separateur = b'|' 

global cpt

# permet :   - créer un socket avec une adresse IPv4 et un protocole TCP
#		     - configurer la socket avec les coordonnées de la machine (@IP) et un port.
#		     - ensuite écoute 1 machine à la fois.
def preparer():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print(s)
    except OSError:
        print('Socket creation failed')
        return(-1)
    else:
        # print('Création socket réussie')
        print("--------------------------------------------------------------")
        print("IP address to give to the Web developer - " + socket.gethostbyname(socket.gethostname()))
        print("--------------------------------------------------------------\n")
        
        # récupere l'adresse ip et le port d'écoute de le socket
        coord_S = (socket.gethostbyname(socket.gethostname()), 65432)
        try:
            # initialise le socket avec les coordonnées initialisé précedement (IP,Port)
            s.bind(coord_S)
        except OSError:
            print('bind() failed')
            s.close()
            return(-1)
        else:
            # le bind a bien été réussi
            try: 
                # on écoute une socket à la fois
                s.listen(1)
            except OSError:
                print('listen() failed')
                s.close()
                return(-1)
            else:
                # listen() réussi'
                return(s)

# permet d'accepter connexion à un socket entré en paramétre.
def accepter(sockd):
    print("Waiting for a web developer")
    try:
        (s, coord_C)= sockd.accept()
    except OSError:
        print('Failed to connect to Web developer')
        return(-1)
    else:
        # accept() réussi pour le client', coord_C)
        print('The web developer is connected\n')

        print("\n----------------------------\n    Start of the game\n----------------------------") 
        return(s)

# Retranscrit le bloc de donnée en paramétre en une chaine de caractère
def analyser(bloc):
    # print('Requête reçue = ',bloc.decode())
    return(bloc.decode())

# Appelle la classe Interaction pour construire une réponse au message 
def construire(message):
    rep = interaction.questionReponse(message)
    # print('Construction réponse effectuée')
    return str(rep).encode()

# Permet de communiquer avec le  developpeur web, 
# la méthode attend une réponse du developpeur web 
#analyse le message reçu et construire la réponse que va recevoir le client.
# retourne -1 si il y a eu un echec durant la communication sinon retourne 0 
def echanger(s_comm, cpt):
    code_sortie = 0
    if cpt < 3:
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

# permet d'arrete le socket mis en paramétre
def arreter(s, nom):
    try:
        s.close()
    except OSError:
        print()
    


# programme principal

interaction = Interaction.Interaction(Graphe.Graphe(), 0)
cpt = 0
print("--------------- CONTEXT --------------- \n")
print("The two players in this game are a developer and a customer. The customer wants to create a website. He calls on an external company specializing in web development and user interfaces to delegate this work. His company does not have the resources to create the website. The web developer contacts the customer\'s to obtain information to optimize the development and better understand the customer's needs.To do this, they use a communication software in which the web developer has already prewritten 10 questions to ask the client. As this software works interactively, the developer and the client have to use it simultaneously. ")
print("--------------------------------------- \n")
print("---------------  RULES  --------------- \n")
print("1.	The Developer chooses between two questions.")
print("2.	The Developer can choose only one of the two proposed questions.")
print("3.	The Player answers the question.")
print("4.	The Player can choose between one of the two proposed answers.")
print("5.	The Game does not deal with the time to answer questions and ask questions also for the choice of questions for the Developer.")
print("6.	If the Player leaves the game wildly, then the game stops.")
print("7.	If the Developer leaves the game wildly, then the game stops.")
print("8.	The Game ends when the Customer has answered the second question.")
print("--------------------------------------- \n")
s1 = preparer()
on_continue = 0
if (s1 != -1 ):
    s2 = accepter(s1)
    if (s2 != -1 ):
        while (on_continue == 0):
            cpt = cpt + 1
            on_continue = echanger(s2, cpt)
        arreter(s2,'Web developer')
    arreter(s1,'Player')
print("---------------\nEND OF THE GAME\n---------------\n")

input("Press Enter to quit ?")