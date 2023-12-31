from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

#created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS= (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')   #span[class="rct-checkbox"] #span[class="rct-title"]
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")



class RadioButtonPageLocators:

    YesButton = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    ImpressiveButton = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NoButton = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    #add person form
    ADD_BUTTON = (By.CSS_SELECTOR,'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR,'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR,'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR,'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR,'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR,'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR,'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR,'button[id="submit"]')

    #tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR,'div[class="rt-tr-group"]')