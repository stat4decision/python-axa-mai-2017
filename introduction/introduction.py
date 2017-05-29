# coding: utf-8

int1=5
float1=4.5
bool1=True
str1="data"

str2="Python pour la Science"

list1=[2,4,6,7,"Direct"]

list_celsius=[0,10,20,33]
list_fahrenheit=[9/5*temp +32 for temp in list_celsius]

str3="Vive la data science"

list3=str3.split(" ")

list3=list3+["et", "python"]

list3.extend(["et", "python"])

for indice in ["et", "python"]:
    list3.append(indice)


# Créez la chaîne ‘Ce client est …, il a … ans d’ancienneté et a dépensé … euros’. On utilisera les %... dans la chaîne que l’on pourra remplacer par différentes valeurs

str_client="Ce client s'appelle %s, il a %i ans d'ancienneté et a dépensé %.2f euros"


# Construire un dictionnaire composé de listes de mots et accédez à un élément d’une des listes du dictionnaire.  Affichez le mot en majuscule.

dico1={"Pays":["France", "Suisse", "USA"], "Villes":["Paris","New York"]}

# ### Les fonctions

def test2(a:int,b:float,*args):
    """
    Cette fonction prend un nombre indéfini d'éléments en entrée et les extrait
    dans une liste
    """
    list4=[]
    for indice in args:
        list4.append(indice)
    #print(a,b,list4)
    return a,b,list4

a,b,list_autres=test2("zer","abc",4,5,6)

f=lambda x,y : x**2+x*y

sep_et_maj=lambda str1:str1.upper().split(" ")

def moyenne_listes(list1:list,list2:list):
    return sum(list1+list2)/len(list1+list2)


def moyenne_listes2(list1:list,list2:list):
    somme=0.0
    for indice in list1+list2:
        somme+=indice
    return somme/len(list1+list2)

moy_listes=moyenne_listes([i**2 for i in range(5)],[2,3,5])

# ### Les classes

# Définir une classe Client qui s’initialise avec comme variable nouveau_client et ville. 
# Créer un objet client1 et affichez les valeurs allouées
# 
class Client:
    def __init__(self, nouveau_client=True,ville="Suresnes"):
        self.nouveau_client=nouveau_client
        self.ville= ville

    def affiche_client(self):
        if self.nouveau_client==True:
            print("Ce client est un nouveau client qui vient de",self.ville)
        else:
            print("Ce client est un ancien client qui vient de",self.ville)
    
    def demenagement(self,nouvelle_ville):
        self.ville=nouvelle_ville



# Définissez une classe CompteBancaire(), qui permette d'instancier des objets tels que compte1, compte2, etc. 
# Le constructeur de cette classe initialisera deux attributs d'instance nom et solde, avec les valeurs par défaut ‘A' et 0.
# 
# Trois autres méthodes sont définies :
# - depot(somme) permettra d'ajouter une certaine somme au solde
# - retrait(somme) permettra de retirer une certaine somme du solde
# - affiche() permettra d'afficher le solde du compte et un message d’alerte en cas de solde négatif. 
# 

class CompteBancaire:
    """
    Classe pour créer un objet du type compte bancaire
    """
    def __init__(self, nom="Moi",solde=0):
        self.nom=nom
        self.solde=solde

    def depot(self,somme):
        self.solde+=somme

    def retrait(self,somme):
        self.solde-=somme

    def affiche(self):
        """
        Méthode affichant le solde
        """
        if self.solde<0:
            print("Attention solde négatif")
        else:
            print(self.solde)