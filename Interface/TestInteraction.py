import unittest
from Interaction import Interaction
from Graphe import Graphe
from unittest.mock import patch

class TestInteraction(unittest.TestCase):
    def setUp(self):
        self.graphe = Graphe()
        self.interaction = Interaction(self.graphe)
        
    def test_question_reponse(self):
        # Test initial question réponse
        # si on choisi 1 --> alors -1000 comme indice
        with patch('builtins.input', return_value='1'):
            indice = self.interaction.questionReponse(0)
            # on a simulé que l'utilisateur choisissait 2 donc on va comparer avec le fils gauche
            self.assertEqual(indice, self.graphe.afficher(0).filsGauche.numero)
            print("choix : 1")
            
        
        # si on choisi 2 --> alors 1000 comme indice
        with patch('builtins.input', return_value='2'):
            indice = self.interaction.questionReponse(0)
            # on a simulé que l'utilisateur choisissait 2 donc on va comparer avec le fils droit
            self.assertEqual(indice, self.graphe.afficher(0).filsDroit.numero)
            print("choix : 2")
        
        
    
if __name__ == '__main__':
    unittest.main()