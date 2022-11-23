class Noeud :

    def __init__(self, indice, questionReponse) :
        
        self.texte = questionReponse
        self.numero = int(indice)
        self.filsGauche = None
        self.filsDroit = None
        
    def ajouterNoeud(self, indice, questionReponse) :
        
        if indice < self.numero :
            if self.filsGauche == None :
                self.filsGauche = Noeud(indice, questionReponse)
            else :
                self.filsGauche.ajouterNoeud(indice, questionReponse)
        else :
            if self.filsDroit == None :
                self.filsDroit = Noeud(indice, questionReponse)
            else :
                self.filsDroit.ajouterNoeud(indice, questionReponse)
       
    def afficher(self, noATrouver) :
    
        if noATrouver == self.numero :
            return self
        
        if int(noATrouver) < self.numero :
            if self.filsGauche == None :
                return "Aucun texte trouvé 1"
            else :
                return self.filsGauche.afficher(int(noATrouver))
        else :
            if self.filsDroit == None :
                return "Aucun texte trouvé 2"
            else :
                return self.filsDroit.afficher(int(noATrouver))
        
        return None
        
    def afficheArbreNiveau(self, niveau) :
        
        if (self.filsDroit != None) :
            self.filsDroit.afficheArbreNiveau(niveau + 1)
            
        for i in range (0, niveau * 5) :
            print(' ', end='')
        print(self.numero)
        
        if (self.filsGauche != None) :
            self.filsGauche.afficheArbreNiveau(niveau + 1)