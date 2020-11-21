import os.path
import pandas as pd
import varGlobais

def readCSV():
    if(os.path.isfile("contatos.csv")):
        aux = pd.read_csv("contatos.csv")
        varGlobais.updateVar(aux)


def salvar():
    df = varGlobais.df
    df.to_csv('contatos.csv', encoding='utf-8', index=False)
    print('\033[93m' + "Alterações salvas!!" + '\033[0m')


def returnDF():
    if(varGlobais.df.size == 0):
        readCSV()
    return varGlobais.df