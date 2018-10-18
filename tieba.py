# ---------- nothing is impossiable -------------
# __author__ = Luke_Tang
# __time__ = 2018.10.17
# __main__ = 爬取魔靈百度貼吧信息
# -----------------------------------------------


from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from urllib.parse import quote
from selenium.webdriver.chrome.options import Options


KEYWORD = '魔靈召喚'

for i in range(2):
	offset = i * 50
	url = 'https://tieba.baidu.com/f?kw=' + quote(KEYWORD)+ '&pn=' + str(offset)
	try:
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')  #無窗體瀏覽
		brower = webdriver.Chrome(chrome_options=options)
		brower.get(url)
		brower.maximize_window()
		brower.set_page_load_timeout(15)
		yeshu = brower.find_element_by_xpath('//*[@id="frs_list_pager"]/span').text
		print('---------當前搜索頁面：第' + yeshu + '頁----------')
		contents = brower.find_elements_by_xpath('//*[@id="thread_list"]//div/div[2]/div[1]/div[1]/a')
		authors = brower.find_elements_by_xpath('//*[@id="thread_list"]//div/div[2]/div[1]/div[2]/span[1]/span[1]/a')
		for content,author in zip(contents,authors):
			print('內容：' + content.text + '\t作者：' + author.text + '\t鏈接：' + content.get_attribute('href'))
		time.sleep(1)
		brower.close()
	except TimeoutException:
		break

print('-----------搜索完成---------------')



