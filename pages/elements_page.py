from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self, full_name, email, current_address, permanent_address):
        self.element_is_present(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_present(self.locators.EMAIL).send_keys(email)
        self.element_is_present(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_present(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_clickable(self.locators.SUBMIT).click()

        # Добавляем задержку на несколько секунд
        sleep(5)

        # Возвращаем данные после заполнения
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.FULL_NAME).get_attribute("value")
        email = self.element_is_present(self.locators.EMAIL).get_attribute("value")
        current_address = self.element_is_present(self.locators.CURRENT_ADDRESS).get_attribute("value")
        permanent_address = self.element_is_present(self.locators.PERMANENT_ADDRESS).get_attribute("value")

        return full_name, email, current_address, permanent_address
