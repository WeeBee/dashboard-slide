# *********************** #
# *** Dashboard Slide *** #
# 2023, Wilson Pereira Jr #
# *********************** #
import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
logging.basicConfig(filename='dashboard.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
print('\n*** WeeBee Dashboard 2023 ***\n')
print('Web Driver: ' + str(os.popen('where.exe chromedriver.exe', 'r').read()))
print(str(os.popen('chromedriver.exe --version', 'r').read()))
options = Options()
options.add_argument("--start-fullscreen")
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options)
usrGrafana = os.environ.get('USR_GRAFANA')
pwdGrafana = os.environ.get('PWD_GRAFANA')
usrSplunk = os.environ.get('USR_SPLUNK')
pwdSplunk = os.environ.get('PWD_SPLUNK')
#seconds to wait on each domain:
SPLUNK = 30
POWERBI = 58
GRAFANA = 59
DYNATRACE = 60
urls = {
	"https://www.google.com":DYNATRACE,
	"https://www.microsoft.com":GRAFANA,
	"https://www.apple.com":SPLUNK,
	"https://www.amazon.com":POWERBI
}

def loginGrafana():
	try:
		driver.find_element("name", "user").send_keys(usrGrafana)
		wait(1)
		driver.find_element("name", "password").send_keys(pwdGrafana)
		wait(1)
		driver.find_element(By.XPATH, '//*[@id="reactRoot"]/div[1]/main/div[3]/div/div[2]/div/div/form/button').click()
		wait(1)
	except Exception:
		pass
def loginSplunk():
	try:
		driver.find_element("id", "username").send_keys(usrSplunk)
		wait(1)
		driver.find_element("id", "password").send_keys(pwdSplunk)
		wait(1)
		driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/form/fieldset/input[1]").click()
	except Exception:
		pass
def wait(secs):
	try:
		time.sleep(secs)
	except Exception:
		time.sleep(60)
def zoomOut():
	driver.execute_script("document.body.style.zoom='0.5'")

# main
try:
	while True:
		for k,v in urls.items():
			driver.get(k)
			if v == SPLUNK:
				loginSplunk()
			elif v == GRAFANA:
				loginGrafana()
				zoomOut()
			elif v == DYNATRACE:
				zoomOut()
			driver.execute_script("document.body.style.cursor='none'")
			wait(v)
except KeyboardInterrupt:
	driver.close()
except Exception as err:
	logger.error(err)
