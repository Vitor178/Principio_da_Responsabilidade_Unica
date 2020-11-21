import pandas as pd
from armazenamento import returnDF
from varGlobais import updateVar

class Contato:
    def __init__(self, nome, email, data):
        self.nome = nome
        self.email = email
        self.data = data

    def __eq__(self, other):
        return (self.email == other.email)


def addContato(obj):
    df = returnDF()
    if(obj.email in df['email']):
        print('\033[93m' + "Email ja cadastrado!!" + '\033[0m')
    else:
        df2 = pd.DataFrame({'nome': [obj.nome], 'email': [obj.email], 'data': [obj.data]})
        updateVar(df.append(df2, ignore_index=True))
        print('\033[93m' + "Contato adicionado!")
        print("*Não se esqueça de salvar(opção 3) antes de sair*" + '\033[0m')


def removerContato(email):
    df = returnDF()
    if(email in df['email'].values):
        updateVar(df[df['email'] != email])
        print('\033[93m' + "Contato Removido!")
        print("*Não se esqueça de salvar(opção 3) antes de sair*" + '\033[0m')
    else:
        print('\033[93m' + "Email não cadastrado!!" + '\033[0m')


def printContatos():
    df = returnDF()
    print(df)