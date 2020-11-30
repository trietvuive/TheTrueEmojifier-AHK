import urllib.request
from selenium import webdriver
page = urllib.request.urlopen('https://www.wikipedia.org/')
driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

