"""
importation de module pour éliminer la ponctuation et les accents
"""
import string
from unidecode import unidecode

#### Fonction secondaire


def ispalindrome(p):
    """
    création d'une fonction qui détermine si une chaine de caractères est un palindrome
    """
    p4=p.translate(str.maketrans('', '', string.punctuation))
    p3=p4.lower()
    p2=unidecode(p3)
    p1=p2.replace(" ","")
    if len(p1)<=1:
        return True
    if p1[0]==p1[-1]:
        return ispalindrome(p1[1:-1])
    return False


#### Fonction principale

def main():
    """
    fonction principale qui teste la fonction ispalindrome
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
