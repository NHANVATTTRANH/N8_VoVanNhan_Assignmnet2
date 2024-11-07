import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pytest
import logging  
from selenium.webdriver.firefox.options import Options
from selenium.common import ElementClickInterceptedException

# Thiết lập fixture để khởi tạo và đóng trình duyệt
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

