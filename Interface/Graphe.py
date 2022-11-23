import Noeud

class Graphe :

    def __init__(self):
        
        self.racine = None
        
    def ajouterNoeud(self, indice, questionReponse,) :
        
        if self.racine == None :
            self.racine = Noeud.Noeud(indice, questionReponse)
        else :
            self.racine.ajouterNoeud(indice, questionReponse)
            

    def afficher(self, noATrouver) :
        
        if self.racine == None :
            return "Aucun texte trouvé"
        else :
            return self.racine.afficher(noATrouver)
          
