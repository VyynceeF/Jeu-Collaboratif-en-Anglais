import Noeud, Graphe, unittest

class TestGraphe(unittest.TestCase):
    
	# Graphe utilisé : 
	#              			5
	#			  3					   7
	#	 1										9
    def setUp(self):
        # Création graphe
        self.graphe = Graphe.Graphe()
        
        # Ajout de noeud au graphe 
        self.graphe.ajouterNoeud(5, "Bonjour")
        self.graphe.ajouterNoeud(3, "Hello")
        self.graphe.ajouterNoeud(7, "Hi")
        self.graphe.ajouterNoeud(1, "Hola")
        self.graphe.ajouterNoeud(9, "Salut")
        
    def test_ajouterNoeud(self):
        self.assertEqual(self.graphe.racine.filsGauche.texte, "Hello")
        self.assertEqual(self.graphe.racine.filsDroit.texte, "Hi")
        self.assertEqual(self.graphe.racine.filsGauche.filsGauche.texte, "Hola")
        self.assertEqual(self.graphe.racine.filsDroit.filsDroit.texte, "Salut")
    
	
    def test_afficher(self):
        self.assertEqual(self.graphe.afficher(5).texte, "Bonjour")
        self.assertEqual(self.graphe.afficher(3).texte, "Hello")
        self.assertEqual(self.graphe.afficher(7).texte, "Hi")
        self.assertEqual(self.graphe.afficher(1).texte, "Hola")
        self.assertEqual(self.graphe.afficher(9).texte, "Salut")
		
		# Graphe utilisé : 
		#              			5
		#------------------------------------------------
		#			  3					   7
		#------------------------------------------------
		#	 1						6			    9
		#------------------------------------------------
		#         2                             8
        #------------------------------------------------
		
		# 2 --> ajout sur un fils droit donc méthode afficher doit retourner No Text Found 2
        self.assertEqual(self.graphe.afficher(2), "No text found 2")
		
		# 8 --> ajout sur un fils gauche donc méthode afficher doit retourner No Text Found 1
        self.assertEqual(self.graphe.afficher(8), "No text found 1")
		
        # création d'un graphe nul pour tester le cas de afficher quand la racine est null
        self.grapheNul = Graphe.Graphe(); 
        self.assertEqual(self.grapheNul.afficher(1), "No text found")
           
   
print("--------------------------------")
print("|Test sur la classe Graphe      | ")
print("--------------------------------")

if __name__ == '__main__':
	unittest.main()  