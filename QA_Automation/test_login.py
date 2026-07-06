from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Test Data
EMAIL = "ranivaniemail@gmail.com"
PASSWORD = "Abc@12345"

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

    # Signup page opens for new users
    with allure.step("Enter First Name"):
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your first name']"))
        ).send_keys("Rani")

    with allure.step("Enter Last Name"):
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your last name']"))
        ).send_keys("Vani")

    with allure.step("Enter Mobile Number"):
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your phone number']"))
        ).send_keys("9876543210")

    with allure.step("Enter Password"):
        wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        ).send_keys(PASSWORD)

    with allure.step("Enter Confirm Password"):
        wait.until(
            EC.visibility_of_element_located((By.ID, "confirmPassword"))
        ).send_keys(PASSWORD)

    # Uncomment if Terms & Conditions checkbox is required
    # with allure.step("Accept Terms and Conditions"):
    #     wait.until(
    #         EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
    #     ).click()

    with allure.step("Click Sign Up Button"):
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign Up')]"))
        ).click()

    with allure.step("Capture Screenshot"):
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Signup Result",
            attachment_type=allure.attachment_type.PNG
        )

    print("Current URL:", driver.current_url)

    driver.quit()