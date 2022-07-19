from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#NOTE:download chromedriver.exe at given path to make this program work
path     = "E:\downloads\chromedriver"  #chromedriver path 

website  = "https://www.thesun.co.uk/tvandshowbiz/" #the website from which we will webscrape

#options used here to not open the website whenever we run the program
options = Options()
options.headless = True

#basic setup 
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)
driver.get(website)

titles = []
subtitles = []
links = []

containers = driver.find_elements(by="xpath",value='//div[@class="rail__item-content"]')

for container in containers:
    title = container.find_element(by='xpath', value='.//h3').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    subtitle = container.find_element(by='xpath', value='.//span').text
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
print(titles)
print(subtitles)
print(links)