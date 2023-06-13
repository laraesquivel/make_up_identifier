import csv
import colorsys
import numpy as np

def ler_csv(nome_arquivo):
    base = []
    with open(nome_arquivo, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=',')
        for linha in leitor_csv:
           base.append([linha[0],linha[2]])
    return base

def on_replace(base):
    lista_rgba = [cor[1].replace("rgba(", "").replace(")", "").split(",") for cor in base]

    for i in range(len(base)):
        base[i][1] = lista_rgba[i]
    return base


def convert_hsv(base):
    for i in range(len(base)):   
        r, g, b, a = base[i][1]
        r = float(r)
        g = float(g)
        b = float(b)
        a = float(a)
        r /= 255.0
        g /= 255.0
        b /= 255.0
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        h *= 360.0
        s *= 100.0
        v *= 100.0
        base[i][1] = [h,s,v]

    return base

def distancia_eucliana(vetor):
    nome_arquivo = 'Maquiagem_sheets.csv'
    base = ler_csv(nome_arquivo)
    baseReplace = on_replace(base)
    baseHSV = convert_hsv(baseReplace)
    vetor = [float(num) for num in vetor]

    resultado = np.array(vetor)
    lista_hsv = [base[1] for base in baseHSV]
    lista_hsv = np.array(lista_hsv)
    distancias = np.linalg.norm(resultado - lista_hsv, axis=1)
    indice_cor_aproximada = np.argmin(distancias)
    cor_aproximada = baseHSV[indice_cor_aproximada]
    return cor_aproximada




