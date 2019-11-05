# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: TALES JOABE LIMA DA COSTA
#
# SCRIPT:
#

# importacao das bibliotecas
from socket import * # sockets
import threading #thread


#definindo funcoes

#Aceitar conexões dos clientes (sem limites);
#Criar uma ou mais threads para cada cliente conectado;
def ThreadConexao(threading.Thread):
    def __init__(self, connectionSocket):
        threading.Thread.__init__(self)
        self.connectionSocket = connectionSocket
        # a funcao run() e executada por padrao por cada thread
    def run(self):
        # aviso de inicio da thread
        print ('Iniciando Thread %d [%s] com %d tarefas' % (self.id, self.name, self.counter))
        # chama a funcao a ser executada por cada thread
        #definir a funcao ...
        
        
#Solicitar um nome (nickname) a cada cliente que se conectar;
def solicitaNickname(connectionSocket):
    nickname = connectionSocket.recv(65000)#receber do cliente
    nickname.encode('utf-8')
    cliente = {
        'nickname': nickname
        'socket': connectionSocket
    }
    connectionSocket.send(addr[0].encode('utf-8'))
    
#Permitir que todos os clientes conectados enviem e recebam mensagens;
def enviarMensagens(clientes, nickname, mensagem):
    cliente.send(str(mensagem).encode('utf-8'))

#Permitir que os clientes possam iniciar comunicações privadas por meio do comando privado(*), onde * será o nome do cliente;
#Exibir a lista de clientes conectados
def listaUsuarios(clientes, connectionSocket, nickname, addr):
    sizelistaclientes = len(clientes)
    for clientesConectados in clientes:
        #concatenar todos os nicknames de clientes conectados
        
#Encerrar todos os clientes quando o servidor for encerrado utilizando o comando sair().


# definicao das variaveis
lista = []
serverName = '' # ip do servidor (em branco)
serverPort = 65000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

while True:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  username = connectionSocket.recv(1024) # recebe dados do cliente
  username = username.decode('utf-8')

  lista.append(username)

  print ('Username: %, IP: %s, Porta: %s' % (username, connectionSocket, addr))
  connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto transformado
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor