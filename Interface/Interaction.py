import Graphe

class Interaction :
    
    # Constructeur qui initialise le graphe pour les questions et le numéro de l'utilisateur : 
    # 1 = client
    # 0 = développeur web
    # Ajoute au graphe un noeud racine initialisé à 0 pour marquer le début du jeu.
    def __init__(self, graphe, noUtilisateur):
    
        self.noUtilisateur = noUtilisateur
        self.graphe = graphe
        self.graphe.ajouterNoeud(0, '\n----------------------------\n    Start of the game\n----------------------------')

        with open('template.txt','r') as fichier :
            lignes = fichier.readlines()

        for ligne in lignes :
            self.graphe.ajouterNoeud(int(ligne.split(';')[0]), ligne.split(';')[1])



    # Permet d'afficher en fonction de l'indice soit 
    #   - choix question/réponse en fonction du noUtilisateur
    #   - à qui est le tour de jouer
    #   - affiche les questions/réponses possibles à partir de l'indice
    #   - demande la saisie d'une réponse 1 ou 2 avec vérification de la saisie en cas d'erreur de l'utilisateur
    #   retourne le nouvelle indice 
    def questionReponse(self,indice):
    
        if (self.noUtilisateur == 1 and indice != 0) :
            print('\n----------------------------\n     Answer of customer\n----------------------------')
        elif (self.noUtilisateur == 0 and indice != 0) :
            print('\n----------------------------\n  Question of Web developer\n----------------------------')
        self.affiche(indice)
    
        if (self.noUtilisateur == 1) :
            print('\n----------------------------\n    Choose your question\n----------------------------')
            user = "Web developer"
        else :
            print('\n----------------------------\n     Choose your answer\n----------------------------')
            user = "customer"
        questionNo1 = self.graphe.afficher(indice).filsGauche.numero
        questionNo2 = self.graphe.afficher(indice).filsDroit.numero
        print('(1) ' + self.graphe.afficher(indice).filsGauche.texte)
        print('(2) ' + self.graphe.afficher(indice).filsDroit.texte)
        
        noInteractionOk = False
        while (not noInteractionOk) :
            noInteraction = input('What is your choice ? (1 or 2) - ')
            # Test si l'entree du joueur est bien egale a '1' ou '2'
            if (noInteraction == '1' or noInteraction == '2') :
                # Demande a l'utilisateur s'il valide son choix
                # Do you want to send choice 1 to the customer ?
                noInteractionOkUser = input('Do you want to send choice ' + noInteraction + ' to the ' + user + ' ? (YES OR NO) - ')
                if (noInteractionOkUser == 'YES') :
                    noInteractionOk = True
            # Erreur de saisie
            else : 
                print('Input error !')
        
        if (noInteraction == "1") :
            indice = self.graphe.afficher(questionNo1).numero
        else :
            indice = self.graphe.afficher(questionNo2).numero
            
        return indice
    
    # appelle la méthode afficher de la classe Graphe avec en paramètre l'indice 
    # qui elle même appelle la méthode afficher de la classe Noeud si la racine n'est pas null.
    def affiche(self, indice):
        print(self.graphe.afficher(indice).texte)



#rep = interaction.questionReponse(0)
#rep2 = interaction.questionReponse(rep)
#rep3 = interaction.questionReponse(rep2)
#interaction.questionReponse(rep3)