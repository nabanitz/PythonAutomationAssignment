from selenium import webdriver
from POMAmazonSearch.AmazonHomePage import AmazonHomePage
from POMAmazonSearch.LoginPage import LoginPage
from POMAmazonSearch.ProductDetailPage import ProductDetailsPage
from POMAmazonSearch.SearchResultPage import SearchResultsPage

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    # Navigate to Amazon
    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    # Amazon Home Page
    home_page = AmazonHomePage(driver)
    home_page.search_product("iphone 13")

    # Search Results Page
    search_results = SearchResultsPage(driver)
    product_titles = search_results.get_product_titles()
    new_product_list = [title for title in product_titles if "iPhone 13" in title.text]

    print("Total Results of Product Name =>", [title.text for title in product_titles])
    print("Total Results of iPhone 13 =>", len(new_product_list))

    if len(new_product_list) > 4:
        print("The 4th iPhone title is ->", new_product_list[3].text)
        search_results.click_product_by_index(3)
    else:
        print("There is less than 4 items available.")

    # Switch to new tab
    driver.switch_to.window(driver.window_handles[1])

    # Product Details Page
    product_details = ProductDetailsPage(driver)
    product_details.click_buy_now()

    # Login Page
    login_page = LoginPage(driver)
    login_page.login("8617043881", "12345@p")

    # Handle error message (if any)
    error_message = login_page.get_error_message()
    print("Login Error Message:", error_message)

except Exception as e:
    print("An error occurred during the test:", str(e))

finally:
    print("Automation completed.")
    driver.quit()
