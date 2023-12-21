import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
from logs.logger import logger
from datetime import datetime

@pytest.fixture(scope='function')
def driver(request):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    logger.info(f'########## Test Case: {test_name} ##########')
    driver = webdriver.Firefox()
    logger.info('Opened Firefox Browser')
    driver.maximize_window()
    logger.info('Launched the DemoQA')
    yield driver
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    driver.save_screenshot(fr".\evidence\{test_name}_{timestamp}.png")
    logger.info('ScreenShot is created')
    driver.quit()
    logger.info('Closed the browser')