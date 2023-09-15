from py import test
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

assert isinstance(test, object)
test
driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)

driver.implicitly_wait(100)
driver.get("https://my.testing.ringplan.com/")

login_liefd = driver.find_element(By.XPATH, '//*[@id="signInName"]')
login_liefd.send_keys("donttouchmyaccman@mailinator.com")

pass_field = driver.find_element(By.XPATH, '//*[@id="password"]')
pass_field.send_keys("Qwerty123!")

sign_in_button = driver.find_element(By.CSS_SELECTOR, '#next')
sign_in_button.click()


close_pop_up = driver.find_element(By.CSS_SELECTOR,'body > modal-container > '
                                                   'div.modal-dialog.modal-dialog-centered.modal-initial-download-apps > div > ssp-download-apps-modal > modal-wrapper > div.modal-header-new > div.svg-close.force')
close_pop_up.click()

duration_colum = driver.find_element(By.CSS_SELECTOR, 'body > ssp-app-root > app-main > div > section > div > '
                                                      'app-dashboard > section > div > div.main-block > '
                                                      'div:nth-child(3) > div:nth-child(2) > calls-source > section > '
                                                      'div > div > btn-group > section > div.button.small.active')
duration_colum.click()

log_out_button = driver.find_element(By.CSS_SELECTOR, 'body > ssp-app-root > app-main > app-header > section > '
                                                      'div.right-block > div.logout-link')
log_out_button.click()

driver.close()
