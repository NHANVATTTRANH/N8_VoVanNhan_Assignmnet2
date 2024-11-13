# OpenCart Selenium Test Suite Setup Guide

## Prerequisites
- Python 3.8 or higher
- PyCharm IDE
- Google Chrome Browser

## Environment Setup

	1. Clone the repository to your local machine
	2. Open PyCharm and create a new project
	3. Open the project terminal in PyCharm and install required packages:

pip install pytest
pip install selenium
pip install webdriver-manager

## Project Structure
	selenium_tests/
	├── assets/
 		style.css
 	├── report.html
	├── test_1_login_logout.py
	├── test_2_form_submission.py
	├── test_3_navigation.py
	├── test_4_data_validation.py
	├── test_5_error_handling.py
	├── test_6_search_functionality.py
	├── test_7_responsive_design.py
	└── requirements.txt

##	Setting Up Test Environment
	1. Open PyCharm and go to File > Settings > Project > Python Interpreter
	2. Click the gear icon and select "Add"
	3. Choose "Virtual Environment" and click "OK"
	4. Wait for PyCharm to create and configure the virtual environment

##	Running Tests
### Method 1: Running Individual Test Files
	1. Right-click on any test file
	2. Select "Run 'pytest in test_1...'"
### Method 2: Running from Terminal
	1. Open PyCharm terminal
	2. Navigate to the project directory
	3. Run individual test files:
### Method 3: Running All Tests
	To run all test files:
pytest -v

## Troubleshooting
	1. ChromeDriver Error: If you get a ChromeDriver error, ensure Chrome browser is up to date
	2. Connection Error: Verify OpenCart is running 
	3. Import Error: Make sure all required packages are installed in your virtual environment

### Execute from Command Line
To run all the tests, navigate to the project folder and run:
   
pytest N8_VoVanNhan_Assignment2

### Generate HTML Test Report in Python
To generate an HTML report for a Selenium test, you need to install a plugin by running the command:
pip install pytest-html
To create the report, move from the current directory to the directory containing the Pytest file you want to execute. Then, run the command:
pytest --html=report.html

Once this command is successfully executed, a new file named report.html will be created in the project folder.
