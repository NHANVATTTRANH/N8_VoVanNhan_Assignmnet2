#DONE
import time

from conftest import *

def test_checkout_as_guest(driver): # Test function for placing an order as a guest
    # Navigate to the product page
    driver.get("https://demo-opencart.com/index.php?route=product/product&language=en-gb&product_id=43")  # Open the iPhone product page
    wait = WebDriverWait(driver, 2)
    time.sleep(5)

    # Verify the visibility of the Add to Cart button and click it
    add_to_cart_button = wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    time.sleep(5)
    add_to_cart_button.click()
    time.sleep(10)

    # Go to the cart page
    driver.get("https://demo-opencart.com/index.php?route=checkout/cart&language=en-gb") # Redirect to the shopping cart
    time.sleep(5)

    # Click the Checkout button to proceed with the purchase
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))).click()
    time.sleep(10)

    # Select the guest account option
    guest_account_option = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-guest")) # Choose the guest account option
    )
    guest_account_option.click()
    time.sleep(5)

    # Fill in personal details and shipping address
    first_name_field = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    first_name_field.send_keys("Nhan")

    last_name_field = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    last_name_field.send_keys("Vo")

    email_field = driver.find_element(By.CSS_SELECTOR, "#input-email")
    email_field.send_keys("nhngngnhung@gmail.com")

    address_field = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-1")
    address_field.send_keys("SGU, An Duong Vuong, Q5, TP HCM")

    city_field = driver.find_element(By.CSS_SELECTOR, "#input-shipping-city")
    city_field.send_keys("Ho Chi Minh City")

    postal_code_field = driver.find_element(By.CSS_SELECTOR, "#input-shipping-postcode")
    postal_code_field.clear()
    postal_code_field.send_keys("00700")

    country_selector = driver.find_element(By.CSS_SELECTOR, "#input-shipping-country")
    country_dropdown = Select(country_selector)
    country_dropdown.select_by_visible_text("Viet Nam")

    region_selector = driver.find_element(By.CSS_SELECTOR, "#input-shipping-zone")
    region_dropdown = Select(region_selector)
    region_dropdown.select_by_visible_text("Ho Chi Minh City")

    time.sleep(5)

    # Proceed to confirm the details by clicking the Continue button
    continue_button = driver.find_element(By.CSS_SELECTOR, "#button-register")
    continue_button.click()
    time.sleep(5)

    # Scroll to shipping methods section
    driver.execute_script("arguments[0].scrollIntoView(false);", driver.find_element(By.CSS_SELECTOR, "#button-shipping-methods"))
    time.sleep(4)

    # Select shipping method
    shipping_method_button = driver.find_element(By.CSS_SELECTOR, "#button-shipping-methods")
    shipping_method_button.click()
    time.sleep(5)

    flat_rate_method = driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat")
    flat_rate_method.click()
    time.sleep(5)

    # Click continue to confirm shipping method
    continue_shipping = driver.find_element(By.CSS_SELECTOR, "#button-shipping-method")
    continue_shipping.click()
    time.sleep(5)

    # Select payment method and confirm order
    payment_method_button = driver.find_element(By.CSS_SELECTOR, "#button-payment-methods")
    payment_method_button.click()
    time.sleep(5)

    cash_on_delivery_method = driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod")
    cash_on_delivery_method.click()
    time.sleep(5)

    continue_payment = driver.find_element(By.CSS_SELECTOR, "#button-payment-method")
    continue_payment.click()
    time.sleep(5)

    # Scroll to confirm order button and click it
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.CSS_SELECTOR, "#button-confirm"))
    time.sleep(5)

    confirm_button = driver.find_element(By.CSS_SELECTOR, "#button-confirm")
    confirm_button.click()
    time.sleep(5)

    # Check the confirmation message on the new page
    confirmation_message = driver.find_element(By.CSS_SELECTOR, "#content > h1")
    actual_message = confirmation_message.text

    expected_message = "Your order has been placed!"
    assert expected_message == actual_message, "The order was not successfully placed" # Check for successful order placement

