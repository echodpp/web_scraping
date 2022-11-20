- 'curl' doesn't work most of the time cause website owners use various ways to stop bots
- we could use headless browser: a web browser without GUI
```
from selenium import webdriver

chrome_options=webdrvier.ChromeOptions()
chorme_options.headless =True
chorme=webdriver.Chrome(
  chrome_options=chrome_options)
 page =chrome.get(url)
