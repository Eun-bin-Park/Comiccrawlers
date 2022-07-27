'''
爬取漫画《南部档案》
'''
from selenium import webdriver
import time
import requests
import os
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome('chromedriver',options=options)
browser.maximize_window()
def get_info(qq):
    #https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&redirect_uri=https%3A%2F%2Fwww.kuaikanmanhua.com%2Fv1%2Fpassport%2Flogin%2Fpc%2Fuser_qq_login_check&state=90fdf07932d600c7238df073efd35d03&client_id=101333357
    browser = webdriver.Chrome('D:/Python/chromedriver.exe')
    browser.get('https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=101483258&redirect_uri=https://ac.qq.com/loginSuccess.html?url=https%3A%2F%2Fac.qq.com%2Findex%3Fauth%3D1')
    browser.switch_to.frame('ptlogin_iframe')
    browser.find_element_by_id('switcher_plogin').click()
    browser.find_element_by_id('u').clear()
    browser.find_element_by_id('u').send_keys(qq)
    browser.find_element_by_id('p').clear()
    browser.find_element_by_id('p').send_keys('密码')
    browser.find_element_by_id('login_button').click()
    time.sleep(3)
    browser.get('https://ac.qq.com/ComicView/index/id/635753/cid/3')
    def uestc(chapter):
        time.sleep(0.5)
        targets = browser.find_elements_by_xpath('//ul[@id="comicContain"]/li')
        for target in targets:
            browser.execute_script('arguments[0].scrollIntoView();', target)
            time.sleep(0.5)
        time.sleep(0.5)
        img_list = browser.find_elements_by_xpath('//ul[@id="comicContain"]/li/img')
        page = 1
        if not os.path.exists(f'南部档案/第{chapter}话'):
            os.mkdir(f'../南部档案/第{chapter}话')
        for li in list(img_list):
            print('----------正在爬取第{}页----------'.format(page))
            img_url = li.get_attribute('src')
            print(img_url)
            img_data = requests.get(img_url).content
            with open(f'../南部档案/第{chapter}话/{page}.jpg',mode='wb') as f:
                f.write(img_data)
            page +=1
        browser.find_element_by_xpath('//*[@id="nextChapter"]').click()
    chapter = 1
    while True:
        uestc(chapter)
        chapter +=1
if __name__ == '__main__':
    get_info('QQ号')