def test_order_with_existing_address(driver): # Test case for placing an order with an existing address in the account
    # Log into the account
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(10)

    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email")))
    email_field.send_keys("vonhan6000@gmail.com")
    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("12345678WW@")
    time.sleep(5)

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()

    # Navigate to the iPhone product page
    driver.get("https://demo-opencart.com/index.php?route=product/product&language=en-gb&product_id=43")
    wait = WebDriverWait(driver, 30)
    time.sleep(10)

    # Add the product to the cart
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(10)

    # Go to the shopping cart
    driver.get("https://demo-opencart.com/index.php?route=checkout/cart&language=en-gb")
    time.sleep(10)

    # Proceed to checkout
    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
    checkout_button.click()
    time.sleep(10)

    # Choose a saved shipping address
    shipping_address_dropdown = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "input-shipping-address")))
    address_select = Select(shipping_address_dropdown)
    address_select.select_by_visible_text("nhan vo, 10 an duong vuong hung vuong, q5 , tp hcm, hcm city, Ho Chi Minh City, Viet Nam")
    time.sleep(10)

    # Choose shipping and payment methods, and confirm the order
    shipping_method_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-shipping-methods")))
    shipping_method_button.click()
    time.sleep(10)

    flat_rate_method = driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat")
    flat_rate_method.click()
    time.sleep(10)

    continue_shipping_button = driver.find_element(By.CSS_SELECTOR, "#button-shipping-method")
    continue_shipping_button.click()
    time.sleep(10)

    payment_method_button = driver.find_element(By.CSS_SELECTOR, "#button-payment-methods")
    payment_method_button.click()
    time.sleep(10)

    cash_on_delivery_method = driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod")
    cash_on_delivery_method.click()
    time.sleep(10)

    continue_payment_button = driver.find_element(By.CSS_SELECTOR, "#button-payment-method")
    continue_payment_button.click()
    time.sleep(10)

    # Confirm the order
    confirm_order_button = driver.find_element(By.CSS_SELECTOR, "#button-confirm")
    confirm_order_button.click()
    time.sleep(10)

    # Verify the success notification
    notification = driver.find_element(By.CSS_SELECTOR, "#content > h1")
    actual_notification = notification.text
    expected_notification = "Your order has been placed!"
    assert actual_notification == expected_notification, "Order was not successfully placed"

def test_checkout_with_newAddress(driver):
    # Log into the account
    driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
    time.sleep(10)

    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email")))
    email_field.send_keys("vonhan6000@gmail.com")
    password_field = driver.find_element(By.ID, "input-password")
    password_field.send_keys("12345678WW@")
    time.sleep(5)
    
    driver.get("https://demo-opencart.com/index.php?route=product/product&language=en-gb&product_id=43")   # Truy cập vào trang sản phẩm iPhone
    wait = WebDriverWait(driver, 5)

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart"))) # Chờ nút "Add to Cart" và nhấn vào
    add_to_cart_button.click()
    time.sleep(5)  

    driver.get("https://demo-opencart.com/index.php?route=checkout/cart&language=en-gb") # Truy cập vào giỏ hàng
    time.sleep(20)  

    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))) # Chờ nút "Checkout" và nhấn vào
    checkout_button.click()
    time.sleep(5)  

    # Chọn hộp kiểm "New Address" nếu chưa được chọn
    shipping_checkbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "input-shipping-new"))
    )
    if not shipping_checkbox.is_selected():
        shipping_checkbox.click()  
    time.sleep(10) 

    input_first_name = driver.find_element(By.CSS_SELECTOR, "#input-shipping-firstname")
    input_first_name.send_keys("nhung")
    time.sleep(10)

    input_last_name = driver.find_element(By.CSS_SELECTOR, "#input-shipping-lastname")
    input_last_name.send_keys("tran")
    time.sleep(10)

    input_address1 = driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-1")
    input_address1.send_keys("02 tran binh trong, p12, q5,tphcm")
    time.sleep(10)



    input_city = driver.find_element(By.CSS_SELECTOR, "#input-shipping-city")
    input_city.send_keys("Ho Chi Minh City")
    time.sleep(10)

    input_post_code = driver.find_element(By.CSS_SELECTOR, "#input-shipping-postcode")
    input_post_code.clear()
    input_post_code.send_keys("00700")
    time.sleep(10)

    # Chọn quốc gia và vùng miền
    input_country = driver.find_element(By.CSS_SELECTOR, "#input-shipping-country")
    selection_country = Select(input_country)
    selection_country.select_by_visible_text("Viet Nam")
    time.sleep(10)

    input_region = driver.find_element(By.CSS_SELECTOR, "#input-shipping-zone")
    selection_region = Select(input_region)
    selection_region.select_by_visible_text("Ho Chi Minh City")
    time.sleep(10)

    # Xác nhận thông tin địa chỉ và tiếp tục đặt hàng
    continue_btn = driver.find_element(By.CSS_SELECTOR, "#button-shipping-address")
    continue_btn.click()
    time.sleep(10)

    #Chọn phương thức thanh toán 
    shipping_method = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-shipping-methods"))
    )
    shipping_method.click()
    time.sleep(10)

    method_flat = driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat")
    method_flat.click()
    time.sleep(10)

    continue_1 = driver.find_element(By.CSS_SELECTOR, "#button-shipping-method")
    continue_1.click()
    time.sleep(10)

    payment_method = driver.find_element(By.CSS_SELECTOR, "#button-payment-methods")
    payment_method.click()
    time.sleep(10)

    cash_method = driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod")
    cash_method.click()
    time.sleep(10)

    continue_2 = driver.find_element(By.CSS_SELECTOR, "#button-payment-method")
    continue_2.click()
    time.sleep(10)

    confirm_order = driver.find_element(By.CSS_SELECTOR, "#button-confirm")
    confirm_order.click()
    time.sleep(5)

    # Kiểm tra thông báo đặt hàng thành công
    notification = driver.find_element(By.CSS_SELECTOR, "#content > h1")
    notification_actual = notification.text
    notification_expected = "Your order has been placed!"
    assert notification_expected == notification_actual, "Đơn hàng không được đặt thành công"


