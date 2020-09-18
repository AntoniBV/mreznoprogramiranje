import socket
import datetime
from local_machine_info import print_machine_info

datum = datetime.datetime.now()
print(datum)
print_machine_info()

host = socket.gethostname()
port = 12345

client_socket = socket.socket() #TCP socket
client_socket.connect((host,port))
poruka = raw_input("Poruka serveru: ")
client_socket.sendall(poruka)

data = client_socket.recv(1024) 	

print data				
client_socket.close()