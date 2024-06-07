from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 设置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 启用无头模式
chrome_options.add_argument("--disable-dev-shm-usage")  # 防止 Chrome 在无头模式下出现崩溃
chrome_options.add_argument("--no-sandbox")  # 以沙盒模式运行，防止 Chrome 在无头模式下出现崩溃

# 创建一个浏览器实例
browser = webdriver.Chrome(options=chrome_options)

# 打开链接
url = "https://radar.cloudflare.com/charts/LargerTopDomainsTable/attachment?id=525&top=1000000"
browser.get(url)

# 等待一段时间以确保下载完成
time.sleep(60)

# 关闭浏览器
browser.quit()
