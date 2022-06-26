import sys, os
sys.path.append(os.getcwd())
import unittest, yagmail, time
from tools.HTMLTestRunner import HTMLTestRunner


def auto_email(html_url):
    yag = yagmail.SMTP('1272459506@qq.com', 'ripelhlqgzpbbadf', 'smtp.qq.com')
    yag.send('1272459506@qq.com', '测试报告', '请查收', html_url)


suite = unittest.defaultTestLoader.discover('./scripts', 'test*.py')
url = f'./report/{time.strftime("%Y%m%d-%H%M%S")}_report.html'
with open(url, 'wb') as f:
    runner = HTMLTestRunner(f, verbosity=1, title='测试报告', description='测试环境: win10')
    runner.run(suite)
# auto_email(url)
