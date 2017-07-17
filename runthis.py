# -*- coding: utf-8 -*-
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
import ipdb;ipdb.set_trace()
import time
import datetime
import winsound
import thread
import codecs

def playsound(filename):
    winsound.PlaySound(filename, winsound.SND_FILENAME)

def replace_line(file_name, line_num, text):
    lines = codecs.open(file_name, 'r','utf-8').readlines()
    lines[line_num] = text
    out = codecs.open(file_name, 'w','utf-8')
    out.writelines(lines)
    out.close()


wa.whatsapp().start()
wa.whatsapp().load()
wa.whatsapp().postcookie()


with codecs.open('database.txt', 'w','utf-8') as f:  # initializing database to empty 
    pass

try:

    while (wa.whatsapp().loggedin()==False):
            wa.whatsapp().loggedin()

    targetcount = 0        
    book = codecs.open('victim.txt', 'r','utf-8').readlines()
    for name in book:
        
        with codecs.open('database.txt','a','utf-8') as file:
            name = name.rstrip()
            fakedata = ('%s\n:none:offline:none\n' %(name))
            file.write(fakedata)
        targetcount+=1    
                    
    timespent    =[[0 for j in range(0)] for i in range(targetcount)]
    lastseentime =[[0 for j in range(0)] for i in range(targetcount)]
    totalonline  =[ 0 for i in range (targetcount)]
    
    while True:
        starttime = time.time()
        os.system('cls')
        try:
            
            targetnamelist = []
            targetstatuslist = []
            
            
            #with codecs.open('victim.txt', 'r','utf-8') as book:  
            targetcount = 0
            for y in book:
                target = y.strip()
                contact, status = wa.whatsapp().lastseen(target)
                targetnamelist.append(contact)
                targetstatuslist.append(status)    
                if status=="online" or status=='typing':
                    #constant online notification coding here
                    thread.start_new_thread( playsound , ('bleep.wav',) )    
                                 
                    try:
                        for i in range(timetaken):
                            try:totalonline[targetcount] += timespent[targetcount].append(1).count(1)
                            except :pass
                            lastseentime[targetcount].append(time.asctime())
                    except NameError:
                        for i in range(targetcount):
                            try:totalonline[targetcount] += timespent[targetcount].append(1).count(1)
                            except :pass
                            lastseentime[targetcount].append(time.asctime())  
                else:
                    timespent[targetcount] = []            

                        
                spotted = timespent[targetcount].count(1)
                spotted = str(datetime.timedelta(seconds=spotted)) #seconds to standard elapsed time HH:mm:ss
                print "%s  => %s  ==> %s for %s seconds " %(target, contact, status, spotted)
                print totalonline[targetcount]
                targetcount +=1

        except Exception as e:
            print e
            
        for i in range(len(targetnamelist)):
        
            try:
                data = ('%s    ==%s    ==%s    ==%s    ==%s\n' % ( targetnamelist[i], targetstatuslist[i], "offline" , datetime.timedelta(seconds=timespent[i].count(1)),totalonline[i]))
                data2 = ('%s:%s:%s:%s\n' % ( targetnamelist[i], targetstatuslist[i], "offline" , timespent[i].count(1)))
            except:
                print"error"

            with codecs.open('database.txt','r+','utf-8') as file:
                currentdata = file.readlines()

            if (targetstatuslist[i].encode('utf-8')=='online') or (targetstatuslist[i].encode('utf-8')=='typing'):
                if currentdata[i].find('offline') > -1:

                    #initial online notification
                    thread.start_new_thread( playsound , ('train2.wav',) )

                data = data.replace('online',time.asctime())
                data = data.replace('offline','online')
                

            elif targetstatuslist[i].encode('utf-8').lower().find('last') > -1:
                if (currentdata[i].find('online') > -1) or (currentdata[i].find('typing') > -1):

                    #initial offline notification
                    print"%s was online from %s till %s" % (targetnamelist[i],lastseentime[i][-1],time.asctime())
                

            else:
                if (currentdata[i].find('online') > -1) or (currentdata[i].find('typing') > -1):
                    #initial offline notification

                    print"%s was online from %s till %s" % (targetnamelist[i],lastseentime[i][-1],time.asctime())
            
            replace_line('database.txt',i,data)            


        endtime = time.time()
        timetaken = int(endtime-starttime)
        print "\n",'database is updated in',timetaken,"/secs",'for',len(targetnamelist),"Users"

except KeyboardInterrupt:
    print "\nbye"
    wa.webdriver.quit()
    sys.exit(0)
