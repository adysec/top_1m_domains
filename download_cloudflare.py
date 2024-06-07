from selenium import webdriver
import time

# 创建一个浏览器实例
browser = webdriver.Chrome()  # 这里假设你使用 Chrome 浏览器，需要下载相应的驱动程序

# 打开链接
url = "https://radar.cloudflare.com/charts/LargerTopDomainsTable/attachment?id=525&top=1000000"
browser.get(url)

# 等待页面加载
time.sleep(60)  # 可以根据实际情况调整等待时间
time.sleep(10)

# 关闭浏览器
browser.quit()
