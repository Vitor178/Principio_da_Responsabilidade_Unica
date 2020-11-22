# Princípio da Responsabilidade única

Ao se iniciar os estudos em computação é bem comum que os primeiros códigos que produzimos não obedeçam muito as boas práticas de programação, visto que isso é algo que o programador adquire com o passar do tempo e com mais experiência. Muito provavelmente todas as pessoas que já se aventuraram em escrever algum código já produziram ou se depararam com aqueles arquivos “faz tudo”, em que em um único arquivo de código é feito a captação dos dados, impressão da tela, processamento de dados ou outras n coisas distintas.

É justamente sobre isso que o princípio da responsabilidade única trata, ele é o primeiro princípio dos 5 princípios [SOLID](https://en.wikipedia.org/wiki/SOLID) e, de maneira direta, diz o seguinte:

    “Uma classe pode ter apenas uma razão para ser mudada”

Na verdade isso não é restrito apenas a classes, o mesmo vale para módulos, métodos, funções ou até arquivos. A razão para mudança que o princípio menciona se refere a responsabilidade que uma unidade de código possui. Sendo assim, outra maneira de se explicar o princípio da responsabilidade única é, como o próprio nome sugere:

    “Uma unidade de código pode ter apenas uma responsabilidade”

Para exemplificar isso vamos dar uma olhada no arquivo de código => [link](https://github.com/Vitor178/Principio_da_Responsabilidade_Unica/blob/master/codigo_antes/emailSender.py)

As explicações sobre o que esse código faz estão aqui => [link](https://github.com/Vitor178/Principio_da_Responsabilidade_Unica/blob/master/EmailSender.md)

```
#estrutura do código
# algumas funções auxiliares não foram colocadas aqui para facilitar a visualização

class Contato:
  ...
def addContato(obj):
  ...
def removerContato(email):
  ...
def printContatos():
  ...
def enviarEmail(dados):
  ...
def readCSV():
  ...
def salvar():
  ...
def main():
  ...
```

A princípio pode parecer interessante manter todo o código em um único arquivo, visto que isso poderia dar uma idéia de um código mais organizado por se encontrar todo em um único local. Porém, não podemos esquecer que o exemplo de código utilizado é relativamente pequeno e que os sistemas computacionais costumam a chegar a tamanhos muito maiores.

Pense em um sistema com dezenas ou até centenas de milhares de linhas de código, todas agrupadas em um único arquivo. Imagine realizar manutenções, adicionar novas funcionalidades ou encontrar bugs em meio a essa imensidão de código agrupado. Certamente seriam tarefas quase impossíveis se todas essas linhas de código estivessem em um mesmo arquivo. Por isso, uma divisão de código é importante, contudo, dividir o código sem algum critério não é uma boa saída, pois muito provavelmente ainda estaríamos agrupando pedaços de código com responsabilidades diferentes em uma mesma unidade. É aí que entra a importância de saber identificar as responsabilidades do código.

Retornando ao exemplo de código dado, podemos perceber que nele há funções responsáveis por enviar email, realizar leitura e escrita em arquivo, gerenciar objetos da classe Contato e a função main, que é responsável pela interação com o usuário. Ou seja, são quatro responsabilidades/razões para mudança em uma mesma unidade de código.
Ao realizar a divisão do código de exemplo em relação às responsabilidades encontradas, a nova distribuição passou a ser assim  => [link](https://github.com/Vitor178/Principio_da_Responsabilidade_Unica/tree/master/codigo_depois)

**Arquivos de código após a divisão**
* armazenamento.py
* contato.py
* main.py
* emailSender.py

###### obs:pequenas mudanças em algumas funções e a criação de um arquivo separado para a variável global foram necessários para manter o mesmo funcionamento do código

Podemos ver que agora temos arquivos mais coesos, ou seja, cada arquivo tem sua própria responsabilidade. O que faz com que mudanças tenham menos chances de gerar erros inesperados em outras partes do código.

Não há uma maneira 100% sistemática de encontrar responsabilidades, por isso pessoas diferentes podem encontrar responsabilidades diferentes, sendo elas mais abrangentes ou mais específicas. Nesse caso não há um certo ou errado, é responsabilidade do programador decidir quais responsabilidades são mais relevantes. Antes de dividir uma responsabilidade em outras reflita se tal divisão, em um contexto geral, irá trazer mais benefícios ou malefícios. Responsabilidades muito específicas podem fazer com que o código fique mais complexo, o que também é algo que não queremos.

