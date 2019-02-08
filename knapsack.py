import csv
import numpy as np
import numpy.linalg as alg

class Objets:
    def __init__(self, n, po, p):
        self.nom = n 
        self.poids = po        
        self.prix = p
        self.rapport = po/p
    
    def __repr__(self):
        return "[OBJET: nom({}), poids({}), prix({}), rapport({})]".format(
                self.nom, self.poids, self.prix, self.rapport)

    def getRapport(self):
        return self.rapport

    def getPoids(self):
        return self.poids

    def getPrix(self):
        return self.prix

    def getNom(self):
        return self.nom

class Sac:
    def __init__(self,c):
        self.capacite = c
        self.contenu = []
        self.valeur = 0
        self.poids = 0
    
    def __repr__(self):
        return "[SAC: capacite({}), contenu({})]".format(
                self.capacite, self.contenu)

    def getCapacite(self):
        return self.capacite

    def getValeur(self):
        return self.valeur

    def getPoids(self):
        return self.poids

    def insererObjet(self, objet): 
        if(not(self.poids + objet.getPoids() > self.capacite)):
            self.contenu.append(objet)
            self.poids = self.poids + objet.getPoids()
            self.valeur = self.valeur + objet.getPrix()
    
    def insererForce(self, objet):
        self.contenu.append(objet)
        self.poids = self.poids + objet.getPoids()
        self.valeur = self.valeur + objet.getPrix()

    def getLen(self):
        return len(self.contenu)

    def getObjet(self, i):
        return self.contenu[i]
            
    

def greedy(filepath_in, filepath_out, size_bag):
    caractere = ";"
    tab = []
    with open(filepath_in, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            chaine = " ".join(row)
            split = chaine.split(caractere)
            s1 = split[1]
            s2 = split[2]
            index = s1.find('.')
            if(index == -1):
                split[1] = int(split[1])
            else:
                split[1] =float(split[1])

            index = s2.find('.')

            if(index == -1):
                split[2] = int(split[2])
            else:
                split[2] = float(split[2])

            objet = Objets(split[0], split[1], split[2])
            tab.append(objet)

        tri(tab)
        sac = Sac(size_bag)

        for i in range(0, len(tab)):
            sac.insererObjet(tab[i])

        with open(filepath_out, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for j in range (0, sac.getLen()):
                spamwriter.writerow([sac.getObjet(j).getNom()] + [sac.getObjet(j).getPoids()] + [sac.getObjet(j).getPrix()])

        return sac.getValeur(), sac.getPoids(), sac.getLen()


 

def repartition(tab, premier, dernier, p):
    tab[p],tab[dernier] = tab[dernier],tab[p]
    j = premier
    for i in range(premier, dernier):
        if(tab[i].getRapport() <= tab[dernier].getRapport()):
            tab[i],tab[j] = tab[j],tab[i]
            j = j + 1
    tab[dernier],tab[j] = tab[j],tab[dernier]
    return (tab, j)

def tri_fusion(tab, premier, dernier):
    if(premier < dernier):
        p = (premier + dernier) // 2 
        tab,j = repartition(tab, premier, dernier, p)
        tab = tri_fusion(tab, premier, j-1)
        tab = tri_fusion(tab, j+1 ,dernier)
    return tab

def tri(tab):
    return tri_fusion(tab, 0, len(tab) - 1)

def dynamique(filepath_in, filepath_out, size_bag):
    caractere = ";"
    tabDy = []
    with open(filepath_in, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            chaine = " ".join(row)
            split = chaine.split(caractere)
            s1 = split[1]
            s2 = split[2]
            index = s1.find('.')
            if(index == -1):
                split[1] = int(split[1])
            else:
                split[1] =float(split[1])

            index = s2.find('.')

            if(index == -1):
                split[2] = int(split[2])
            else:
                split[2] = float(split[2])

            objet = Objets(split[0], split[1], split[2])
            tabDy.append(objet)

    matrice = np.zeros((len(tabDy), size_bag + 1))

    for i in range(0, size_bag + 1):
        matrice[0][i] = 0
    
    for i in range(0, len(tabDy)):
        matrice[i][0] = 0

    for i in range (1,len(tabDy)):
        for j in range (0, size_bag +1):
            if(tabDy[i].getPoids() <= j):
                if(tabDy[i].getPrix() + matrice[i-1][j- int(tabDy[i].getPoids())] > matrice[i-1][j]):
                    matrice[i][j] = tabDy[i].getPrix() + matrice[i-1][j- int(tabDy[i].getPoids())]
                else:
                    matrice[i][j] = matrice[i-1][j]
            else:
                matrice[i][j] = matrice[i-1][j]

    sacDy = Sac(size_bag)
    print(matrice)
    i = len(tabDy) -1
    j = size_bag
    poids = 0

    while i > 0 and j > 0: 
        if(matrice[int(i)][int(j)] != matrice[int(i-1)][int(j)]):
            sacDy.insererObjet(tabDy[i])
            poids = poids + tabDy[i].getPoids()

            i = i -1
            j = j - tabDy[i].getPoids()
        else:
            i = i -1
    print(sacDy)
    print(poids)
    with open(filepath_out, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for j in range (0, sacDy.getLen()):
                spamwriter.writerow([sacDy.getObjet(j).getNom()] + [sacDy.getObjet(j).getPoids()] + [sacDy.getObjet(j).getPrix()])

    return sacDy.getValeur(), sacDy.getPoids(), sacDy.getLen()
    

#greedy('petit_sac.csv', 'petit_sac_tri.csv', 30)
dynamique('petit_sac.csv', 'petit_sac_tr.csv', 30)