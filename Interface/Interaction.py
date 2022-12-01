import Graphe

class Interaction :

    def __init__(self, graphe):
    
        self.graphe = graphe
        self.graphe.ajouterNoeud(0, 'Start')

        with open('template.txt','r') as fichier :
            lignes = fichier.readlines()

        for ligne in lignes :
            self.graphe.ajouterNoeud(int(ligne.split(';')[0]), ligne.split(';')[1])

    def questionReponse(self,indice):
    
        print(self.graphe.afficher(indice).texte)
    
        questionNo1 = self.graphe.afficher(indice).filsGauche.numero
        questionNo2 = self.graphe.afficher(indice).filsDroit.numero
        print('(1) ' + self.graphe.afficher(indice).filsGauche.texte)
        print('(2) ' + self.graphe.afficher(indice).filsDroit.texte)
        
        noInteraction = 0
        while noInteraction != "1" and noInteraction != "2" :
            noInteraction = input('What is your choice ? (1 or 2) ')
        
        if (noInteraction == "1") :
            indice = self.graphe.afficher(questionNo1).numero
        else :
            indice = self.graphe.afficher(questionNo2).numero
            
        return indice

#interaction = Interaction(Graphe.Graphe())

#rep = interaction.questionReponse(0)
#rep2 = interaction.questionReponse(rep)
#rep3 = interaction.questionReponse(rep2)
#interaction.questionReponse(rep3)