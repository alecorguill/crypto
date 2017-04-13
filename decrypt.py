from permutation import *


def decrypt(n,fichier_crypt, fichier_decrypt):
    f_crypt = open(fichier_crypt,"r")
    contenu_crypt = f_crypt.read()
    f_decrypt = open(fichier_decrypt, 'a')
    for perm in permutations(range(n)):
        stri = ''.join(str(perm[i]) for i in range(n))
        f_decrypt.write(stri + '\n')
        f_decrypt.write(construct_decrypt(perm,contenu_crypt) + '\n\n')
    f_crypt.close()
    f_decrypt.close()
    return

def construct_decrypt(perm, text_crypt):
    text_decrypt = ""
    text_decrypt = list(text_decrypt)
    text_crypt = list(text_crypt)
    n = len(perm)
    l = len(text_crypt) - 1
    l -= l%n
    for i in range(l):
        text_decrypt.append('0')
    
    for i in range(l):
        r = i%n
        q = i//n
        text_decrypt[perm[r]+q*n] = text_crypt[i]
    return ''.join(text_decrypt)

decrypt(3,"test.txt","res.txt")        

    
