from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""
PHONE = ""


def abort_application():
    close = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close.click()

    sleep(2)
    discard = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

sleep(2)
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()

sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
sleep(5)
lists = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for each in lists:
    print("Opening Listing")
    each.click()
    sleep(2)
    try:
        apply = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply.click()
        sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        print(submit_button.get_attribute('data-control-name'))

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()