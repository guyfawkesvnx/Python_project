from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


#Tạo Driver Chrome
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Mở đường dẩn
driver.get("https://youtube.com")

#Vào thanh tìm kiếm
search = driver.find_element_by_name("search_query")

#Nhập R3HAB
search.send_keys("R3HAB")

#Chờ 3s rồi thực hiện ENTER
sleep(3)
search.send_keys(Keys.ENTER)

#Chờ 5s rồi thực hiện click vào kênh R3HAB
sleep(5)
channel = driver.find_element_by_link_text("R3HAB")
channel.click()

#Chờ 3s rồi thực hiện click vào PLAYLISTS
#sleep(3)
#playlist = driver.find_element_by_link_text("PLAYLISTS")
#playlist.click()
