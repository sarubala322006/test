from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

EMAIL = "your_registered_email@gmail.com"
PASSWORD = "YourPassword"

@allure.feature("Login Module")
@allure.story("Valid Login")
@allure.title("Valid Login Test")

def test_valid_login():

    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    with allure.step("Open Tichi Website"):
        driver.get("https://tichi-app-webapp-stage.web.app")

    with allure.step("Click Sign In Button"):
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign In')]"))
        ).click()

    with allure.step("Enter Email Address"):
        wait.until(
            EC.visibility_of_element_located((By.ID, "email"))
        ).send_keys(EMAIL)

    with allure.step("Click Continue Button"):
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))
        ).click()

    with allure.step("Enter Password"):
        wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        ).send_keys(PASSWORD)

    with allure.step("Click Login Button"):
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

    with allure.step("Capture Screenshot"):
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Login Result",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Print Current URL"):
        print("Current URL:", driver.current_url)

    driver.quit()