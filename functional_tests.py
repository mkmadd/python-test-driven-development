from selenium import webdriver
from xvfbwrapper import Xvfb    # added for headless selenium operation

# added for headless selenium operation
vdisplay = Xvfb()
vdisplay.start()

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title
browser.quit()

# added for headless selenium operation
vdisplay.stop()
