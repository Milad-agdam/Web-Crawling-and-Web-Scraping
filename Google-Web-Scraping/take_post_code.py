from selenium.webdriver.common.by import By
from time import sleep
from connect_to_driver import my_driver


# city_name_list = []
# post_code_list = []
# city_name = ['Aberdeen', 'Widnes', 'Wrexham']


def post_cart(item):
	driver = my_driver()

	driver.get(f"https://www.just-eat.co.uk/takeaway/{item}")
	sleep(4)
	try:
		cookies = driver.find_element_by_class_name(
			"Button_o-btn_1KX8u.Button_o-btn--primary_NRuBe.Button_o-btn--sizeMedium_2uSln.Button_o-btn--fullWidth_1xkfh")
		cookies.click()
		driver.switch_to_default_content()
		sleep(3)

	except:
		pass
		sleep(1)
		last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Wait to load page
		sleep(9)

		# Calculate new scroll height and compare with last scroll height
		new_height = driver.execute_script("return document.body.scrollHeight / 2")
		if new_height == last_height:
			break
		last_height = new_height

		elements = driver.find_elements(By.CLASS_NAME, 'link-item')

		a_list = [element.text for element in elements]
		split_ = [i.split(' ')[:-1] for i in a_list]
		# area = [item[0].replace(',', '') for item in split_]
		post_code_list = [item[-1] for item in split_]
		# for item in split_:
		# 	city_name_list.append(item[0].replace(',', ''))
		# 	post_code_list.append(item[1])
		# print(f"{city_name_list} city and post card added!")

		sleep(10)
		return post_code_list
