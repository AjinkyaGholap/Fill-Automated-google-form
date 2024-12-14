from selenium import webdriver
import time

web=webdriver.Chrome()
web.get('https://forms.gle/WT68aV5UnPajeoSc8')
time.sleep(2)

full_name='Ajinkya Gholap'
name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(full_name)
time.sleep(2)

contact_number='8484981685'
phone=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
phone.send_keys(contact_number)
time.sleep(2)

email='aajinkya@gmail.com'
mail=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
mail.send_keys(email)
time.sleep(2)

address='Telhara, Akola, Maharashtra'
addr=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
addr.send_keys(address)
time.sleep(2)

pin_code='444-108'
pin=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
pin.send_keys(pin_code)
time.sleep(2)

birth_date='09-08-2002'
birth=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
birth.send_keys(birth_date)
time.sleep(2)

gender='male'
gen=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
gen.send_keys(gender)
time.sleep(2)

check_code='GNFPYC'
code=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
code.send_keys(check_code)
time.sleep(1)

submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()
time.sleep(1)