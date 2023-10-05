from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def my_driver():
	option = Options()
	option.add_argument('--disable-infobars')
	option.add_argument("start-maximized")
	option.add_argument("--disable-extensions")
    
	# option.add_argument('--headless')

	option.add_experimental_option("prefs", {
		"profile.default_content_setting_values.notifications": 1
	})

	# chromedriver_path = 'C:/chromedriver.exe'
	my_webdriver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
	print('Driver connected')
	return my_webdriver

