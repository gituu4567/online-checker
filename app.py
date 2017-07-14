
# *****************************************************
# whatsapp scripting v1.0
# Author:
# Parwinder <psroadheaven@gmail.com>
# https://github.com/parwinders
# 3oth march 2017 
# *****************************************************

import wa
import os
import sys

wa.whatsapp().start()

try:
    target = "mnisha,saran"
    #target = raw_input('enter contacts \",\" seperated  :')
    target = wa.whatsapp().cleanlist(target)       
    print target

    while (wa.whatsapp().loggedin()==False):
            wa.whatsapp().loggedin()
            
    while True:
            for i in range(len(target)):
                    contact, status = wa.whatsapp().lastseen(target[i])
                    print " %s      ==> %s  ==> %s " %(target[i], contact, status)

except:
    wa.whatsapp().logout()
    wa.webdriver.quit()
    print "bye1"