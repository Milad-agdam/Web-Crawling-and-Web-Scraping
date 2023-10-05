import time
import pandas as pd
from connect_to_driver import my_driver
# from adding_exel_file import adding_exel
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import mysql.connector
from getshop import get_shop_info

# read excel file 
df = pd.read_excel('postcode.xlsx')
driver = my_driver()
driver.get("https://www.google.com/search?sca_esv=566856875&tbs=lf:1,lf_ui:9&tbm=lcl&q=AB1+takeaway&rflfq=1&num=10&sa=X&ved=2ahUKEwi7kvub87iBAxUWVkEAHUH3DmgQjGp6BAgaEAE&biw=1528&bih=749")
driver.delete_all_cookies()
time.sleep(1)
reject = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button')
reject.click()
time.sleep(1)

for city , post in zip(df['City'],df['Postcode']):
    try:
        (CITY, POST, Shop_name, Address, Phone_number, Day, Hour, Menu) = get_shop_info(driver, city, post)
        print(f"City: {CITY} Post code: {POST} Shop Name:{Shop_name} Address: {Address} Phone number: {Phone_number}")
        for city , post , shop_name , address , phone_number , day , hour, menu in zip(CITY, POST, Shop_name, Address, Phone_number, Day, Hour, Menu):
            # print(day)
            # print(hour)
            if day!='Empty' and len(day)==7:

                try:

                    mydb = mysql.connector.connect(
                          host="host-name",
                          user="username",
                          password="pass",
                          database="data base name"
                    )
                    mycursor = mydb.cursor()
                    sql = "SELECT shop_name, Address FROM data base name WHERE Shop_name = %s and Address = %s and post = %s"
                    val = (shop_name, address, post)
                    mycursor.execute(sql, val)

                    # if the record does not exist, insert a new record
                    if mycursor.fetchone() is None:

                        if day[0]=='Saturday':

                            sql = "INSERT INTO data base name (City,post,Shop_name,Address,Phone_Number,Menu,Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday," \
                                "Friday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
                            val = ('{}'.format(city), '{}'.format(post),'{}'.format(shop_name), '{}'.format(address),'{}'.format(phone_number), '{}'.format(menu), '{}'.format(hour[0]),'{}'.format(hour[1]), '{}'.format(hour[2]),'{}'.format(hour[3]), '{}'.format(hour[4]), '{}'.format(hour[5]),'{}'.format(hour[6]))

                        if day[0]=='Sunday':
                            sql = "INSERT INTO data base name(City,post,Shop_name,Address,Phone_Number,Menu,Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = ('{}'.format(city), '{}'.format(post),'{}'.format(shop_name), '{}'.format(address),'{}'.format(phone_number), '{}'.format(menu), '{}'.format(hour[6]),'{}'.format(hour[0]),'{}'.format(hour[1]), '{}'.format(hour[2]),'{}'.format(hour[3]), '{}'.format(hour[4]), '{}'.format(hour[5]))

                        if day[0]=='Monday':
                            sql = "INSERT INTO data base name(City,post,Shop_name,Address,Phone_Number,Menu,Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val =  ('{}'.format(city), '{}'.format(post),'{}'.format(shop_name), '{}'.format(address),'{}'.format(phone_number), '{}'.format(menu), '{}'.format(hour[5]),'{}'.format(hour[6]),'{}'.format(hour[0]),'{}'.format(hour[1]),'{}'.format(hour[2]),'{}'.format(hour[3]),'{}'.format(hour[4]))
                            
                        if day[0]=='Tuesday':
                            sql = "INSERT INTO data base name(City,post,Shop_name,Address,Phone_Number,Menu,Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = ('{}'.format(city), '{}'.format(post),'{}'.format(shop_name), '{}'.format(address),'{}'.format(phone_number), '{}'.format(menu), '{}'.format(hour[4]),'{}'.format(hour[5]),'{}'.format(hour[6]),'{}'.format(hour[0]),'{}'.format(hour[1]), '{}'.format(hour[2]),'{}'.format(hour[3]))

                        if day[0]=='Wednesday':
                            sql = "INSERT INTO data base name(City,post,Shop_name,Address,Phone_Number,Menu,Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = ('{}'.format(city), '{}'.format(post),'{}'.format(shop_name), '{}'.format(address),'{}'.format(phone_number), '{}'.format(menu),'{}'.format(hour[3]),'{}'.format(hour[4]),'{}'.format(hour[5]),'{}'.format(hour[6]),'{}'.format(hour[0]),'{}'.format(hour[1]), '{}'.format(hour[2]))

                        if day[0]=='Thursday':
                            sql = "INSERT INTO data base name(City,post,Shop_name,Address,Phone_Number,Menu,Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = ('{}'.format(city), '{}'.format(post),'{}'.format(shop_name), '{}'.format(address),'{}'.format(phone_number),'{}'.format(menu), '{}'.format(hour[2]),'{}'.format(hour[3]),'{}'.format(hour[4]),'{}'.format(hour[5]),'{}'.format(hour[6]),'{}'.format(hour[0]),'{}'.format(hour[1]))

                        if day[0]=='Friday':
                            sql = "INSERT INTO data base name(City,post,Shop_name,Address,Phone_Number,Menu,Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = ('{}'.format(city), '{}'.format(post),'{}'.format(shop_name), '{}'.format(address),'{}'.format(phone_number),'{}'.format(menu), '{}'.format(hour[1]),'{}'.format(hour[2]),'{}'.format(hour[3]),'{}'.format(hour[4]),'{}'.format(hour[5]),'{}'.format(hour[6]),'{}'.format(hour[0]))

                        mycursor.execute(sql, val)

                        mydb.commit()
                    else:
                        print("Record already exists")
                        
                    print(mycursor.rowcount, "record inserted.")
                except mysql.connector.Error as err :
                    print(err)
                    #print(e)
                    #mysql.connector.errors
                    pass
                    #print("Shop does not have open hours")
            else:
                print("Shop does not have open hours")

    except TimeoutException as Tm:
        print('You have time error')
        pass


