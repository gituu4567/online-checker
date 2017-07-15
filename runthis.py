# *****************************************************
# whatsapp scripting v1.0
# Author:
# Parwinder <psroadheaven@gmail.com>
# https://github.com/parwinders
# 3oth march 2017 
# *****************************************************
import os;os.system("cls")
import wa
import sys
#import ipdb;ipdb.set_trace()
import time


wa.whatsapp().start()
wa.whatsapp().load()
wa.whatsapp().postcookie()

try:
    
    #target = "mnisha,saran"
    #target = raw_input('enter contacts \",\" seperated  :')
    #target = wa.whatsapp().cleanlist(target)       
    #print target

    while (wa.whatsapp().loggedin()==False):
            wa.whatsapp().loggedin()
    loop1 = 0        
    with open('victim.txt', 'r') as f:
        for z in f:
            loop1+=1
                    
    timespent =[[0 for j in range(0)] for i in range(loop1)]        
    
    while True:
        tick0 = time.clock()
        try:
            
            data0 = []
            data1 = []
            loop2 = 0
                
            with open('victim.txt', 'r') as book:    
                for y in book:
                    target = y.rstrip()
                    contact, status = wa.whatsapp().lastseen(target)
                    data0.append(contact)
                    data1.append(status)
                    
                    if status == "online":
                        try:
                            for i in range(delay):
                                timespent[loop2].append(1)
                            
                        except NameError:
                            for i in range(loop1):
                                timespent[loop2].append(1)
                    else:
                        try:
                            for i in range(delay):
                                timespent[loop2].append(0)
                            print "\ncorrecting time" 
                            
                        except NameError:
                            for i in range(loop1):
                                timespent[loop2].append(0)
                        
                    print "\n%s      ==> %s  ==> %s " %(target, contact, status)
                    spotted = timespent[loop2].count(1)
                    print spotted
                    loop2+=1

            
        except Exception as e:
            print e
            

        
        with open('database.txt', 'wb') as f:
            for i in range(len(data0)):
                f.write('%s:%s:%s\n' %(data0[i], data1[i],timespent[i].count(1) ))
        
        tick1 = time.clock()
        delay = int(tick1-tick0)
        print "\n",'database is updated in',delay,"/secs",'for',len(data0),"Users"
                
        
        
        
        
except KeyboardInterrupt:
    print "\nbye"
    wa.webdriver.quit()
    sys.exit(0)
