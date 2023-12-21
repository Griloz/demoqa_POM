import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields('Greg', 'griloz@gmail.com', 'Charlotte', 'NC')
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_cur_address)
            print(output_per_address)
