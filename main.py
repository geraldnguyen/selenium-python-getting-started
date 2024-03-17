from selenium import webdriver
from selenium.webdriver.common.by import By


def tc1_get_python_org_title():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.python.org")

        print(driver.title)
    finally:
        driver.quit()


# tc1_get_python_org_title()


def tc2_search_getting_started():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.python.org")

        search_input_field = driver.find_element(By.ID, "id-search-field")
        search_input_field.clear()
        search_input_field.send_keys("getting started in Python")

        search_go_button = driver.find_element(By.ID, "submit")
        search_go_button.click()

        print("current url: " + driver.current_url)

        results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
        print(f"number of results: {len(results)}")

    finally:
        driver.quit()


tc2_search_getting_started()
