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

	elm = browser.find_element_by_css_selector('.first-carousel > .feed-right')
	elm.click()

	browser.implicitly_wait(1)

	#elm = browser.find_element_by_css_selector(".feed-carousel-card:nth-child(9) .product-image")
	elm = browser.find_element_by_xpath("//img[@alt='Pet Supplies']")
	browser.execute_script("arguments[0].click();", elm)
	#elm.click()

	browser.implicitly_wait(1)

	elm = browser.find_element_by_xpath("//div[@id='leftNav']/ul/ul/div/li[2]/span/a/span")
	browser.execute_script("arguments[0].click();", elm)

	browser.implicitly_wait(1)

	elm = browser.find_element_by_xpath("//div[@id='leftNav']/ul/ul/div/li[4]/span/a/span")
	browser.execute_script("arguments[0].click();", elm)

	browser.implicitly_wait(1)

	elm = browser.find_element_by_xpath("//div[@id='anonCarousel1']/ol/li/div/a/span")
	browser.execute_script("arguments[0].click();", elm)





	browser.close()

	try:
		print("try")
	except:
		print("was_get_request_except")
	#return self.exception_request(browser)
