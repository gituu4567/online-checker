import wa
import codecs
import time
import os
import socket
import subprocess
             

# processing input
def incoming():
	global inputlist
	global outgoinglist
	while True:
		if inputlist:
			input = inputlist.pop(0)
			input = str(input)
			data = input.split(':')
			clientid = data[0]
			target   = data[1]
			target, status = wa.whatsapp().lastseen(target)
			if status == "online":
				outgoinglist.append(input)
		else:
			print "No pending incoming requests"
			time.sleep(10)

# processing output
def outgoing():
	while True:
		if outgoinglist:
			output = outgoinglist.pop(0)
			print output
			print "outgoing success !!!"
			# notification coding goes here
		else:
			print "No pending outgoing requests"
			time.sleep(10)

def server():
	host = ''        # Symbolic name meaning all available interfaces
	port = 12345     # Arbitrary non-privileged port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(1)
	conn, addr = s.accept()
	print"hi"
	print('Connected by', addr)
	while True:
	    data = conn.recv(1024)
	    if not data: break
	    conn.sendall(data)
	conn.close()				










def main():
	outgoinglist = []
	inputlist = []
	server()
	wa.whatsapp().start()
	wa.whatsapp().load()
	wa.whatsapp().postcookie()
	
	while (wa.whatsapp().loggedin()==False):
		wa.whatsapp().loggedin()
		time.sleep(5)

	incoming()
	outgoing()


main()