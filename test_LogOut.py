#DONE
from conftest import *

def test_logout(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    print(driver.current_url)  # Print initial URL after loading the login page
    time.sleep(5)

    # Log in
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("vonha318@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345678WW@")
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print(driver.current_url)  # Print URL after logging in

    # Open account menu and select "Logout"
    myAccount_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-toggle' and @data-bs-toggle='dropdown']"))
    )
    driver.execute_script("arguments[0].click();", myAccount_dropdown)
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )
    driver.execute_script("arguments[0].click();", logout_link)
    time.sleep(2)
    print(driver.current_url)  # Print URL after clicking "Logout"

    # Check for successful logout
    WebDriverWait(driver, 10).until(
        EC.url_contains("account/logout")
    )
    assert "account/logout" in driver.current_url, "Logout was not successful."

    # Click the "Continue" button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Continue"))
    )
    driver.execute_script("arguments[0].click();", continue_button)
    time.sleep(2)
    print(driver.current_url)  # Print URL after clicking "Continue"

    # Verify redirection to the homepage
    WebDriverWait(driver, 10).until(
        EC.url_contains("common/home")
    )
    assert "common/home" in driver.current_url, "User was not redirected to the homepage after clicking 'Continue'."
