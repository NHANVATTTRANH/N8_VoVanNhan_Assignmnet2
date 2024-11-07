#DONE
from conftest import *

def test_change_your_password(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("nhungnhungnhung@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("NewPassword123!")
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(5)

    change_password_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Change your password"))
    )
    change_password_link.click()
    print("Đã nhấn vào liên kết 'Change your password'")
    time.sleep(5)

    new_password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-password"))
    )
    new_password.send_keys("NewPassword123!")

    confirm_password = driver.find_element(By.ID, "input-confirm")
    confirm_password.send_keys("NewPassword123!")
    time.sleep(2)

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    continue_button.click()
    print("Đã nhấn vào nút 'Continue' để xác nhận thay đổi mật khẩu.")

    # Kiểm tra thông báo xác nhận thay đổi mật khẩu thành công
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        print("Thay đổi mật khẩu thành công:", success_message.text)
    except TimeoutException:
        print("Không thấy thông báo thành công. Có thể đã xảy ra lỗi khi thay đổi mật khẩu.")



def test_edit_account_information(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    # Đăng nhập vào tài khoản
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("nhungnhungnhung@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("NewPassword123!")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(5)

    # Nhấn vào liên kết "Edit your account information"
    edit_acount_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Modify your address book entries"))
    )
    edit_acount_link.click()
    print("Đã nhấn vào liên kết 'Modify your address book entries'.")
    time.sleep(5)

    # Chỉnh sửa thông tin cá nhân
    # Clear và nhập lại thông tin "First Name"
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name.clear()
    first_name.send_keys("nhung")

    # Clear và nhập lại thông tin "Last Name"
    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.clear()
    last_name.send_keys("thi tran")

    # Clear và nhập lại thông tin "Email"
    email = driver.find_element(By.ID, "input-email")
    email.clear()
    email.send_keys("nhungnhungnhung@gmail.com")

    # Nhấn nút "Continue" để lưu thay đổi
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    continue_button.click()
    print("Đã nhấn vào nút 'Continue' để xác nhận thay đổi thông tin tài khoản.")

    # Kiểm tra thông báo thành công
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        print("Thông tin tài khoản đã được cập nhật thành công:", success_message.text)
    except TimeoutException:
        print("Không thấy thông báo thành công. Có thể đã xảy ra lỗi khi cập nhật thông tin tài khoản.")


def test_add_new_address_book(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    # Đăng nhập vào tài khoản
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys(
        "nhungnhungnhung@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("NewPassword123!")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(5)

    # Truy cập vào sổ địa chỉ
    address_book_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Address Book"))
    )
    address_book_link.click()
    print("Đã nhấn vào liên kết 'Address Book'.")
    time.sleep(5)

    # Nhấn vào nút "New Address"
    new_address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, 'route=account/address.form') and text()='New Address']"))
    )
    new_address_button.click()
    print("Đã nhấn vào nút 'New Address' để thêm địa chỉ mới.")
    time.sleep(5)

    # Cập nhật các trường địa chỉ
    # Clear và nhập lại thông tin "First Name"
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name.clear()
    first_name.send_keys("tran")

    # Clear và nhập lại thông tin "Last Name"
    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.clear()
    last_name.send_keys("thi thi")

    # Clear và nhập lại thông tin "Address 1"
    address_1 = driver.find_element(By.ID, "input-address-1")
    address_1.clear()
    address_1.send_keys("123 New aaaaStreet")

    # Clear và nhập lại thông tin "City"
    city = driver.find_element(By.ID, "input-city")
    city.clear()
    city.send_keys("New C9ity")

    # Clear và nhập lại thông tin "Postcode"
    postcode = driver.find_element(By.ID, "input-postcode")
    postcode.clear()
    postcode.send_keys("1234")

    # Chọn "Vietnam" từ combobox Country
    country_dropdown = Select(driver.find_element(By.ID, "input-country"))
    country_dropdown.select_by_visible_text("Viet Nam")
    time.sleep(2)
    # Chọn "Ha Noi" từ combobox Region/State
    region_dropdown = Select(driver.find_element(By.ID, "input-zone"))
    region_dropdown.select_by_visible_text("Ho Chi Minh City")

    # Nhấn nút "Continue" để lưu thay đổi địa chỉ
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    continue_button.click()
    print("Đã nhấn vào nút 'Continue' để lưu thay đổi địa chỉ.")

    # Kiểm tra thông báo thành công
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        print("Cập nhật địa chỉ thành công:", success_message.text)
    except TimeoutException:
        print("Không thấy thông báo thành công. Có thể đã xảy ra lỗi khi cập nhật địa chỉ.")


def test_edit_address_book(driver):
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(5)

    # Đăng nhập vào tài khoản
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("nhungnhungnhung@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("NewPassword123!")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(5)

    # Truy cập vào sổ địa chỉ
    address_book_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Address Book"))
    )
    address_book_link.click()
    print("Đã nhấn vào liên kết 'Address Book'.")
    time.sleep(5)

    # Nhấn vào nút "Edit" để chỉnh sửa địa chỉ, sử dụng XPath selector
    edit_address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'route=account/address.form') and contains(@class, 'btn-primary')]"))
    )
    edit_address_button.click()
    print("Đã nhấn vào nút 'Edit' để chỉnh sửa địa chỉ.")
    time.sleep(5)

    # Cập nhật các trường địa chỉ
    # Clear và nhập lại thông tin "First Name"
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-firstname"))
    )
    first_name.clear()
    first_name.send_keys("nhung")

    # Clear và nhập lại thông tin "Last Name"
    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.clear()
    last_name.send_keys("thi tran")

    # Clear và nhập lại thông tin "Address 1"
    address_1 = driver.find_element(By.ID, "input-address-1")
    address_1.clear()
    address_1.send_keys("123 New Street")

    # Clear và nhập lại thông tin "City"
    city = driver.find_element(By.ID, "input-city")
    city.clear()
    city.send_keys("New City")

    # Clear và nhập lại thông tin "Postcode"
    postcode = driver.find_element(By.ID, "input-postcode")
    postcode.clear()
    postcode.send_keys("123456")

    # Chọn "Vietnam" từ combobox Country
    country_dropdown = Select(driver.find_element(By.ID, "input-country"))
    country_dropdown.select_by_visible_text("Viet Nam")
    time.sleep(2)
    # Chọn "Ha Noi" từ combobox Region/State
    region_dropdown = Select(driver.find_element(By.ID, "input-zone"))
    region_dropdown.select_by_visible_text("Ha Noi")

    # Nhấn nút "Continue" để lưu thay đổi địa chỉ
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    continue_button.click()
    print("Đã nhấn vào nút 'Continue' để lưu thay đổi địa chỉ.")

    # Kiểm tra thông báo thành công
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        print("Cập nhật địa chỉ thành công:", success_message.text)
    except TimeoutException:
        print("Không thấy thông báo thành công. Có thể đã xảy ra lỗi khi cập nhật địa chỉ.")
