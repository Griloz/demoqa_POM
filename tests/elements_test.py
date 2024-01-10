import random
from venv import logger
from selenium.webdriver.firefox.webdriver import WebDriver
from generator import generated_person
from pages.elements_page import CheckBoxPage, RadioButtonPage, TextBoxPage, WebTablePage
from data import Person
from time import sleep
from generator.generator import generated_person

class TestTextBox:
    def test_text_box(self, driver: WebDriver):
        # Генерируем данные для заполнения полей
        person_info = next(generated_person())

        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()

        # Передаем сгенерированные данные в метод fill_all_fields
        input_data = text_box_page.fill_all_fields(
            person_info.full_name,
            person_info.email,
            person_info.current_address,
            person_info.permanent_address
        )

        # Проверяем, что форма заполнена корректно, используя данные, возвращенные из fill_all_fields
        output_data = text_box_page.check_filled_form()

        # Теперь используйте assert для сравнения
        assert input_data == output_data


class TestCheckBox:
    def test_check_box(self, driver: WebDriver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        print(input_checkbox)
        print(output_result)
        assert input_checkbox == output_result, "checkboxes have't been selected"


class TestRadioButton:
    def test_radio_button(self, driver: WebDriver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()

        assert output_yes == 'Yes', "'Yes' have not been selected"
        assert output_impressive == 'Impressive', "'Impressive' have not been selected"
        assert output_no == 'No', "'No' have not been selected"


class TestWebTable:
    def test_web_table_add_person(self, driver: WebDriver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()

        logger.info(f"New added {new_person}")
        logger.info(f"Result on table: {table_result}")
        # last_non_empty_result = next((result for result in reversed(table_result) if any(cell.strip() for cell in result)), None)
        # logger.info(f"Result on table: {last_non_empty_result}")
        assert new_person in table_result
        sleep(3)


    def test_web_table_serch_person(self, driver: WebDriver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0,5)]
        web_table_page.serch_some_person(key_word)
        table_result = web_table_page.check_serch_person(key_word)

        logger.info(f"Key Word: {key_word}")
        logger.info(f"Result: {table_result}")
        assert key_word in table_result, "Person wasn't found"
