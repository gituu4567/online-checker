import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys


web = webdriver.Chrome('driver/chromedriver')  # f*** these difference bw file finding while both are in same folder
#web = webdriver.Firefox('./driver') #still it uses the geckodriver in root folder not the specified driver folder
web.get("https://web.whatsapp.com/")
web.maximize_window()


    
class Whtsapp:
    def __init__(self):
        pass
    
    def loggedin(self):
        try:
            elem1 = web.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[1]/button')  # contact button
            elem1.click()  # click contacts button
            time.sleep(2)
            web.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/header/div/div/span').click() # back-button
            return True
        except:
            return False

    def checkstatus(self, t, sleeptime):
        #import ipdb;ipdb.set_trace()
        assert (t.strip != True)# "contact name is blank"
        try:
            web.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[1]/button').click()  # contact button
            elem2 = web.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div[1]/div/label/input')  # find search box
            elem2.clear() # TODO improve finding contact by pressing send key with target name
            elem2.send_keys(t)  # send contact name to search box
            elem2.send_keys(Keys.RETURN)
            #old = """web.find_element_by_xpath('//span[contains(text(),"targetname")]').click()"""  # advNCED matching
            #new = old.replace("targetname", t)
            #exec new
            time.sleep(sleeptime)
            elem6 = web.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
            status = elem6.text
            return status

                
        except Exception as e:
            return "Hidden**"
            try: web.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/header/div/div/span').click()
            except: pass

    def online(self, t):
        try:
            if Whtsapp.checkstatus(web, t) == "online":
                return True
            else: return False
        except Exception as e:
            print e

    def spam(self, t, msg, loop):
        for i in range(loop):
            try:
                elem1 = web.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[1]/button')  # contact button
                elem1.click()  # click contacts button
                time.sleep(2)

                elem2 = web.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/div[1]/div/label/input')  # find search box
                elem2.send_keys(t)  # send contact name to search box
                time.sleep(2)

                old = """web.find_element_by_xpath('//span[contains(text(),"targetname")]').click()"""  # advNCED matching
                new = old.replace("targetname", t)

                exec new
                time.sleep(2)

                elem3 = web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  # message box
                elem3.send_keys(msg)  # sending valid message
                elem4 = web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/button')  # send key only appears when message is valid
                elem4.click()  # press send
            except Exception as e:
                print e
                return False

        return True
