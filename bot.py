from socket import *

server = socket(AF_INET,SOCK_STREAM)

server.connect(("web.rubika.ir",443))

print("Connected ! ! !")