import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_correct_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == success_message, f"Expected '{product_name}' in message, but got '{success_message}'"

    def should_be_correct_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Expected basket total '{product_price}', but got '{basket_total}'"