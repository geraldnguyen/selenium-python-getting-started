from selenium import webdriver


def tc1_get_python_org_title():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.python.org")

        print(driver.title)
    finally:
        driver.quit()

# tc1_get_python_org_title()


