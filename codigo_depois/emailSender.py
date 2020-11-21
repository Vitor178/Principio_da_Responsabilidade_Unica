import yagmail
from Seu_Email_Aqui import EMAIL

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
 