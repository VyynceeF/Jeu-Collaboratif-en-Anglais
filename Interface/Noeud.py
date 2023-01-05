class Noeud :
    # Initalise le filsDroit et filsGauche du Noeud courant à null .
    # Initialise le numéro du noeud et la question ou réponse du Noeud .
    def __init__(self, indice, questionReponse) :
        
        self.texte = questionReponse
        self.numero = int(indice)
        self.filsGauche = None
        self.filsDroit = None


    # Effectue une recherche à partir du noeud courant 
    # pour ajouter le noeud du bon côté de l'arbre.        
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


    # Affiche la question/reponse au noeud d'indice noATrouver .
    def afficher(self, noATrouver) :
    
        if noATrouver == self.numero :
            return self
        
        if int(noATrouver) < self.numero :
            if self.filsGauche == None :
                return "No text found 1"
            else :
                return self.filsGauche.afficher(int(noATrouver))
        else :
            if self.filsDroit == None :
                return "No text found 2"
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