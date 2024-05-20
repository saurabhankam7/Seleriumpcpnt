import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
# Variable Declaration
username = "Ahmednagar MC/137"
password = "    "

# URL Of The Login Page
login_url = "https://pcpndt.maharashtra.gov.in/Home/Login.aspx"

# Set up Chrome options
options = Options()
custom_cache_dir = r"C:\\PythonError"
options.add_argument(f"user-data-dir={custom_cache_dir}")
# driver = webdriver.Chrome()
# Path to ChromeDriver
chromedriver_path = r'C:\PythonScript\chromedriver.exe'
service = Service(chromedriver_path)

# Initialize WebDriver with options
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the login page
    driver.get(login_url)

    # Wait for the username field to be present and enter the username
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtusername'))).send_keys(username)

    # Wait for the password field to be present and enter the password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtpassword'))).send_keys(password)

    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='ctl00_CPH_btnlogin']"))
    )
    login_button.click()
    fname="ABC"
    mname="EFG"
    lname="XYZ"
    age=20
    address="Radison blue, mumbai-400001"
    contact=1234567890
    dayslastcheck=25
    val=1
    child1year=20
    child1month=2
    child2year=10
    child2month=2
    child3year=9
    child3month=2
    child4year=8
    child4month=2
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtFirstName'))).send_keys(fname)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtMiddleName'))).send_keys(mname)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(lname)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(age)
    dropdown = Select(driver.find_element(By.ID, 'ctl00_CPH_ddlMaleChild'))
    dropdown.select_by_value(val)
    # if val==1:
    #     pass
    # elif val==1:
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child1year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child1month)  
    # elif val==2:
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child1year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child1month)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child2year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child2month)  
    # elif val==3:
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child1year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child1month)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child2year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child2month)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child3year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child3month)  
    # elif val==4:
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child1year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child1month)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child2year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child2month)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child3year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child3month)  
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtSurname'))).send_keys(child4year)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientage'))).send_keys(child4month)  
    dropdown1 = Select(driver.find_element(By.ID, 'ctl00_CPH_ddlFemaleChild'))
    dropdown1.select_by_value(val)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtPatientaddress'))).send_keys(address)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_CPH_txtContactnumber'))).send_keys(contact)
    table = driver.find_element(By.ID, 'ctl00_CPH_rbReferType')
    radio_button = table.find_element(By.ID, 'ctl00_CPH_rbReferType_1')
    radio_button.click()
    dropdown = Select(driver.find_element(By.ID, 'ctl00_CPH_ddlSelRefer'))
    dropdown.select_by_value("Registered Medical Practioner~2003/08/3130~Abhijeet Shinde")
    input_field = driver.find_element(By.ID, 'ctl00_CPH_txtPatientMenses')
    input_field.clear()
    input_field.send_keys("07/05/2024")
    input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'ctl00$CPH$txtLMP')))
    driver.execute_script("arguments[0].removeAttribute('readonly')", input_field)
    input_field.send_keys(dayslastcheck)
    time.sleep(30)
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Script execution completed. Closing WebDriver session.")
    driver.quit()
