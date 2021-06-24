from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
# option.add_argument("--headless")
# option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path='<local chrome driver location>', options=option)

# Google Form Addresss
browser.get("https://docs.google.com/forms/d/e/<form_ID>/viewform")


# Find the elements that you want to use (Textboxes, checkboxes, radio buttons etc.) 
# Each one of these elements are grouped according to their type with a common class value. (Ctrl+Shift+c)
# find_elements_by_class_name returns a list of all elements with that class
# find_element_by_class_name or find_element_by_id 
text_boxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radio_buttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelText")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submit_button = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")


text_boxes[0].send_keys("string")
text_boxes[1].send_keys("string")
radio_buttons[0].click()
radio_buttons[2].click()
text_boxes[3].send_keys("string")
# submit_button[0].click()
# submit_button.click()		# if only one submit button 

# browser.close()
