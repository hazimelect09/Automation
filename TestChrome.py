from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from configparser import ConfigParser
config=ConfigParser()
print('Enter the path of the config file')
path=input()
config.read(path)
print(config.sections())
print(config['test']['student'])

print('Enter the location of the chrome driver ')
ChromePATH = input()
Opt= Options()
PATH = ChromePATH
Opt.add_experimental_option('debuggerAddress','localhost:8989')
driver = webdriver.Chrome(executable_path=PATH,options=Opt)
#self.driver = webdriver.Chrome(PATH,Opt)
driver.implicitly_wait(4)
driver.find_element_by_id('search_query_top').send_keys('testinggg')
driver.find_element_by_name('submit_search').click()