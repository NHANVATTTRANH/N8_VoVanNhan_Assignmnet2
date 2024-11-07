#DONE

from conftest import *

@pytest.fixture(autouse=True)
def setup(driver):
    # Navigate to the homepage of the OpenCart demo site
    driver.get('https://demo-opencart.com/index.php?route=common/home&language=en-gb')
    wait = WebDriverWait(driver, 10)
    return driver, wait

def test_Random_Click_onbroad(setup):
    driver, wait = setup

    # Open the "Desktops" menu
    desktopsMenu = driver.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle[href*="category"]')
    desktopsMenu.click()
    time.sleep(5)  # Wait for dropdown to appear

    # Select "Mac" from the dropdown menu
    macSubcategory = driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href*="category&language=en-gb&path=20_27"]')
    macSubcategory.click()
    time.sleep(5)  # Wait for the page to load

    # Print current URL to verify navigation
    print("Current URL:", driver.current_url)

    # Verify the page title contains the word "Mac"
    assert 'Mac' in driver.title, "Failed to navigate to the 'Mac' category!"

def test_show_All_Desktops(setup):
    driver, wait = setup

    # Open the "Desktops" menu and then click "Show All Desktops"
    driver.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle[href*="category"]').click()
    time.sleep(5)  # Wait for dropdown
    showAllLink = driver.find_element(By.CSS_SELECTOR, 'a.see-all[href*="category"]')
    showAllLink.click()
    time.sleep(5)  # Wait for page to load

    # Print current URL to verify navigation
    print("Current URL:", driver.current_url)

    # Verify the page title contains the word "Desktops"
    assert 'Desktops' in driver.title, "Failed to navigate to the 'Desktops' page!"

def test_Menu_Navigation(setup):
    driver, wait = setup

    # Open the "Desktops" menu
    desktopsMenu = driver.find_element(By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle[href*="category"]')
    desktopsMenu.click()
    time.sleep(5)  # Wait for dropdown to appear

    # List of menu items with their sub-items
    menuItems = [
        {"name": "Desktops", "subItems": ["PC (0)", "Mac (1)"]},
        {"name": "Laptops & Notebooks", "subItems": ["Macs (0)", "Windows (0)"]},
        {"name": "Components", "subItems": ["Mice and Trackballs (0)", "Monitors (2)", "Printers (0)", "Scanners (0)", "Web Cameras (0)"]},
        {"name": "MP3 Players", "subItems": ["test 11 (0)", "test 12 (0)", "test 15 (0)"]}
    ]

    # Loop through each main menu item
    for item in menuItems:
        # Hover over the main menu item
        menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, item["name"])))
        ActionChains(driver).move_to_element(menu).perform()
        wait.until(EC.visibility_of(menu))  # Ensure the menu is visible
        time.sleep(2)  # Wait for the menu to fully open

        # Loop through each sub-item and click it
        for subItem in item["subItems"]:
            # Wait for the sub-item to be visible
            subMenu = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, subItem)))
            time.sleep(2)  # Wait for sub-item visibility

            # Ensure the sub-item is clickable before clicking
            if subMenu.is_displayed() and subMenu.is_enabled():
                subMenu.click()
                time.sleep(5)  # Wait for the page to load after the click

                # Verify that the page title contains the expected sub-item name
                expectedTitle = subItem.split(" ")[0]  # Get the category name (e.g., "PC", "Mac")
                assert expectedTitle in driver.title, f"Expected page title to include '{expectedTitle}' but got '{driver.title}'"

                # Go back to the previous page
                driver.back()
                time.sleep(2)  # Wait for the page to load after navigating back

                # Re-hover over the main menu item to reopen the dropdown
                menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, item["name"])))
                ActionChains(driver).move_to_element(menu).perform()

