# Tichi Login Automation

## Project Description
This project automates the Login functionality of the Tichi web application using Selenium WebDriver, Python, Pytest, and Allure Reports.

## Tools Used
- Python
- Selenium WebDriver
- Pytest
- Allure Report
- Google Chrome

## Test Scenario
- Valid Login

## Project Structure

Tichi_Automation/
├── test_login.py
├── requirements.txt
├── README.md

## How to Run

1. Install the required packages:

pip install -r requirements.txt

2. Execute the test:

pytest -s test_login.py --alluredir=allure-results

3. Generate the Allure Report:

allure serve allure-results

## Expected Result

The automation should:
- Open the Tichi website
- Click Sign In
- Enter login credentials
- Click Login
- Verify successful login
- Capture a screenshot in the Allure report