from wa import whatsapp
import sys

whatsapp().start()

print "\nscan QR code"
while True:
	raw_input("\n\n\nReady to dump cookie? PRESS Enter")
	if whatsapp().getcookie():
		print"got cookie "
		if whatsapp().dump():
			print "dump success"
			break
		else: print " dump failed"	
	else:
		print"error getting cookie"
		
wa.webdriver.quit()
sys.exit(0)