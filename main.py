from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with open("scraped_data.txt", "a", encoding="utf-8") as file:
    file.write("Scraped Data:\n")

record_counter = 1
page_counter = 1

while True:
    try:
        driver = webdriver.Chrome()
        if page_counter == 1:
            url = f"https://bar-register.bg/unified-registry/attorneys"
        else:
            url = f'https://bar-register.bg/unified-registry/attorneys?page={page_counter}'
        driver.get(url)
        time.sleep(2)

        current_counter = 1
        while True:
            try:
                layer_info_field_xpath = f"//html/body/div[3]/div/div/div/div/div[{current_counter}]/a/div/div[1]/p"
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, layer_info_field_xpath))).click()
                time.sleep(1)

                name_field_xpath = "/html/body/div[3]/div/div[1]/div/div/div[2]/div[2]/div/p[1]/strong"
                reg_number_xpath = "/html/body/div[3]/div/div[1]/div/div/div[2]/div[3]/div[1]/p/strong"
                tel_number_xpath = "/html/body/div[3]/div/div[1]/div/div/div[2]/div[4]/div[2]/div[1]"
                tel2_number_xpath = "/html/body/div[3]/div/div[1]/div/div/div[2]/div[4]/div[2]/div[2]"
                email_xpath = "/html/body/div[3]/div/div[1]/div/div/div[2]/div[4]/div[2]/div[3]"
                email2_xpath = "/html/body/div[3]/div/div[1]/div/div/div[2]/div[4]/div[2]/div[4]"
                kolegiq_xpath = "/html/body/div[2]/h2"
                sastoqnie_xpath = "/html/body/div[3]/div/div[1]/div/div/div[2]/div[2]/div/p[2]/span"
                adres_xpath = "/html/body/div[3]/div/div[1]/div/div/div[2]/div[4]/div[1]/p[2]"

                emails = []
                tel_numbers = []

                try:
                    kolegiq = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, kolegiq_xpath))).text
                except:
                    kolegiq = 'No name'

                try:
                    sastoqnie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, sastoqnie_xpath))).text
                except:
                    sastoqnie = 'No name'

                try:
                    adres = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, adres_xpath))).text
                except:
                    adres = 'No name'

                try:
                    layer_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name_field_xpath))).text
                except:
                    layer_name = 'No name'
                try:
                    reg_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, reg_number_xpath))).text
                except:
                    reg_number = 'No reg number'

                try:
                    tel_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, tel_number_xpath))).text
                    if "@" in tel_number:
                        email = tel_number
                        emails.append(email)
                    else:
                        tel_numbers.append(tel_number)
                except:
                    continue

                try:
                    tel2_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, tel2_number_xpath))).text
                    if "@" in tel2_number:
                        email = tel2_number
                        emails.append(email)
                    else:
                        tel_numbers.append(tel2_number)
                except:
                    continue

                try:
                    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, email_xpath))).text
                    emails.append(email)
                except:
                    email = 'No email'
                    email2 = 'No email2'

                try:
                    email2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, email2_xpath))).text
                    emails.append(email2)
                except:
                    email2 = 'No email2'

                # Save the information to a text file
                with open("scraped_data3.txt", "a", encoding="utf-8") as file:
                    file.write(f"{record_counter} -- {layer_name} -- {reg_number} -- {tel_numbers} -- {emails} -- {kolegiq} -- {sastoqnie} -- {adres}\n")

                print(f"{record_counter} - {layer_name} with reg_num {reg_number} and tel_num {tel_numbers} and email {emails}")

                current_counter += 1
                record_counter += 1
                driver.back()
            except:
                page_counter += 1
                break
    except:
        break

