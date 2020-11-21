import yagmail
import csv
import pandas as pd
import os.path
from datetime import datetime, date
from Seu_Email_Aqui import EMAIL

df = pd.DataFrame({'nome': pd.Series([], dtype='str'), 'email': pd.Series([], dtype='str'), 'data': pd.Series([], dtype='str')})


class Contato:
    def __init__(self, nome, email, data):
        self.nome = nome
        self.email = email
        self.data = data

    def __eq__(self, other):
        return (self.email == other.email)


def returnDF():
    global df
    if(df.size == 0):
        readCSV()
    return df


def printContatos():
    df = returnDF()
    print(df)
    

def readCSV():
    if(os.path.isfile("contatos.csv")):
        aux = pd.read_csv("contatos.csv")
        global df
        df = df.append(aux, ignore_index=True)
        

def salvar():
    global df
    df.to_csv('contatos.csv', encoding='utf-8', index=False)
    print('\033[93m' + "Alterações salvas!!" + '\033[0m')


def addContato(obj):
    global df
    df = returnDF()
    if(obj.email in df['email']):
        print('\033[93m' + "Email ja cadastrado!!" + '\033[0m')
    else:
        df2 = pd.DataFrame({'nome': [obj.nome], 'email': [obj.email], 'data': [obj.data]})
        df = df.append(df2, ignore_index=True)
        print('\033[93m' + "Contato adicionado!")
        print("*Não se esqueça de salvar(opção 3) antes de sair*" + '\033[0m')
    

def removerContato(email):
    global df
    df = returnDF()
    if(email in df['email'].values):
        df = df[df['email'] != email]
        print('\033[93m' + "Contato Removido!")
        print("*Não se esqueça de salvar(opção 3) antes de sair*" + '\033[0m')
    else:
        print('\033[93m' + "Email não cadastrado!!" + '\033[0m')


def verificarData():
    hoje = date.today().strftime("%d/%m")
    global df
    df = returnDF()
    aux = df[df['data'].str.contains(hoje)]
    if(aux.size > 0):
        enviarEmail(aux)
    else:
        print('\033[93m' + "Não há ninguém fazendo aniversário hoje :(" + '\033[0m')


def enviarEmail(dados):
    print('\033[93m' + "Enviando parabéns para:")
    for i in range(len(dados)):
        print(dados['email'].values[i])
        receiver = dados['email'].values[i]
        body = "Parabéns!!!"
        filename = "parabens.jpg"

        yag = yagmail.SMTP(EMAIL)
        yag.send(
            to=receiver,
            subject="Parabéns!!",
            contents=body, 
            attachments=filename,
        )

    print("fim" + '\033[0m')
 

def receberEntrada():
    print("nome: ")
    nome = input()
    print("email: ")
    email = input()
    print("data(xx/xx/xxxx): ")
    data = input()
    _ = datetime.strptime(data, '%d/%m/%Y')
    obj = Contato(nome, email, data)
    return obj


def receberEmail():
    print("email do contato que deseja excluir: ")
    email = input()
    return email


def main():
    
    helperText = '\033[95m'+"""
    Bem vindo ao EmailSender!!
    Nunca mais se esqueça de mandar parabéns para seus amigos!
    Selecione uma das opções abaixo:
        1 - Cadastrar novo amigo
        2 - Remover amigo cadastrado
        3 - Salvar mudanças
        4 - Mostrar todos os amigos salvos
        5 - Iniciar verificador de aniversários
        0 - sair
    """+'\033[0m'

    print(helperText)
    while(True):
        num = int(input())
        if(num == 1):
            addContato(receberEntrada())
        elif(num == 2):
            removerContato(receberEmail())
        elif(num == 3):
            salvar()
        elif(num == 4):
            printContatos()
        elif(num == 5):
            print("Iniciando...")
            verificarData()
        elif(num == 0):
            print("saindo...")
            return
        else: print(helperText)

if __name__ == "__main__":
    main()
