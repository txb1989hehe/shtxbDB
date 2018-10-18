# ---------- nothing is impossiable -------------
# __author__ = Luke_Tang
# __time__ = 2018.10.17
# __main__ = 百度貼吧自動回復增加經驗值
# -----------------------------------------------


from selenium import webdriver
import time
from urllib.parse import quote
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import re
from selenium.common.exceptions import TimeoutException
import random


KEYWORD = '魔靈召喚'
offset = 0
url = 'https://tieba.baidu.com/f?kw=' + quote(KEYWORD)+ '&pn=' + str(offset)
brower = webdriver.Chrome()
brower.get(url)
brower.maximize_window()
brower.delete_all_cookies()
wait = WebDriverWait(brower,20)
brower.find_element_by_css_selector('.u_login > div:nth-child(1) > a:nth-child(1)').click()
time.sleep(2)
login = wait.until(ec.element_to_be_clickable((By.ID,'TANGRAM__PSP_11__footerULoginBtn')))
login.click()
# print(login)
user = wait.until(ec.presence_of_element_located((By.ID,'TANGRAM__PSP_11__userName')))
user.send_keys('txb1989hehe')
psword = wait.until(ec.presence_of_element_located((By.ID,'TANGRAM__PSP_11__password')))
psword.send_keys('kuang803#')
login_button = wait.until(ec.element_to_be_clickable((By.ID,'TANGRAM__PSP_11__submit')))
login_button.click()
time.sleep(2)
try:
	quit_button = wait.until(ec.element_to_be_clickable((By.ID,'TANGRAM__26__header_a')))
	quit_button.click()
	time.sleep(2)
except NoSuchElementException:
	pass
count = 0
while True:
	count =+ 1
	new_url = brower.find_element_by_xpath('//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a').get_attribute('href')
	# print(brower.window_handles)
	str_cookie = 'TIEBA_USERTYPE=fa1d9a0fa7623ca6978c0a06; TIEBAUID=628f5f105828c41f45750eea; ' \
				 'rpln_guide=1; bdshare_firstime=1516933161145; __' \
				 'cfduid=da12aac6da48e8df217b5dc8f86419fcc1524019599; ' \
				 'Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1536546604,1536546795,1537343585,1538038213; ' \
				 'BAIDUID=F2B750422FF031BC4A21E67A67D25F0C:FG=1; PSTM=1538620169; ' \
				 'BIDUPSID=C253C687607D8956C42898BEBB81CF1C; ' \
				 'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ' \
				 'H_PS_PSSID=1469_21088_20927; wise_device=0; 189532523_FRSVideoUploadTip=1; ' \
				 'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1539682858,1539758862,1539760381,1539764529; ' \
				 'baidu_broswer_setup_txb1989hehe=0; ' \
				 'BDUSS=FlY0pQc3VkcmpXa3ZQM2tkWDIwRWFYVW9rU1l4UndWS2pGcHdjbFhPZy1YdTliQVFBQUFBJCQAAAAAAAAAAAEAAABrCUwLdHhiMTk4OWhlaGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD7Rx1s-0cdbNG; ' \
				 'STOKEN=1154be55c84aa0e2a6a90fa3c0fc1f01e2f9981735f908a92aee6f0be3320681; ' \
				 'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1539823039; delPer=0; PSINO=3'
	lst = re.findall('([\s\S]*?)=([\s\S]*?); ', str_cookie+'; ')
	for i in lst:
		ck = {'name':i[0],'value':i[1]}
		# print(ck)
		brower.add_cookie(ck)
	if len(brower.window_handles) < 2:
		brower.execute_script('window.open()')
		brower.switch_to_window(brower.window_handles[1])
	else:
		brower.switch_to_window(brower.window_handles[1])
	brower.get(new_url)
	# print(brower.get_cookies())
	new_wait = WebDriverWait(brower,20)
	# brower.execute_script('window.scrollTo(0, document.body.scrollHeight)')
	content = ['殺不盡的歐洲狗，我只能說66666666',
			   '大水熊的歐氣在號召你們~',
			   '貼吧里的人越來越少，哎']
	new_wait.until(ec.element_to_be_clickable((By.ID,'ueditor_replace'))).click()
	js = "document.getElementById('ueditor_replace').innerHTML='"+ random.choice(content) + "'"
	brower.execute_script(js)
	# brower.find_element_by_xpath('//*[@id="ueditor_replace"]/p').send_keys(content)
	time.sleep(3)
	try:
		brower.execute_script('window.scrollTo(0, document.body.scrollHeight)')
		bt = new_wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@class="j_floating"]/a')))
		bt.click()
		# print(bt.text)
		# brower.find_element_by_css_selector('.lzl_panel_submit').click()
		time.sleep(50)
		print('回帖成功，回帖數量：' + str(count))
		# new_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.lzl_panel_submit'))).click()
		# brower.find_element_by_css_selector('.lzl_panel_submit').click()
	except TimeoutException:
		print('回復失敗~')
		brower.close()

	brower.switch_to_window(brower.window_handles[0])
	brower.refresh()
	# print(brower.window_handles)





# brower.close()





