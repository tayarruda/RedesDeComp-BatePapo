# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: TALES JOABE LIMA DA COSTA
#
# SCRIPT:
#

# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = '10.2.251.200' # ip do servidor
serverPort = 65000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

username = input('Username: ')
clientSocket.send(username.encode('utf-8')) # envia o nickname para o servidor

modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente