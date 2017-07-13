# developer: psroadheaven@gmail.com
# whatsapp looper spam sender v-1.0
# 3oth march 2017

from wa import Whtsapp
import os


#target = ["mnisha","saran"]
target = raw_input('enter contacts \",\" seperated  :')
target = Whtsapp().cleanlist(target)       
print target

while (Whtsapp().loggedin()==False):
        Whtsapp().loggedin()
        
while True:
        os.system("clear")
        for i in range(len(target)):
                contact, status = Whtsapp().checkstatus(target[i],0)
                print " %s      ==> %s  ==> %s " %(target[i], contact, status)
