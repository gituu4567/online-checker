
import os
import wa
import sys
import time as time2
import datetime
from selenium.webdriver.common.keys import Keys

from datetime import datetime, time

def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

leaving_date = datetime.strptime('2017-11-23 00:00:00', '%Y-%m-%d %H:%M:%S')


print "ctrl + c to exit "
wa.whatsapp().start()
wa.whatsapp().load()
wa.whatsapp().postcookie()

# import ipdb;ipdb.set_trace()

while (wa.whatsapp().loggedin() == False):
    wa.whatsapp().loggedin()
    time2.sleep(5)

profilebtn = wa.webdriver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/span/img')
profilebtn.click()

while True:
	time2.sleep(5)

	edit = wa.webdriver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/div/div/div[4]/div[2]/div[2]/div[2]/span[1]/div/span')
	edit.click()

	input = wa.webdriver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/div/div/div[4]/div[2]/div[2]/div[1]/div[2]')
	input.clear()
	now = datetime.now()

	#countdown = " %d " % dateDiffInSeconds(now, leaving_date)
	countdown = "%d days, %d hours, %d minutes, %d seconds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, leaving_date))


	input.send_keys(countdown)
	input.send_keys(Keys.RETURN)
