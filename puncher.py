import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def punch(
    acud_token: str,
    account: str,
    password: str,
    wait_second: int = 10,
    randomness_start: int = 60,
    randomness_end: int = 1200,
) -> bool:
    t = random.randint(randomness_start, randomness_end)
    time.sleep(t)
    browser = webdriver.Remote(
        command_executor='http://chrome-puncher:4444/wd/hub',
        options=webdriver.ChromeOptions()
    )
    try:
        browser.get('https://bsignin.104.com.tw/login')
        browser.add_cookie({'name': 'ACUD', 'value': acud_token, 'domain': 'bsignin.104.com.tw'})
        browser.get('https://bsignin.104.com.tw/login')
        browser.refresh()
        time.sleep(wait_second)

        account_input = browser.find_element(By.XPATH,'//input[@placeholder="輸入您的電子信箱"]')
        account_input.send_keys(account)

        password_input = browser.find_element(By.XPATH,'//input[@placeholder="輸入密碼，區分大小寫"]')
        password_input.send_keys(password)

        button = browser.find_element(By.XPATH, '//button[contains(text(), "立即登入")]')
        button.click()

        wait = WebDriverWait(browser, wait_second)
        link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://pro.104.com.tw/"]')))
        link.click()

        browser.get('https://pro.104.com.tw/psc2')

        time.sleep(wait_second)
        count = 0
        success = False
        while count < 10 and not success:
            try:
                elements = browser.find_elements(By.XPATH, '//span[text()="Clock in/out"]')
                elements[2].click()
                success = True
                print('Punch successfully')
            except Exception as e:
                print(f'Punch failed due to {e}, try times: {count}')
                count += 1
                time.sleep(wait_second)
        time.sleep(wait_second)

    except Exception as e:
        print(e)

    browser.quit()

    return True
