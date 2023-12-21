from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self, full_name, email, current_address, permanent_address):
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_clickable(self.locators.SUBMIT).click()



    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.FULL_NAME).text
        email = self.element_is_present(self.locators.EMAIL).text
        current_address = self.element_is_present(self.locators.CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address