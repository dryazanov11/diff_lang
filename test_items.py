import time 


link = "https://yandex.ru/"

def test_second (browser):
	browser.get (link)
	#time.sleep(30)
	buttons = browser.find_elements_by_css_selector ("button.btn.btn-lg.btn-primary.btn-add-to-basket")     
	assert len (buttons) == 1
	
	
