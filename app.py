# developer: psroadheaven@gmail.com
# whatsapp looper spam sender v-1.0
# 3oth march 2017

from wa import Whtsapp
import os


target = ["Gp", "mnisha","rocky","saran jio"]


while (Whtsapp().loggedin()==False):
        Whtsapp().loggedin()
        
while True:
        os.system("clear")
        for i in range(len(target)):
                status = Whtsapp().checkstatus(target[i],0)
                print " %s ==========> %s " %(target[i],status)
