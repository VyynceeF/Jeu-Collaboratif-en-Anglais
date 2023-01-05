import Noeud, unittest

class TestNoeud(unittest.TestCase):
  def test_init(self):
    # Tests du constructeur Noeud
    root = Noeud.Noeud(5, "C'est une question ou une réponse ?")
    self.assertEqual(root.texte, "C'est une question ou une réponse ?")
    self.assertEqual(root.numero, 5)
    self.assertIsNone(root.filsGauche)
    self.assertIsNone(root.filsDroit)

  def test_ajouterNoeud(self):
    # Test méthode ajouterNoeud
    root = Noeud.Noeud(5, "C'est une question ou une réponse ?")
    root.ajouterNoeud(3, "C'est une question")
    root.ajouterNoeud(7, "C'est une réponse")
    self.assertEqual(root.filsGauche.texte, "C'est une question")
    self.assertEqual(root.filsDroit.texte, "C'est une réponse")

  def test_afficher(self):
    # Test méthode afficher
    root = Noeud.Noeud(5, "C'est une question ou une réponse ?")
    root.ajouterNoeud(3, "C'est une question")
    root.ajouterNoeud(7, "C'est une réponse")
    self.assertEqual(root.afficher(3).texte, "C'est une question")
    self.assertEqual(root.afficher(7).texte, "C'est une réponse")
    self.assertEqual(root.afficher(4), "No text found 2")
    self.assertEqual(root.afficher(6), "No text found 1")

  def test_afficheArbreNiveau(self):
    # Test méthode afficherArbreNiveau
    # Ceci affichera l'arborescence de l'arbre sur la console,
    # Vous devrez donc inspecter visuellement la sortie pour déterminer si elle est correcte.
    root = Noeud.Noeud(5, "C'est une question ou une réponse ?")
    root.ajouterNoeud(3, "C'est une question")
    root.ajouterNoeud(7, "C'est une réponse")
    root.afficheArbreNiveau(0)

if __name__ == '__main__':
  unittest.main()



