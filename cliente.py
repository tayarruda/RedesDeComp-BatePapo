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
clientison = true;

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 65000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

#definicao das funcoes


#conectar-se ao servidor
#Escolher um nome (nickname) para se identificar no bate-papo;

nickname = print('Digite um nickname: ')
while nickname == "":
    nickname = ptint('Digite seu nickname para iniciar a conversa: ')
clientSocket.send(nickname.encode('utf-8')) # envia o nickname para o servidor
#Enviar e receber mensagens em grupo;
thread = receber(clientSocket)
thread.start()

#Enviar e receber mensagens em grupo;
class receber(threading.Thread):
    # redefine a funcao __init__ para aceitar a passagem parametros de entrada
    def __init__(self,clientSocket):
        threading.Thread.__init__(self)
        self.client_Socket = clientSocket
    # a funcao run() e executada por padrao por cada thread
    def run(self):
        
        while clientison:
            msg = self.client_Socket.recv(1024)
            msg = msg.decode('utf-8')
            #pegar os dados da funcao do protocolo, nao sei fz...
            print(dados)

modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente

def protocoloCliente(tam, nickname, comando, dados):
        return{
        "TamanhoMensagem": tam,
        "NicknameClient": nickname.encode('utf-8'),
        "Comando": comando.encode('utf-8'),
        "Dados": dados.encode('utf-8')
        }

try:
#se ele tiver online pode enviar comandos
    while clientison:
        try:
        #extrair o comando da funcao protocolo, ver como faz..
            if comando.decode('utf-8') == 'sair()':
                clientison = false
                clientSocket.close()
                break
        except:
            clientSocket.close
