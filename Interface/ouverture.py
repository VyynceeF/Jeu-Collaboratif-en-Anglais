import Graphe

graphe = Graphe.Graphe()

with open('template.txt','r') as fichier :
    lignes = fichier.readlines()

for ligne in lignes :
    graphe.ajouterNoeud(int(ligne.split(';')[0]), ligne.split(';')[1])

