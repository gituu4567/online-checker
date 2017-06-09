# developer: psroadheaven@gmail.com
# whatsapp looper spam sender v-1.0
# 3oth march 2017

from wa import Whtsapp

target = ["rocky", "Gp", "mnisha"]


while True:
    while Whtsapp().loggedin():

        for i in range(len(target)):
            
            status = Whtsapp().checkstatus(target[i],2)
            print target[i]
            print status
    else:
        pass