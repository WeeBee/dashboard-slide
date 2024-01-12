# *********************** #
# *** Dashboard Slide *** #
# 2024, Wilson Pereira Jr #
# *********************** #
import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
logging.basicConfig(filename='dashboard.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
print('\n*** WeeBee Dashboard 2024 ***\n')
print('Web Driver: ' + str(os.popen('where.exe chromedriver.exe', 'r').read()))
print(str(os.popen('chromedriver.exe --version', 'r').read()))
options = Options()
options.add_argument("--start-fullscreen")
options.add_argument("force-device-scale-factor=0.75")
options.add_argument("high-dpi-support=0.75")
options.add_experimental_option("excludeSwitches", ['enable-automation'])
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options)
usr_grafana = os.environ.get('USR_GRAFANA')
pwd_grafana = os.environ.get('PWD_GRAFANA')
usr_splunk = os.environ.get('USR_SPLUNK')
pwd_splunk = os.environ.get('PWD_SPLUNK')
#seconds to wait on each domain:
SPLUNK = 3
POWERBI = 4
GRAFANA = 5
DYNATRACE = 6
urls = {
	"https://www.google.com":DYNATRACE,
	"https://www.microsoft.com":GRAFANA,
	"https://www.apple.com":SPLUNK,
	"https://www.amazon.com":POWERBI
}

def login_grafana():
	try:
		driver.find_element("name", "user").send_keys(usr_grafana)
		wait(1)
		driver.find_element("name", "password").send_keys(pwd_grafana)
		wait(1)
		driver.find_element(By.XPATH, '//*[@id="reactRoot"]/div[1]/main/div[3]/div/div[2]/div/div/form/button').click()
		wait(1)
	except Exception:
		pass
def login_splunk():
	try:
		driver.find_element("id", "username").send_keys(usr_splunk)
		wait(1)
		driver.find_element("id", "password").send_keys(pwd_splunk)
		wait(1)
		driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/form/fieldset/input[1]").click()
	except Exception:
		pass
def wait(secs):
	try:
		time.sleep(secs)
	except Exception:
		time.sleep(60)
def zoom_out():
	driver.execute_script("document.body.style.zoom='0.5'")

# main
try:
	while True:
		for k,v in urls.items():
			driver.get(k)
			if v == SPLUNK:
				login_splunk()
			elif v == GRAFANA:
				login_grafana()
				zoom_out()
			elif v == DYNATRACE:
				zoom_out()
			driver.execute_script("document.body.style.cursor='none'")
			wait(v)
except KeyboardInterrupt:
	driver.close()
except Exception as err:
	logger.error(err)

