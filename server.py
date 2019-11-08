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
class myThread(threading.Thread):
    def __init__(self, connectionSocket):
        threading.Thread.__init__(self)
        self.connectionSocket = connectionSocket
        # a funcao run() e executada por padrao por cada thread
    def run(self):
        # aviso de inicio da thread
        print ('Iniciando Thread %d [%s] com %d tarefas' % (self.id, self.name, self.counter))
        # chama a funcao a ser executada por cada thread
        #definir a funcao ...
        clientConecta(self.connectionSocket)
        
#Solicitar um nome (nickname) a cada cliente que se conectar;
    
def clienteConecta(connectionSocket):
    #servidor recebe dados do cliente
    nickname = connectionSocket.recv(1024)
    nickname = nickname.decode('utf-8')
    #adiciona cliente na lista
    connectionSocket.send(addr[0].encode('utf-8'))
    addList(clients,nickname, addr[0], addr[1])
    #cliente entra na sala
    clientOn(nickname)
    
#Permitir que todos os clientes conectados enviem e recebam mensagens;
def enviarMensagens(clientes, nickname, mensagem):
    cliente.send(str(mensagem).encode('utf-8'))
    
#lista de clientes
def addList(clients,nickname, ip, port):
    clientName = nickname.decode('utf-8')[2:len(nickname)-1]
    clientInfo = [clientName, ip, port]
    clients.append(clientInfo)
    print(clients)

#cliente entra na sala
def clientOn(nickname):
    userOn= nickname.decode('utf-8')[2:len(nickname)-1]
    print(colored(userOn, 'green'), "entrou na sala")

#estabelece conexao: cliente entrou na sala e add na lista

#definindo protocolo
def protocoloComunicacao(tam,nickname,comando, dados):
    return{
        "TamanhoMensagem": tam,
        "NicknameClient": nickname.encode('utf-8'),
        "Comando": comando.encode('utf-8'),
        "Dados": dados.encode('utf-8')
    }
#Permitir que os clientes possam iniciar comunicações privadas por meio do comando privado(*), onde * será o nome do cliente;
  
#Encerrar todos os clientes quando o servidor for encerrado utilizando o comando sair().


# definicao das variaveis
lista = []
serverName = '' # ip do servidor (em branco)
serverPort = 65000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
clients = []
while True:
    try:
  #connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
        mensagem = connectionSocket.recv(1024) # recebe dados do cliente
        mensagem = username.decode('utf-8')
        
        if comando.decode('utf-8') == 'lista()':
            print("Lista de usuários Conectados: \n")
            print(clients)
        
        else if comando.decode('utf-8') == 'sair()':
            print(nickname + 'saiu!')
            clients.pop(nickname)
            connectionSocket.close()
        else:
            mensagemEnviar = nickname + " escreveu: "+ msg.decode('utf-8')
            
while True:
    try:
        connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
        threadConexoesServidor = ThreadConexoes(connectionSocket) # Cria uma Thread para cada nova conexão.
        threadConexoesServidor.start()
    except:
         serverSocket.close()