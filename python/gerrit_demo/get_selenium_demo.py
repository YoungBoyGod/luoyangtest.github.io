import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Specify ChromeDriver path (replace with your actual path)
driver_path = "chromedriver.exe"

# Create a ChromeDriver service instance
chrome_service = Service(driver_path)

# Create Chrome WebDriver using the serviceEDIT.
driver = webdriver.Chrome(service=chrome_service)

# Open Google homepage
driver.get("http://127.0.0.1:8080/login/%2F")
driver.find_element(By.XPATH, '//*[@id="userlist"]/a').click()
time.sleep(2)
driver.get("http://127.0.0.1:8080/admin/repos/repo1,access")
time.sleep(2)

# 等待带有 editBtn 类名的元素出现，最多等待 10 秒
element = driver.execute_script(
    'document.querySelector("#pg-app").shadowRoot.querySelector("#app-element").shadowRoot.querySelector("main > gr-admin-view").shadowRoot.querySelector("div > gr-repo-access").shadowRoot.querySelector("#editBtn").click()')

# 使用 JavaScript 定位包含 Shadow DOM 的元素
element1 = driver.execute_script('return document.querySelector("#pg-app").shadowRoot.querySelector("#app-element").shadowRoot.querySelector("main > gr-admin-view").shadowRoot.querySelector("div > gr-repo-access").shadowRoot.querySelector("#loadedContent > gr-access-section:nth-child(4)").shadowRoot.querySelector("#mainContainer > div.sectionContent > gr-permission").shadowRoot.querySelector("#groupAutocomplete").shadowRoot.querySelector("#input").shadowRoot.querySelector("#input-4 > input");')

# 执行其他操作，例如输入文本到输入框
element1.send_keys("Administrator")
# Close the browser window
time.sleep(100)
driver.quit()
