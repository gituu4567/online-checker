# -*- coding: utf-8 -*-
import os
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import ipdb;ipdb.set_trace()

class whatsapp:

    def cleanlist(self, x):
        List = x.split(",")
        for i in reversed(range(len(List))):  
                # reversing index due to error on index traversal when elements are poped out results in change in overall as well as each element index after it is poped, sol: take element from end of list
            if List[i] == "":
                List.pop(i)
            else:
                List[i] = List[i].strip().lower()
        return List

    def start(self):
        try:
            global webdriver
            from selenium import webdriver
	    if os.name=="posix":
            	# Linux specific code here
            	webdriver = webdriver.Chrome('./driverlinux/chromedriver')
                #webdriver = webdriver.Firefox()
                #geckodriver must be in /usr/local/bin/ with chmod +x
                webdriver.implicitly_wait(2)
                #implicit wait --it causes missing parameter and url not opening in linux firefox
            else:
                # windows specific
            	webdriver = webdriver.Chrome('driver/chromedriver')  
                # f*** these difference bw file finding while both are in same folder
            	#webdriver = webdriver.Firefox('./driver')  # still it uses the geckodriver in root folder not the specified driver folder
                webdriver.implicitly_wait(0)
              
            # seconds # http://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp#implicit-waits
            webdriver.get("https://web.whatsapp.com/")
            #webdriver.maximize_window()
            return True
        except Exception as e:
            print e

    def loggedin(self):
        try:
            elem2 = webdriver.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input')
            return True
        except:return False    

    def search(self, t):
        try:
            t = str(t)
            elem2 = webdriver.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input')  
            # alternate search box 2
            elem2.clear()  
            # clr field
            elem2.send_keys(t)  
            # send contact name to search box
            elem2.send_keys(Keys.RETURN)
            # press Enter
            elem3 = webdriver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span')
            if elem3.text.lower().find(t.lower()) > -1:  
            # finding contact name is same as input target
                return True
            else:
                return False
        except Exception as e:
            print e
            return False

    def sendmsg(self, msg):
        msg = str(msg)
        msgbox = webdriver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  
        # message box
        msgbox.send_keys(msg)  
        # sending valid message
        try:
            msgbox.send_keys(Keys.RETURN)
            return True
        except:
            print "Blank msg error"
            return False

    def logout(self):
        try:
            settingbtn = webdriver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/button')
            settingbtn.click()
            logoutbtn = webdriver.find_element_by_xpath(
                '//*[@id="side"]/header/div[2]/div/span/div[2]/span/div/ul/li[6]/a')
            logoutbtn.click()
            return True
        except Exception as e:
            print e
            return False

    def verify(self,t):
        t =str(t)
        try:
            elem1 = webdriver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span')
            if elem1.text.lower().find(t.lower()) > -1:
                return True
            else:return False
        except: return False




    def lastseen(self, t):
        t = str(t)
        assert t != "", "Blank input found"
        if whatsapp().verify(str(t))==False:
            whatsapp().search(t)
        try:
            while True:

                try:
                    elem6 = webdriver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
                    status = elem6.text

                    if status == "click here for contact info":
                        continue

                    elem3 = webdriver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span')
                    if elem3.text.lower().replace(' ','').find(t.lower()) > -1:  
                    # finding contact name is same as input target
                        return elem3.text, status
                        break
                    else:
                        print t.lower(), "compared to",elem3.text.lower(),"failed" 
                        return t, "unknown contact"
                        break
                except Exception as e :
                    print e
                    return t, "hidden"
        except KeyboardInterrupt as e:
            print "\n keyboard interrupt raised"
            raise e
        except:
            return t, "error"

    def online(self, t):
        t = str(t)
        try:
            if whatsapp().lastseen(t)[1]=="online" or whatsapp().lastseen(t)[1]=="typing":
                return True
            else:
                return False
        except Exception as e:
            print e
            return False

    def spam(self, x, msg, loop):  
    # looper program in short
        if whatsapp().search(x):
            for i in range(loop):
                if whatsapp().sendmsg(msg) != True:
                    return False
        else:
            return False
        return True

    def getcookie(self):
        global data
        try:
            data = (webdriver.execute_script("""

var key = [] ;
var value = [] ;
var data = [] ;

for ( var i = 0, len = localStorage.length; i < len; ++i ) 
{
key[i] = localStorage.key(i) ;
value[i] = localStorage.getItem(localStorage.key(i)) ;

}
data[0] = key;
data[1] = value;
return data ;

"""))
            return True
        except Exception as e:
            print e

        for i in range(len(data[0])):
            print "Got local storage for", data[0][i].encode('utf-8'), "=====", data[1][i].encode('utf-8')

    def postcookie(self):
        try:
            for i in range(len(data[0])):
                webdriver.execute_script("""localStorage.setItem('%s','%s');""" % (data[0][i], data[1][i]))
                # print "injecting... local storage for ", data[0][i],"=====>", data[1][i]
            # webdriver.find_element_by_xpath("//body").send_keys(Keys.F5)
            webdriver.refresh()
            return True
        except Exception as e:
            print "injecting failed for", data[0][i], "=====>", data[1][0], "due to", e
            raise

    def dump(self):
        prince = data
        with open('cookies.pkl', 'wb') as f:
            pickle.dump(prince, f)
            # print data
        return True

    def load(self):
        global data
        with open('cookies.pkl', 'rb') as f:
            data = pickle.load(f)
        return True

    def waitingpeople(self):
        global waiting
        waiting = webdriver.find_elements_by_class_name("unread")
        return len(data)

    def autopilot(self):
        for i in range(whatsapp().waitingpeople()):
            if waiting:
                try:
                    waiting[i].click()
                    whatsapp().sendmsg("Master is busy , try Calling if its Urgent... next Available at 10:30 afterwards  ")
                except:
                    pass



if __name__ == '__main__':  
# differentiate between running as main or module
    whatsapp().start()
