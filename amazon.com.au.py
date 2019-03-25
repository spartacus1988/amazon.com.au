from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime



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
	#browser.implicitly_wait(0.1)

	elm = browser.find_element_by_css_selector('.first-carousel > .feed-right')
	elm.click()

	#browser.implicitly_wait(0.1)

	#elm = browser.find_element_by_css_selector(".feed-carousel-card:nth-child(9) .product-image")
	elm = browser.find_element_by_xpath("//img[@alt='Pet Supplies']")
	browser.execute_script("arguments[0].click();", elm)
	#elm.click()

	#browser.implicitly_wait(0.1)

	elm = browser.find_element_by_xpath("//div[@id='leftNav']/ul/ul/div/li[2]/span/a/span")
	browser.execute_script("arguments[0].click();", elm)

	browser.implicitly_wait(0.1)

	elm = browser.find_element_by_xpath("//div[@id='leftNav']/ul/ul/div/li[4]/span/a/span")
	browser.execute_script("arguments[0].click();", elm)

	#browser.implicitly_wait(0.1)

	elm = browser.find_element_by_xpath("//div[@id='anonCarousel1']/ol/li/div/a/span")
	browser.execute_script("arguments[0].click();", elm)

	#browser.implicitly_wait(0.1)

	elm = browser.find_element_by_xpath("//div[@id='detail_bullets_id']/table/tbody/tr/td/div[2]/ul/li[3]")
	print(elm.text)
	ASIN = elm.text
	ASIN = ASIN.split(':')
	ASIN = ASIN[1] 
	print(ASIN)

	elm = browser.find_element_by_xpath("//div[@id='detail_bullets_id']/table/tbody/tr/td/div[2]/ul/li[4]")
	print(elm.text)
	Date = elm.text
	Date = Date.split(':')
	Date = Date[1] 
	print(Date)
	Date = Date.split()
	d = Date[0]
	B = Date[1]
	Y = Date[2]
	string = str(d +','+ B+','+ Y)
	print(string)
	Date = datetime.strptime(string, '%d,%B,%Y')
	print(Date.strftime('%Y-%m-%d'))


	elm = browser.find_element_by_id("productTitle")
	print(elm.text)



	browser.close()

	try:
		print("try")
	except:
		print("was_get_request_except")
	#return self.exception_request(browser)
