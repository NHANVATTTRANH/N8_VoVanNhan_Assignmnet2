#DONE
from conftest import *

def test_register_valid_user(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(5)

    first_name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name.send_keys("Vo")

    last_name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-lastname"))
    )
    last_name.send_keys("Nhan")

    email_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-email"))
    )
    email_input.send_keys("vonhan6001@gmail.com")

    password_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-password"))
    )
    password_input.send_keys("12345678WW@")
    time.sleep(5)

    privacy_checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].click();", privacy_checkbox)
    time.sleep(5)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(5)

    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1"))
        )

        assert success_message.is_displayed(), "Failed to display success message."
        assert "Your Account Has Been Created!" in success_message.text, "Unexpected account creation message."

    except Exception as e:
        print("Error encountered:", e)
        print("Page source:", driver.page_source)

def test_register_invalid_email(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(5)

    first_name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name.send_keys("Vo")

    last_name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-lastname"))
    )
    last_name.send_keys("Nhan")

    email_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-email"))
    )
    email_input.send_keys("vonhan60012gmail.com")

    password_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "input-password"))
    )
    password_input.send_keys("12345678WW@")

    privacy_checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].click();", privacy_checkbox)
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    time.sleep(5)

    try:
        email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email validation error is not shown."
        assert "E-Mail Address does not appear to be valid!" in email_error.text, "Incorrect email error message."

    except Exception as e:
        print("Error encountered:", e)

def test_register_existing_account(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(5)

    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name.send_keys("nhung")

    last_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-lastname"))
    )
    last_name.send_keys("Vo")

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-email"))
    )
    email_input.send_keys("vonha318@gmail.com")

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-password"))
    )
    password_input.send_keys("12345678Ww@!")

    privacy_checkbox = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].click();", privacy_checkbox)
    time.sleep(5)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(5)

    try:
        email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email error message not shown."
        assert "E-Mail Address is already registered!" in email_error.text, "Unexpected email error message."

    except Exception as e:
        print("Error encountered:", e)

def test_register_missing_required_fields(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/register&language=en-gb")
    time.sleep(5)

    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name.send_keys("nhung")

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-email"))
    )
    email_input.send_keys("nhungnhungnhung@gmail.com")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(5)

    try:
        first_name_error = driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div[@class='text-danger']")
        assert first_name_error.is_displayed(), "First name validation error is missing."
        assert "First Name must be between 1 and 32 characters!" in first_name_error.text, "First name error message is incorrect."

        last_name_error = driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div[@class='text-danger']")
        assert last_name_error.is_displayed(), "Last name validation error is missing."
        assert "Last Name must be between 1 and 32 characters!" in last_name_error.text, "Last name error message is incorrect."

        email_error = driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email validation error is missing."
        assert "E-Mail Address does not appear to be valid!" in email_error.text or "E-Mail Address must be between 1 and 96 characters!" in email_error.text, "Email error message is incorrect."

        password_error = driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div[@class='text-danger']")
        assert password_error.is_displayed(), "Password validation error is missing."
        assert "Password must be between 4 and 20 characters!" in password_error.text, "Password error message is incorrect."

    except Exception as e:
        print("Error encountered:", e)
        print("Current page source:", driver.page_source)
