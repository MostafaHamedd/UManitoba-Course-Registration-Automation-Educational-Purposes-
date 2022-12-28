import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://aurora.umanitoba.ca/banprod/twbkwbis.P_WWWLogin")


username = driver.find_element(By.NAME,'sid')
username.send_keys("0123")

#
password = driver.find_element(By.NAME,"PIN")
password.send_keys("Password")

link = driver.find_element(By.XPATH,'/html/body/div[4]/form/p/input[1]')
link.click()

link = driver.find_element(By.LINK_TEXT ,'Enrolment & Academic Records').click()
link = driver.find_element(By.LINK_TEXT,'Registration and Exams').click()

link = driver.find_element(By.LINK_TEXT,'Add or Drop Classes').click()
# value for winter is 202310
link = driver.find_element(By.XPATH,"//select[@name='term_in']/option[@value='202310']").click()

link = driver.find_element(By.XPATH,"//input[@type='submit' and @value='Submit']").click()

crns= ["empty","1801","1802","1803","1804","1805","1806","1807","1808","1809","1810"]
for i in range (1,len(crns)):
  id = 'crn_id' + str(i)
  print(id)
  crn = driver.find_element(By.ID,id)
  crn.send_keys(crns[i])

time.sleep(5)
#
#
#
#
#
#
#
#
#
