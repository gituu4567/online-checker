# -*- coding: utf-8 -*-
# *****************************************************
# whatsapp scripting v1.0
# Author:
# Parwinder <psroadheaven@gmail.com>
# https://github.com/parwinders
# 3oth march 2017 
# *****************************************************
from thread import *
# import pdb;pdb.pm()
import os
import wa
import sys
import time
import datetime

if os.name == 'nt':
    import winsound

    flag = "win"
else:
    flag = 'linux'
    import pygame

    pygame.init()

import thread
import codecs


def playsound(filename):
    if flag == 'win':
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    else:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()


def replace_line(file_name, line_num, text):
    lines = codecs.open(file_name, 'r', 'utf-8').readlines()
    lines[line_num] = text
    out = codecs.open(file_name, 'w', 'utf-8')
    out.writelines(lines)
    out.close()


def gettargetcount():
    global book
    book = codecs.open('victim.txt', 'r', 'utf-8').readlines()
    for line in book:
        if not line.rstrip().strip():
            book.pop(line)
    targetcount = len(book)
    return targetcount


def start():
    global timespent
    global lastseentime
    global totalonline
    with codecs.open('database.txt', 'w', 'utf-8') as file:
        pass
    for i in range(targetcount):
        with codecs.open('database.txt', 'a', 'utf-8') as file:
            book[i] = book[i].rstrip()
            fakedata = ('%s:none:offline:none\n' % (book[i]))
            file.write(fakedata)

    timespent = [[0 for j in range(0)] for i in range(targetcount)]
    lastseentime = [[0 for j in range(0)] for i in range(targetcount)]
    totalonline = [0 for i in range(targetcount)]


print "ctrl + c to exit "
wa.whatsapp().start()
wa.whatsapp().load()
wa.whatsapp().postcookie()

# import ipdb;ipdb.set_trace()

while (wa.whatsapp().loggedin() == False):
    wa.whatsapp().loggedin()
    time.sleep(5)

targetcount = gettargetcount()
start()

while True:
    if targetcount != gettargetcount():
        targetcount = gettargetcount()
        start()

    while True:
    	wa.whatsapp().autopilot()
        starttime = time.time()
        try:

            targetnamelist = []
            targetstatuslist = []


            # with codecs.open('victim.txt', 'r','utf-8') as book:
            for x in range(targetcount):
                target = book[x].strip()
                try:
                    contact, status = wa.whatsapp().lastseen(target)
                except KeyboardInterrupt:
                    print "\nbye"
                    wa.webdriver.quit()
                    sys.exit(0)

                targetnamelist.append(contact)
                targetstatuslist.append(status)
                if status == "online" or status == 'typing':
                    # constant online notification coding here
                    thread.start_new_thread(playsound, ('bleep.wav',))

                    try:
                        for i in range(timetaken):
                            try:
                                totalonline[x] += timespent[x].append(1).count(1)
                            except:
                                pass
                            lastseentime[x].append(time.asctime())
                    except NameError:
                        for i in range(targetcount):
                            try:
                                totalonline[x] += timespent[x].append(1).count(1)
                            except:
                                pass
                            lastseentime[x].append(time.asctime())

                    spotted = timespent[x].count(1)
                    spotted = str(datetime.timedelta(seconds=spotted))  # seconds to standard elapsed time HH:mm:ss
                    # print "%s  => %s  ==> %s for %s seconds " %(target, contact, status, spotted)
                    # print totalonline[x]
                    print "%s=>	%s ==> %s for %s seconds " % (target, contact, status, spotted)
                else:
                    timespent[x] = []

        except Exception as e:
            print e

        for i in range(targetcount):

            try:
                data = ('%s    ==%s    ==%s    ==%s    ==%s\n' % (
                    targetnamelist[i], targetstatuslist[i], "offline", datetime.timedelta(seconds=timespent[i].count(1)),
                    totalonline[i]))
                data2 = ('%s:%s:%s:%s\n' % (targetnamelist[i], targetstatuslist[i], "offline", timespent[i].count(1)))
            except:
                raise

            with codecs.open('database.txt', 'r+', 'utf-8') as file:
                currentdata = file.readlines()

            if targetstatuslist[i].encode('utf-8') in ('online', 'typing'):
                if currentdata[i].find('offline') > -1:
                    # initial online notification
                    thread.start_new_thread(playsound, ('train1.wav',))
                    print "\n", targetnamelist[i], "is Online !!!"

                data = data.replace('online', time.asctime())
                data = data.replace('offline', 'online')


            elif targetstatuslist[i].encode('utf-8').lower().find('last') > -1:
                if (currentdata[i].find('online') > -1) or (currentdata[i].find('typing') > -1):
                    # initial offline notification
                    print"\n%s was online from %s till %s" % (targetnamelist[i], lastseentime[i][-1], time.asctime())


            else:
                if (currentdata[i].find('online') > -1) or (currentdata[i].find('typing') > -1):
                    # initial offline notification
                    thread.start_new_thread(playsound, ('train2.wav',))
                    print"\n%s was online from %s till %s" % (targetnamelist[i], lastseentime[i][-1], time.asctime())

            replace_line('database.txt', i, data)

        endtime = time.time()
        timetaken = int(endtime - starttime)
        print "\n", 'database is updated in', timetaken, "/secs", 'for', len(targetnamelist), "Users"

  	break
