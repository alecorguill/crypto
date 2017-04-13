
import numpy as np
import collections as c
import re

tab_lettre = ['a','b','c','d','e','f','g','h',
                   'i','j','k','l','m','n','o','p',
                   'q','r','s','t','u','v','w','x',
                   'y','z']


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def frequency(text,tab_lettre):
    taille=len(text)
    res = {}
    for lettre in tab_lettre:
        res[lettre]= 0
    for i in range(taille):
        if(text[i].isalpha()):
            res[text[i]]+= 1
    return res

def indice(text):
    somme = 0
    n = len(text)
    tab_occ = frequency(text, tab_lettre)
    for lettre in tab_lettre:
        n_lettre = tab_occ[lettre]
        somme += float(n_lettre*(n_lettre-1))/ (n*(n-1))
    return somme

def indice_block(block_len, fichier_crypt):
    f_crypt = open(fichier_crypt,"r")
    contenu_crypt = f_crypt.read()
    tab_indice = []
    n_block = len(contenu_crypt) / block_len
    for i in range(n_block):
        tab_indice.append(indice(contenu_crypt[i*block_len:(i+1)*block_len]))
    f_crypt.close()
    return tab_indice

'''
for i in [2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500]:
    print(i, indice_block(i,"text_crypt.txt"))
    print("\n")
'''



def string_in_string(str2,str1):
    for m in re.finditer(str2, str1):
         print(str2 + 'found', m.start(), m.end())

def distance_trigramme(trig, fichier_crypt):
    f_crypt = open(fichier_crypt,"r")
    contenu_crypt = f_crypt.read()
    string_in_string(trig,contenu_crypt)
    f_crypt.close()
    return


#distance_trigramme('uen',"text_crypt.txt")
