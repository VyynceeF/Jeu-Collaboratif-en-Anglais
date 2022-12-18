import Graphe

class Interaction :

    def __init__(self, graphe, noUtilisateur):
    
        self.noUtilisateur = noUtilisateur
        self.graphe = graphe
        self.graphe.ajouterNoeud(0, '\n----------------------------\n    Start of the game\n----------------------------')

        with open('template.txt','r') as fichier :
            lignes = fichier.readlines()

        for ligne in lignes :
            self.graphe.ajouterNoeud(int(ligne.split(';')[0]), ligne.split(';')[1])

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
     
    def affiche(self, indice):
        print(self.graphe.afficher(indice).texte)



#rep = interaction.questionReponse(0)
#rep2 = interaction.questionReponse(rep)
#rep3 = interaction.questionReponse(rep2)
#interaction.questionReponse(rep3)