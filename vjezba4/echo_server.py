import socket
import datetime
from local_machine_info import print_machine_info

datum = datetime.datetime.now()
print(datum)
print_machine_info()

host = socket.gethostname()
port = 12345

echo_server = socket.socket() #TCP socket
echo_server.bind((host, port))
echo_server.listen(5)

print "Cekam klijenta..."
conn, addr = echo_server.accept() 
print "Spojen: ", addr

while True:
	data = conn.recv(1024)	
	if not data: break	
	if data == 'aspira':
		print 'Tekst nije dozvoljen'
	else:
		print data
		conn.sendall(data)		

conn.close()