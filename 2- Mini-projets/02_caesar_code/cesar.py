"""
Miniprojet: Le chiffrement de César
====================================
Programme de chiffrement et déchiffrement utilisant le chiffre de César.
"""

import os
import sys

# Obtenir le répertoire du script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Exercice 1: Génération de l'alphabet avec espace
def generate_alphabet():
    """Génère la liste abc contenant les caractères de 'A' à 'Z' plus l'espace"""
    abc = []

    # A COMPLETER
    return abc


# Exercice 2: Génération de l'alphabet décalé
def generate_cipher_alphabet(abc, shift):
    """Génère l'alphabet décalé pour le chiffrement"""
    abc_cipher = []
    n = len(abc)
    # A COMPLETER

    return abc_cipher


# Question 1: Fonction d'encryption d'une chaîne
def encrypt_string(string, shift):
    """
    Encrypte une chaîne de caractères avec le chiffre de César
    
    Args:
        string: La chaîne à encrypter
        shift: Le décalage à appliquer
        
    Returns:
        La chaîne encryptée en majuscules
    """
    string = string.upper()
    abc = generate_alphabet()
    abc_cipher = generate_cipher_alphabet(abc, shift)
    
    encrypted = []
    # A COMPLETER
    
    return ''.join(encrypted)


# Question 2: Fonction de décryption d'une chaîne
def decrypt_string(string, shift):
    """
    Décrypte une chaîne de caractères chiffrée avec le chiffre de César
    
    Args:
        string: La chaîne à décrypter
        shift: Le décalage utilisé pour l'encryption
        
    Returns:
        La chaîne décryptée
    """
    string = string.upper()
    abc = generate_alphabet()
    abc_cipher = generate_cipher_alphabet(abc, shift)
    
    decrypted = []
    # A COMPLETER
    
    return ''.join(decrypted)


# Question 3: Lecture d'un fichier
def readfile(filename):
    """
    Lit un fichier texte et retourne ses lignes
    
    Args:
        filename: Le nom du fichier à lire
        
    Returns:
        Une liste contenant chaque ligne du fichier
    """
    # Construire le chemin complet dans le répertoire du script
    filepath = os.path.join(SCRIPT_DIR, filename)
    
    # A COMPLETER

    return page


# Question 4: Encryption d'une page
def encrypt_page(page, shift=3):
    """
    Encrypte une liste de lignes de texte
    
    Args:
        page: Liste de chaînes de caractères
        shift: Le décalage (par défaut 3)
        
    Returns:
        Liste des lignes encryptées
    """
    encrypted_page = []
    # A COMPLETER

    return encrypted_page


# Question 5: Décryption d'une page
def decrypt_page(page_cipher, shift=3):
    """
    Décrypte une liste de lignes de texte chiffrées
    
    Args:
        page_cipher: Liste de chaînes encryptées
        shift: Le décalage utilisé (par défaut 3)
        
    Returns:
        Liste des lignes décryptées
    """
    decrypted_page = []
    # A COMPLETER

    return decrypted_page


# Question 6: Sauvegarde dans un fichier
def savefile(filename, page):
    """
    Sauvegarde une liste de lignes dans un fichier
    
    Args:
        filename: Le nom du fichier de sortie
        page: Liste de chaînes à sauvegarder
    """
    # A COMPLETER


# Question 7: Programme principal
if __name__ == '__main__':
    # Test simple
    s = encrypt_string('ABC', 3)
    print(f"Test encryption 'ABC' avec shift=3: {s}")
    
    # Lecture et traitement d'un fichier
    filename = input('Nom du fichier : ')
    
    try:
        # Lecture du fichier original
        page = readfile(filename)
        print("\n=== Contenu original ===")
        for line in page:
            print(line, end='')
        
        # Encryption
        print("\n\n=== Contenu encrypté ===")
        page_cipher = encrypt_page(page)
        for line in page_cipher:
            print(line)
        
        # Décryption (test)
        print("\n=== Contenu décrypté (test) ===")
        page_decrypted = decrypt_page(page_cipher)
        for line in page_decrypted:
            print(line)
        
        # Sauvegarde du fichier encrypté
        tmp = filename.split('.')
        filename_cipher = tmp[0] + '_cipher.' + tmp[1]
        print(f"\n=== Sauvegarde dans {filename_cipher} ===")
        savefile(filename_cipher, page_cipher)
        print("Fichier sauvegardé avec succès!")
        
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{filename}' n'existe pas.")
    except Exception as e:
        print(f"Erreur: {e}")