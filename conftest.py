﻿import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException 

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default=None,
                     help="Choose language: es, en or ru")
					 
					 
@pytest.fixture(scope="function")
def browser(request):	
	user_language = request.config.getoption ("language")
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
	browser = webdriver.Chrome(options=options)
	browser.implicitly_wait(5)
	yield browser
	browser.quit()

	
	
	
	
	