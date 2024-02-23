from selenium import webdriver as WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import BrowserController

formatProductLink = ("https://www.etsy.com/listing/{product_id}/black-and-beige-set-of-3-prints-henri?click_key"
                     "=c710384ecc86679044eb9780719f001c8e2654f3%3A1446293575&click_sum=19d4d1fa&ref"
                     "=shop_home_active_1&crt=1")


def setUpChromeWebDriver():
    driver_manager = ChromeDriverManager()
    options = Options()
    service = Service(driver_manager.install())
    WebDriver.ChromeService = driver_manager.install()
    options.add_experimental_option("detach", True)
    return WebDriver.Chrome(service=service, options=options)


def openProductLink(product_id: str):
    print(formatProductLink.format(product_id=product_id))
    driver.get(formatProductLink.format(product_id=product_id))


def findProductName():
    elementProductName = driver.find_element(by=By.CSS_SELECTOR, value="#listing-page-cart > div.wt-mb-xs-1 > h1")
    return elementProductName.text


def findExploreRelatedSearches():
    elements = driver.find_elements(by=By.CSS_SELECTOR, value="#content > div.content-wrap.listing-page-content > "
                                                              "div.wt-body-max-width.wt-mb-xs-6.wt-pl-md-4.wt-pr-md-4"
                                                              ".wt-pl-lg-5.wt-pr-lg-5 > div.recs-appears-logger > div "
                                                              "> "
                                                              "div.tags-section-container.tag-cards-section-container"
                                                              "-with-images > ul li")
    for element in elements:
        e = element.find_element(by=By.CSS_SELECTOR, value="a > h3")
        print(e.text)


driver = None

if __name__ == '__main__':
    driver = setUpChromeWebDriver()
    openProductLink(product_id="1436406443")
    productName = findProductName()
    print(f"Product Name: {productName}")
    findExploreRelatedSearches()
    driver.quit()
