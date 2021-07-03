import watchdog.events
import watchdog.observers
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

options = webdriver.ChromeOptions()
options.headless =True
base='.\\upload\\'
arr=os.listdir(base)

def upload(k):
                image_url = k
                PATH = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver. Chrome(PATH,options=options)
                driver.get("http://127.0.0.1:8000/classification/")
                driver.find_element_by_name("imageFile").clear()
                driver.find_element_by_name("imageFile").send_keys(image_url)
                e=driver.find_element_by_name("submit")
                e.click()
                driver.quit()
            
def rem(url):
    image_url = url
    os.remove(image_url)


class Handler(watchdog.events.PatternMatchingEventHandler):
	def __init__(self):
		# Set the patterns for PatternMatchingEventHandler
		watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.jpg'],
                                                                     ignore_directories=True, case_sensitive=False)

	def on_created(self, event):
		print("Watchdog received created event - % s." % event.src_path)
		upload(event.src_path)


	def on_modified(self, event):
		print("Watchdog received modified event - % s." % event.src_path)
		rem(event.src_path)


if __name__ == "__main__":
	src_path = r"E:\pyfiles\selenium tut\upload"
	event_handler = Handler()
	observer = watchdog.observers.Observer()
	observer.schedule(event_handler, path=src_path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
