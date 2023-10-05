# import from selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


import time
import mysql.connector
#import local libarry
from connect_to_driver import my_driver




#############################################
def get_shop_info(driver, city, post_code):
    CITY = []
    POST = []
    Shop_name = []
    Address = []
    Phone_number = []
    Day = []
    Hour = []
    Menu = []
    
    driver.get(f"https://www.google.com/search?sca_esv=566856875&tbs=lf:1,lf_ui:9&tbm=lcl&q={post_code}+takeaway&rflfq=1&num=10&sa=X&ved=2ahUKEwi7kvub87iBAxUWVkEAHUH3DmgQjGp6BAgaEAE&biw=1528&bih=749")
    time.sleep(2)
    
    while True:
        try:
            shop_detail = driver.find_elements(By.CLASS_NAME,'dbg0pd ')
            print('ok')
        except:
            continue
        
        for i in shop_detail:
            action = ActionChains(driver)

            # click the item
            action.click(on_element=i)

            # perform the operation
            action.perform()
            time.sleep(1)
            try:
                shop_name = driver.find_element(By.CLASS_NAME, 'SPZz6b').text
                # print(shop_name)
            
                Shop_name.append(shop_name)
                time.sleep(1) 
            except:
                Shop_name.append("Sponser")
                
                
            # appending City and Post Code to list
            CITY.append(city)
            POST.append(post_code)
            try:
                adress = driver.find_element(By.CLASS_NAME, "LrzXr").text
                Address.append(adress)
                # print(adress)
            except:
                Address.append("Empty")
                pass
            time.sleep(1)
            
            # find phone number and appended to a list

            
            try:
                phone_number = driver.find_element(By.CSS_SELECTOR, "span.LrzXr:nth-child(1)").text
                
                Phone_number.append(phone_number)
                # print(phone_number)
            except:
                Phone_number.append("Empty")
                pass

            # find Open Hour and appended to a list

            try:
                click_hours = driver.find_element(By.CLASS_NAME,'BTP3Ac')
                click_hours.click()
                time.sleep(2)
                table1 = driver.find_elements(By.CSS_SELECTOR, ".WgFkxc > tbody>tr")
                days = []
                open_hour = []
                
                for time in table1:
                    day = time.text
                    days.append(day.split(" ")[0])
                    open_close = day.split(" ")[1:]

                
                    # find open hour
                    open_hour.append(open_close[0].replace("\u202f", " "))
                Day.append(days)
                Hour.append(open_hour)
              
                # print(days)
                # print(Day)
            except:
                Day.append('Empty')
                Hour.append("Empty")
 
            # find menu and appended to a list
           
            try:
                menu = driver.find_element(By.CLASS_NAME, "JV5xkf").text
                
                Menu.append(menu.replace("Menu: ", ""))                
                # print(menu)
               
            except:
                 Menu.append("Empty")                
            
        # Click for next page

           
        try: 
            nextButton = driver.find_element(By.ID, "pnnext")
            nextButton.click()
            time.sleep(2)
            
        except:
            print("Reached the last page")
            break
        
        
        
    return CITY, POST, Shop_name, Address, Phone_number, Day, Hour, Menu
       

