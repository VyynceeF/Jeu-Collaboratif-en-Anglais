import Noeud

class Graphe :
    # initialise la racine du graphe à null 
    def __init__(self):
        
        self.racine = None
    # ajoute un Noeud de paramètre (indice, questionReponse) dans le graphe    
    def ajouterNoeud(self, indice, questionReponse,) :
        
        if self.racine == None :
            self.racine = Noeud.Noeud(indice, questionReponse)
        else :
            self.racine.ajouterNoeud(indice, questionReponse)
            
    # effectue une recherche pour trouver le Noeud à la position noATrouver
    # retourne la question qui se trouve à l'indice noAtrouver.
    def afficher(self, noATrouver) :
        
        if self.racine == None :
            return "No text found"
        else :
            return self.racine.afficher(noATrouver)
          
