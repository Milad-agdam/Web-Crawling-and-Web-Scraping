import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

def get_data(driver,  post_code):
	CITY = []
	POST = []
	Shop_name = []
	Address = []
	Phone_number = []
	Day = []
	Hour = []
	link = driver.get(f"https://www.google.com/search?sca_esv=566856875&tbs=lf:1,lf_ui:9&tbm=lcl&q={post_code}+takeaway&rflfq=1&num=10&sa=X&ved=2ahUKEwi7kvub87iBAxUWVkEAHUH3DmgQjGp6BAgaEAE&biw=1528&bih=749)
	# for i,j in zip(city_test, post_codes_test):
	search_box.clear()
	search_box.send_keys(f"{city} {post_code}"+" takeaway")
	search_box.send_keys(Keys.ENTER)
	time.sleep(6)
	time.sleep(6)
	restaurants = driver.find_element(By.CLASS_NAME, 'e2moi ')
	print('ok')
	restaurants.click()
	time.sleep(6)
	# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
	x = 0

	while True:
		x += 1
		els = driver.find_elements(By.CSS_SELECTOR, '.TFQHme')
		driver.execute_script("arguments[0].scrollIntoView();", els[-1])
		time.sleep(6)
		if x > 3:
			break
	shop_detail = driver.find_elements(By.CLASS_NAME,'hfpxzc ')
	for i in shop_detail:
		# create action chain object
		action = ActionChains(driver)

		# click the item
		action.click(on_element=i)

		# perform the operation
		action.perform()

		# i.click()
		time.sleep(6)
		print('-----------------------------------------')

		time.sleep(6)
		shop_name = driver.find_element(By.TAG_NAME, 'h1').text
		Shop_name.append(shop_name)
		time.sleep(6)
		CITY.append(city)
		POST.append(post_code)
		print(shop_name)
		try:
			adress = driver.find_element(By.CSS_SELECTOR,"[data-item-id='address']").text
			Address.append(adress)
			print(adress)
		except:
			Address.append(np.NAN)
			pass
		time.sleep(6)
		try:
			phone_number = driver.find_element(By.CSS_SELECTOR,"[data-tooltip='Copy phone number']").text
			Phone_number.append(phone_number)
			print(phone_number)
		except:
			Phone_number.append(np.NAN)
			pass
		time.sleep(6)
		try:

			click_hours = driver.find_element(By.CLASS_NAME,'o0Svhf')
			# ZDu9vd
			click_hours.click()
			time.sleep(6)
			days = driver.find_elements(By.CLASS_NAME, "ylH6lf ")
			times = driver.find_elements(By.CLASS_NAME, "mxowUb")
			#append Day to list
			day = [a.text for a in days]
			Day.append(day)
			print(day)
   


			open_close_time = [a.text for a in times]
			time.sleep(6)
			#append Hour to list
			open_close_time2= [element.replace('\u202f','').replace('\n', '') for element in open_close_time]
			Hour.append(open_close_time2)
			print(open_close_time2)

			#
			# # print(open_close_time)
			# open_close_time1 = [i.split('\n')[0] for i in open_close_time]
			# open_close_time2 = " ".join(open_close_time1)
		except:
			Day.append('Empty')
			Hour.append(np.NAN)
		
	return CITY, POST, Shop_name, Address, Phone_number, Day, Hour