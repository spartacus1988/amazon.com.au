from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait



class AmazonSpider:
	
	def init_driver(file_path):
		options = Options()
		#options.add_argument("--headless")
		browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)	
		browser.wait = WebDriverWait(browser, 10)
		return(browser)




if __name__ == "__main__":

	AmazonSpider = AmazonSpider()
	browser = AmazonSpider.init_driver()


	url = 'https://www.amazon.com.au/'

	browser.get(url)
	browser.implicitly_wait(1)

	#elm = browser.find_element_by_css_selector('.first-carousel > .feed-right > .gw-icon')
	elm = browser.find_element_by_css_selector('.first-carousel > .feed-right')
	elm.click()
	#browser.execute_script("arguments[0].click();", elm)

	#elm.click()
	#print(elm.get_attribute("class"))

	#browser.close()

	try:
		print("try")
		#print("get_one_request_first_try")
		#elm = browser.find_element_by_css_selector('.first-carousel > .feed-right > .gw-icon').click()
		#elm = browser.find_element_by_id('home-details-module-zone')
	except:
		print("get_one_request_first_except")
	#return self.exception_request(browser)


	#update_csv_cell(ZillowSpider, browser)