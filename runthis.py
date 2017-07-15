# *****************************************************
# whatsapp scripting v1.0
# Author:
# Parwinder <psroadheaven@gmail.com>
# https://github.com/parwinders
# 3oth march 2017 
# *****************************************************
import numpy
import os;os.system("cls")
import wa
import sys
import ipdb;ipdb.set_trace()


wa.whatsapp().start()
wa.whatsapp().load()
wa.whatsapp().postcookie()

try:
    target = "mnisha,saran"
    #target = raw_input('enter contacts \",\" seperated  :')
    target = wa.whatsapp().cleanlist(target)       
    print target

    while (wa.whatsapp().loggedin()==False):
            wa.whatsapp().loggedin()        
    while True:
        try:
            
            data0 = []
            data1 = []
            for i in range(len(target)):
                contact, status = wa.whatsapp().lastseen(target[i])
                print "\n%s      ==> %s  ==> %s " %(target[i], contact, status)
                data0.append(contact)
                data1.append(status)
            
        except Exception as e:
            print e
                    
        with open('database.txt', 'wb') as f:
            for i in range(len(target)):
                f.write('%s:%s\n' %(data0[i], data1[i] ))
                
        
        
        
        
except KeyboardInterrupt:
    print "\nbye"
    wa.webdriver.quit()
    sys.exit(0)
