# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: TALES JOABE LIMA DA COSTA
#
# SCRIPT:
#

# importacao das bibliotecas
from socket import *
import threading #threading

#definicao das funcoes
#Conectar-se ao servidor;
#Escolher um nome (nickname) para se identificar no bate-papo;
nickname = input('Digite um nickname: ')
while nickname == "":
    nickname = input('Digite seu nickname para iniciar a conversa: ')

clientSocket.send(nickname.encode('utf-8')) # envia o nickname para o servidor
#Enviar e receber mensagens em grupo;


def getComando(comando):
    
#Enviar mensagens privadas por meio do comando privado(*), onde * será o nome do cliente a receber;
#Requisitar a lista de clientes por meio do comando lista();
#Encerrar a sua aplicação ao digitar sair().
if comando.decode('utf-8') == "sair()":
    clientSocket.close()
    break

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 65000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor


modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente