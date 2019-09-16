import time 


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button (browser):
	browser.get (link)
	#time.sleep(30)
	buttons = browser.find_elements_by_css_selector ("button.btn.btn-lg.btn-primary.btn-add-to-basket")     
	assert len (buttons) == 1
	
	
