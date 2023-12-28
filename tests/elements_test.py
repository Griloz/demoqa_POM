from selenium.webdriver.firefox.webdriver import WebDriver
from generator import generated_person
from pages.elements_page import CheckBoxPage, TextBoxPage
from data import Person
from generator.generator import generated_person

class TestTextBox:
    def test_text_box(self, driver):
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
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()

