class Noeud :

    def __init__(self, indice, questionReponse) :
        
        self.texte = questionReponse
        self.numero = indice
        self.filsGauche = None
        self.filsDroit = None
        
    def ajouterNoeud(self, indice, questionReponse) :
        
        if indice < self.numero :
            if self.filsGauche == None :
                self.filsGauche = Noeud(indice, questionReponse)
            else :
                self.filsGauche.ajouterNoeud(indice, questionReponse)
        
        if self.filsDroit == None :
            self.filsDroit = Noeud(indice, questionReponse)
        else :
            self.filsDroit.ajouterNoeud(indice, questionReponse)