from contato import Contato, addContato, removerContato, printContatos
from armazenamento import salvar, returnDF
from datetime import datetime, date
from emailSender import enviarEmail


def verificarData():
    hoje = date.today().strftime("%d/%m")
    df = returnDF()
    aux = df[df['data'].str.contains(hoje)]
    if(aux.size > 0):
        enviarEmail(aux)
    else:
        print('\033[93m' + "Não há ninguém fazendo aniversário hoje :(" + '\033[0m')


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