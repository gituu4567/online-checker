import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

web = webdriver.Chrome('driver/chromedriver')  # f*** these difference bw file finding while both are in same folder
#web = webdriver.Firefox('./driver') #still it uses the geckodriver in root folder not the specified driver folder
web.implicitly_wait(5) # seconds # http://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp#implicit-waits
web.get("https://web.whatsapp.com/")
web.maximize_window()


    
class Whtsapp:


    def __init__(self):
        pass

    def search(self, t):
        try:
            elem2 = web.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input') # alternate search box 2
            elem2.clear() # TODO improve finding contact by pressing send key with target name
            elem2.send_keys(t)  # send contact name to search box
            elem2.send_keys(Keys.RETURN)
            elem3 = web.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/h2/span')
            if elem3.text.lower().find(t.lower()) > -1:             # finding contact name is same as input target
                return True
            else: return False
        except Exception as e:
            print e
            return False
            
    def sendmsg(self,msg):
                elem3 = web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  # message box
                elem3.send_keys(msg)  # sending valid message
                try:
                    elem4 = web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/button')  # send key only appears when message is valid
                    elem4.click()  # press send
                    return True
                except:
                     print "Blank msg error"
                     return False
        
    def cleanlist(self,x):
        List = x.split(",")
        for i in reversed(range(len(List))): # reversing index due to error on index traversal when elements are poped out results in change in overall as well as each element index after it is poped, sol: take element from end of list
            if List[i] == "":
                List.pop(i)
            else:
                List[i] = List[i].strip().lower()
            
        return List 
    
    def loggedin(self):
        try:
            loginelem = web.find_element_by_xpath('//*[@id="window"]/div[1]/div[2]/div[2]')
            if loginelem.text == "Use WhatsApp on your phone to scan the code":
                return False
            else: return True
        
        except:
            return True


    def checkstatus(self, t):
        #import ipdb;ipdb.set_trace()
        assert t != "", "Blank input found"                     # "contact name is blank"
        try:
            while True:
                Whtsapp().search(t)
                try:
                    elem6 = web.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
                    status = elem6.text
                    
                    if status == "click here for contact info":
                        continue
                    
                    elem3 = web.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/h2/span')
                    if elem3.text.lower().find(t.lower()) > -1:             # finding contact name is same as input target
                        return elem3.text, status
                        break
                    else:
                        return t, "unknown contact"
                        break
                except: return t, "hidden"
        except: return "error","error"
        
    def online(self, t):
        try:
            if (Whtsapp().checkstatus(t))[1] == "online":
                return True
            else: return False
        except Exception as e:
            print e
            return False


    def spam(self, x, msg, loop):                                       #TODO ALOT copy correction from checkstatus :)
        if Whtsapp().search(x):
            for i in range(loop):
                if Whtsapp().sendmsg(msg) !=True:
                    return False
        else: return False       
        return True        
                    
                            
