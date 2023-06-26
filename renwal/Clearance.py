from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bidi.algorithm import get_display
from arabic_reshaper import reshape

url='https://www.amman.jo/ar/clearance/clearance.aspx'
driver = webdriver.Firefox()
driver.get(url)

wait = WebDriverWait(driver,50)


user_nat_no = 9912017766
persone_card_no = '743/818'

radio_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='1']")))
radio_button.click()
# time.sleep(1)

radio_button2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='0101']")))
radio_button2.click()
# time.sleep(1)

user_nat_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_persone_nat"]')))
user_nat_no_input_field.clear()
user_nat_no_input_field.send_keys(user_nat_no)

user_persone_card_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_persone_card_no"]')))
user_persone_card_no_input_field.clear()
user_persone_card_no_input_field.send_keys(persone_card_no)

check_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="تحقق معلومات مقدم الطلب"]')))
time.sleep(2)
check_button.click()
time.sleep(20)

# text_print = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[@id="ctl00_ContentPlaceHolder1_lbl_chk_order_ok"]')))
# print('your order is approved',text_print.text)

radio_button3 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='63']")))
radio_button3.click()

user_phone_no = '0798724657'

user_phone_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_owner_phone"]')))
user_phone_no_input_field.clear()
user_phone_no_input_field.send_keys(user_phone_no)

save_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="حفظ بيانات الطلب"]')))
time.sleep(2)
save_button.click()


try :
     element = wait.until(EC.presence_of_element_located((By.XPATH,'//td[@class="buildwhitesitefont"]')))
     if element :
#  print('element', 'تم تقديم الطلب بنجاح , رقم الطلب :632300224 , الخدمة : براءة الذمة الالكترونية')
         print(element.text[::-1])

except :
    element_except = wait.until(EC.presence_of_element_located((By.XPATH,'//span[@id="ctl00_ContentPlaceHolder1_lblmsg"]')))

    print(element_except.text[::-1])

