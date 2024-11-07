

from conftest import *

def test_single_item_addition_to_cart(driver):
    # Mở trang chính của OpenCart
    driver.get("http://localhost/webopencart/index.php?route=common/home&language=en-gb")
    wait = WebDriverWait(driver, 2)

    try:
        # Tìm và nhấn nút "Add to Cart" của sản phẩm đầu tiên
        cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.row div:nth-child(2) button:nth-of-type(1)")
        ))
        driver.execute_script("arguments[0].scrollIntoView();", cart_button)
        cart_button.click()

        # Xác minh sự hiện diện của thông báo thành công
        success_alert = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
        )
        assert "iPhone" in success_alert.text, "Tên sản phẩm không xuất hiện trong thông báo thành công."

    except (TimeoutException, ElementClickInterceptedException):
        print("Có lỗi khi nhấn nút, thử tải lại trang và thử lại.")
        driver.refresh()
        cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.row div:nth-child(2) button:nth-of-type(1)")
        ))
        driver.execute_script("arguments[0].click();", cart_button)

        success_alert = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
        )
        assert "iPhone" in success_alert.text, "Tên sản phẩm không xuất hiện trong thông báo sau khi thử lại."


def test_add_same_product_twice(driver):
    # Điều hướng đến trang sản phẩm MacBook
    driver.get("http://localhost/webopencart/index.php?route=product/product&language=en-gb&product_id=43")
    wait = WebDriverWait(driver, 2)

    # Nhấn vào "Add to Cart" hai lần
    add_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_button.click()
    time.sleep(1)
    add_button.click()
    time.sleep(3)

    # Mở giỏ hàng
    cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header-cart button")))
    cart_icon.click()
    time.sleep(2)

    # Lấy tên và số lượng sản phẩm từ giỏ hàng
    items_in_cart = driver.find_elements(By.CSS_SELECTOR, "#header-cart .dropdown-menu .text-start > a")
    item_quantities = driver.find_elements(By.CSS_SELECTOR, "#header-cart .text-end:nth-child(3)")

    product_names = [item.text for item in items_in_cart]
    quantities = [int(quantity.text.replace("x", "").strip()) for quantity in item_quantities if quantity.text]

    # Xác minh kết quả
    assert product_names == ['MacBook'], "Tên sản phẩm trong giỏ hàng không đúng."
    assert quantities == [2], "Số lượng sản phẩm không khớp với mong đợi."


def test_add_two_different_products(driver):
    # Truy cập trang chính và thêm sản phẩm iPhone vào giỏ hàng
    driver.get("http://localhost/webopencart/index.php?route=common/home&language=en-gb")
    wait = WebDriverWait(driver, 2)

    iphone_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.row div:nth-child(2) button:nth-of-type(1)")
    ))
    driver.execute_script("arguments[0].scrollIntoView();", iphone_button)
    iphone_button.click()
    time.sleep(2)

    # Truy cập trang MacBook và thêm sản phẩm vào giỏ hàng
    driver.get("http://localhost/webopencart/index.php?route=product/product&language=en-gb&product_id=43")
    macbook_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    macbook_button.click()
    time.sleep(3)

    # Kiểm tra giỏ hàng để đảm bảo cả hai sản phẩm có mặt
    cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header-cart button")))
    cart_icon.click()
    time.sleep(2)

    cart_items = driver.find_elements(By.CSS_SELECTOR, "#header-cart .text-start > a")
    items_in_cart = [item.text for item in cart_items]
    expected_items = ["iPhone", "MacBook"]

    assert set(items_in_cart) == set(expected_items), "Danh sách sản phẩm trong giỏ hàng không đúng."
