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
        else :
            print('\n----------------------------\n     Choose your answer\n----------------------------')
        questionNo1 = self.graphe.afficher(indice).filsGauche.numero
        questionNo2 = self.graphe.afficher(indice).filsDroit.numero
        print('(1) ' + self.graphe.afficher(indice).filsGauche.texte)
        print('(2) ' + self.graphe.afficher(indice).filsDroit.texte)
        
        noInteraction = input('What is your choice ? (1 or 2) - ')
        while noInteraction != "1" and noInteraction != "2" :
            noInteraction = input('Input error ! What is your choice ? (1 or 2) - ')
        
        if (noInteraction == "1") :
            indice = self.graphe.afficher(questionNo1).numero
        else :
            indice = self.graphe.afficher(questionNo2).numero
            
        return indice
     
    def affiche(self, indice):
        print(self.graphe.afficher(indice).texte)

#interaction = Interaction(Graphe.Graphe())

#rep = interaction.questionReponse(0)
#rep2 = interaction.questionReponse(rep)
#rep3 = interaction.questionReponse(rep2)
#interaction.questionReponse(rep3)