#!c:\python27\python
import wa
import sys

print "\n\n\npls login then dump cookie"

wa.whatsapp().start()

print "\nscan QR code"
while True:
	raw_input("\nReady to dump cookie? PRESS Enter")
	if wa.whatsapp().getcookie():
		print"got cookie "
		if wa.whatsapp().dump():
			print "dump success"
			break
		else: print " dump failed"	
	else:
		print"error getting cookie"
		
wa.webdriver.quit()