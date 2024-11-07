#DONE
from conftest import *

def test_login(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(20)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("vonhan6000@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345678WW@")
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        print("Đăng nhập không thành công: ", error_message.text)
        return
    except TimeoutException:
        print("Không có thông báo lỗi đăng nhập. Tiếp tục kiểm tra URL...")

        # In ra URL hiện tại để kiểm tra
    print("URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)

    try:
        WebDriverWait(driver, 10).until(EC.url_contains("account/account"))
        assert "account/account" in driver.current_url,"Log in successfully! You have been redirected to the account page."
        print("Đăng nhập thành công! Bạn đã được chuyển hướng đến trang tài khoản.")
    except TimeoutException:
        print("Đăng nhập không thành công hoặc URL không thay đổi. URL hiện tại:", driver.current_url)


def test_login_wronginput(driver): #PASS
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    email_field = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.ID, "input-email")))
    email_field.send_keys("nguoivana2gmail.com")

    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("1")
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    time.sleep(5)

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        print("Đăng nhập không thành công: ", error_message.text)
        print("URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thất bại, không chuyển hướng sang trang tài khoản.")
        return
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.url_contains("account/account"))
        print("Không có thông báo lỗi đăng nhập. URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thành công! Bạn đã được chuyển hướng đến trang tài khoản.")


def test_login_wrong_password(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "input-email")))
    email_field.send_keys("nguoivanvoST@gmail.com")

    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("WRong1pass123")
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    time.sleep(5)

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        print("Đăng nhập không thành công: ", error_message.text)
        print("URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thất bại, không chuyển hướng sang trang tài khoản.")
        return
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.url_contains("account/account"))
        print("Không có thông báo lỗi đăng nhập. URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thành công! Bạn đã được chuyển hướng đến trang tài khoản.")


# PASS
def test_login_empty_password(driver): # PASS
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-email")))
    email_field.send_keys("nguoivanvoST@gmail.com")

    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    time.sleep(5)

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        print("Đăng nhập không thành công: ", error_message.text)
        print("URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thất bại, không chuyển hướng sang trang tài khoản.")
        return
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.url_contains("account/account"))
        print("Không có thông báo lỗi đăng nhập. URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thành công! Bạn đã được chuyển hướng đến trang tài khoản.")


def test_login_empty_email(driver): #PASS
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)


    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("12345678WW@")
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    time.sleep(5)

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        print("Đăng nhập không thành công: ", error_message.text)
        print("URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thất bại, không chuyển hướng sang trang tài khoản.")
        return
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.url_contains("account/account"))
        print("Không có thông báo lỗi đăng nhập. URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thành công! Bạn đã được chuyển hướng đến trang tài khoản.")


def test_login_w_special_symbols_email(driver): # Kiểm tra đăng nhập với email chứa ký tự đặc biệt
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "input-email")))
    email_field.send_keys("@#%A^^#$@!@!#.com")

    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("WRong123")
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    time.sleep(5)

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        print("Đăng nhập không thành công: ", error_message.text)
        print("URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thất bại, không chuyển hướng sang trang tài khoản.")
        return
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.url_contains("account/account"))
        print("Không có thông báo lỗi đăng nhập. URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thành công! Bạn đã được chuyển hướng đến trang tài khoản.")


# # PASS
def test_login_w_special_symbols_password(driver): # Kiểm tra đăng nhập với mật khẩu chứa ký tự đặc biệt
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    email_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "input-email")))
    email_field.send_keys("nguoivanvoST@gmail.com")

    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("%#@(#^!@#@#!#")
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    time.sleep(5)

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        print("Đăng nhập không thành công: ", error_message.text)
        print("URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thất bại, không chuyển hướng sang trang tài khoản.")
        return
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.url_contains("account/account"))
        print("Không có thông báo lỗi đăng nhập. URL hiện tại sau khi nhấn đăng nhập:", driver.current_url)
        print("Đăng nhập thành công! Bạn đã được chuyển hướng đến trang tài khoản.")


def test_login_sql_invalid(driver):  #PASS
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    # Điền dữ liệu SQL injection vào trường email
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "input-email"))
    )
    email_input.send_keys("' UNION SELECT NULL, username, password FROM users -- ")

    # Điền dữ liệu SQL injection vào trường mật khẩu
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "input-password"))
    )
    password_input.send_keys("' UNION SELECT NULL, username, password FROM users -- ")
    time.sleep(2)

    # Nhấn nút đăng nhập
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(5)

    # Kiểm tra thông báo lỗi sau khi nhấn đăng nhập
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        print("Tấn công SQL injection không thành công: ", error_message.text)
    except TimeoutException:
        print("Không có thông báo lỗi khi thực hiện SQL injection.")

    # Kiểm tra URL hiện tại sau khi thử đăng nhập
    current_url = driver.current_url
    print("URL hiện tại sau khi thử đăng nhập bằng SQL injection:", current_url)

    # Kiểm tra nếu không có sự chuyển hướng đến trang tài khoản
    if "account/account" not in current_url:
        print("Tấn công SQL injection thất bại, không có chuyển hướng đến trang tài khoản.")
    else:
        print("Có vẻ như tấn công SQL injection thành công, đã chuyển hướng đến trang tài khoản.")
