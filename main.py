import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_tc1_get_python_org_title(self):
        driver = self.driver
        driver.get("https://www.python.org")

        print(driver.title)
        self.assertEqual("Welcome to Python.org", driver.title)


    def test_tc2_search_getting_started(self):
        driver = self.driver

        driver.get("https://www.python.org")

        search_input_field = driver.find_element(By.ID, "id-search-field")
        search_input_field.clear()
        search_input_field.send_keys("getting started in Python")

        search_go_button = driver.find_element(By.ID, "submit")
        search_go_button.click()

        print("current url: " + driver.current_url)
        self.assertEqual("https://www.python.org/search/?q=getting+started+in+Python&submit=", driver.current_url)

        results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
        print(f"number of results: {len(results)}")
        self.assertGreater(len(results), 0)

if __name__ == '__main__':
    unittest.main()

