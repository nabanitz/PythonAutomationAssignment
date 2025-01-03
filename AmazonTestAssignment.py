import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


productName =[]
newProductList = []

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("iphone 13")
    search_box.send_keys(Keys.ENTER)
    totalTitles = driver.find_elements(By.CSS_SELECTOR, ".s-title-instructions-style .a-text-normal")
    for title in totalTitles:
        if "iPhone 13" in title.text:
            newProductList.append(title)
            productName.append(title.text)

    print("Total Results of Product Name => ", productName)
    print("Total Results of iphone 13 => ", len(newProductList))
    if len(newProductList) > 4:
        print("The 4th iphone title is -> ", newProductList[3].text)
        newProductList[3].click()
    else:
        print("There is less than 4 item available")
        driver.quit()
        exit()
    try:
        driver.switch_to.window(driver.window_handles[1])
    except IndexError:
            print("Unable to open new tab")
            driver.quit()
            exit()
    try:
        driver.find_element(By.ID, "buy-now-button").click()

    except Exception as e:
            print("Failed to find or click the 'Buy Now' button. Error:", str(e))
            driver.quit()
            exit()
    try:
        driver.find_element(By.ID, "ap_email").send_keys("8617043881")
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("12345@p")
        driver.find_element(By.ID, "signInSubmit").click()
        textMsg = driver.find_element(By.CLASS_NAME,"a-list-item").text
    except AssertionError as ae:
        print("Assertion failed:", str(ae))
    except Exception as e:
        print("An error occurred during the login process:", str(e))

finally:
    print("Automation completed.")
    time.sleep(15)
    driver.quit()