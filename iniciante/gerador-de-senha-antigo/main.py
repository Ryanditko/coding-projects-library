import random

LetrasMaiuculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LetrasMinusculas = "abcdefghijklmnopqrstuvwxyz"
Numeros = "0123456789"
Simbolos = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

def GerarSenha(tamanho, LetrasMaiusculas, LetrasMinusculas, Numeros, Simbolos): 
    caracteres = LetrasMaiuculas + LetrasMinusculas + Numeros + Simbolos
    senha = ""
    for _ in range(tamanho): 
        senha += random.choice(caracteres)
    return senha

print(GerarSenha(12, LetrasMaiuculas, LetrasMinusculas, Numeros, Simbolos))