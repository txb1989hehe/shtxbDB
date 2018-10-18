from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class xl_news_spider():
	def __init__(self):
		self.start_url = 'https://news.sina.com.cn/roll/#pageid=153&lid=2509&k=&num=50&page=1'
		chrome_option = Options()
		chrome_option.add_argument('--headless')
		chrome_option.add_argument('--disable-gpu')
		self.driver = webdriver.Chrome(chrome_options=chrome_option)
		self.driver.set_page_load_timeout(30)
		self.start_request()

	def close(self):
		print('spider closed.')
		print('=' * 50)
		self.driver.close()

	def start_request(self):
		try:
			self.driver.get(self.start_url)  # 獲取頁面源碼
			self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 網頁進度條拉到底
		except Exception as e:
			print('time out~[%s]' %e)
			self.driver.execute_script('window.stop()')  # 關閉網頁
		time.sleep(3)
		self.driver.save_screenshot('main.png')
		print('---------------------實時新聞----------------------')
		while True:
			with open('news.txt', 'w') as f:
				items = {}
				self.driver.find_element_by_id('reloadButton').click()
				news = self.driver.find_element_by_xpath('//*[@id="d_list"]/ul[1]/li[1]/span[2]/a')
				items['name'] = news.text
				items['link'] = news.get_attribute('href')
				f.write(str(items) + '\n')
				print(items)
			time.sleep(50)  # 50秒刷新一次
		# self.close()

if __name__ == '__main__':
	xl_news_spider()






