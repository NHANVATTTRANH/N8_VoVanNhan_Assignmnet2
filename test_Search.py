#DONE
from conftest import *

def test_search_with_valid_keyword(driver):
    keyword = "Macbook"
    search_results = perform_search(driver, keyword)
    time.sleep(5)
    assert len(search_results) > 0, "No products matched the search criteria."

def test_search_with_non_existent_keyword(driver):
    keyword = "2con cua giận mẹ"
    search_results = perform_search(driver, keyword)
    time.sleep(5)
    assert len(search_results) == 0, f"Search unexpectedly returned results for '{keyword}'!"

def test_search_with_blank_input(driver):
    keyword = ""
    search_results = perform_search(driver, keyword)
    time.sleep(5)
    assert len(search_results) == 0, f"Expected no results for an empty search, but got {len(search_results)} results."
    print("Blank search test passed: No products found.")

def test_search_with_special_symbols(driver):
    keyword = "!!@@mac!"
    search_results = perform_search(driver, keyword)
    time.sleep(5)
    assert len(search_results) == 0, f"Unexpected results for special character search '{keyword}', found {len(search_results)}."
    print("Special character search test passed: No products found.")

def test_search_with_extra_whitespace(driver):
    keyword = " " *50 + " mac"
    search_results = perform_search(driver, keyword)
    time.sleep(10)
    assert len(search_results) > 0, f"Expected results for '{keyword.strip()}', but found none."
    print(f"Whitespace-handling search test for '{keyword.strip()}' passed: Products found.")

def test_search_with_leading_special_character(driver):
    keyword = "!mac"
    search_results = perform_search(driver, keyword)
    time.sleep(5)
    assert len(search_results) == 0, f"Search returned results for '{keyword}', which was unexpected."
    print(f"Leading special character search test for '{keyword}' passed: No products found.")

def test_search_with_excessive_length(driver):
    keyword = "phone" * 50
    search_results = perform_search(driver, keyword)
    time.sleep(5)
    assert len(search_results) == 0, f"Search returned results for excessively long keyword '{keyword}', which was unexpected."
    print(f"Excessive length search test for '{keyword}' passed: No products found.")

    page_width = driver.execute_script("return document.body.scrollWidth;")
    viewport_width = driver.execute_script("return window.innerWidth;")
    assert page_width <= viewport_width, "Layout issue: Page width exceeds viewport width, causing horizontal scroll."
    print("Layout stability test passed: No horizontal scrolling detected.")

def perform_search(driver, query):
    driver.get("https://demo-opencart.com/index.php?route=common/home&language=en-gb")
    time.sleep(5)

    try:
        search_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "search")))
        search_box.clear()
        search_box.send_keys(query + Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "content")))

        products = driver.find_elements(By.XPATH, "//div[@id='content']//div[@class='product-thumb']")
        product_data = []

        if not products:
            print("No products were found for this search.")
            return product_data

        for product in products:
            name = product.find_element(By.XPATH, ".//h4/a").text
            price = product.find_element(By.XPATH, ".//span[@class='price-new']").text
            link = product.find_element(By.XPATH, ".//h4/a").get_attribute('href')

            product_data.append({
                "Name": name,
                "Price": price,
                "Link": link
            })

            print(f"Product: {name}")
            print(f"Price: {price}")
            print(f"link: {link}")
            print("~~~" * 10)

        return product_data

    except Exception as e:
        print(f"An error occurred while searching: {e}")
        return []
