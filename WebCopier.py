# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import win32clipboard, os, re, time

op = webdriver.ChromeOptions()
op.add_argument('--lang=en')
wd = webdriver.Chrome(chrome_options=op)
list = os.listdir('.')
pwd = os.getcwd()
print 'Now we are at', pwd
count = 0
for fileName in list:
    if not re.match(r'.*html', fileName):
        continue
    count += 1
    print 'doing', fileName
    wd.get(pwd + '\\' + fileName)
    ele = wd.find_element_by_css_selector('body')
    time.sleep(1)
    ele.send_keys(Keys.CONTROL, 'a')
    ele.send_keys(Keys.CONTROL, 'c')
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    with open(fileName.replace('html', 'txt'), 'w') as f:
        f.write(data)

print count
wd.close()
