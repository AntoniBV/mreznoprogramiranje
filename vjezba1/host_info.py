import socket
def host_info():
	host_name = socket.gethostbyaddr("8.8.8.8")
	#print "Host name: %s" % host_name
	print host_name
if __name__ == '__main__':
	host_info()