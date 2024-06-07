from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 设置 Chrome 选项
chrome_options = Options()

# 创建一个浏览器实例
browser = webdriver.Chrome(options=chrome_options)

# 打开链接
url = "https://radar.cloudflare.com/charts/LargerTopDomainsTable/attachment?id=525&top=1000000"
browser.get(url)

# 等待一段时间以确保下载完成
time.sleep(60)

# 关闭浏览器
browser.quit()
