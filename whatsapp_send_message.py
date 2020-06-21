from selenium import webdriver as GoToChrome
# By: ClickCyber From israel 
driver = GoToChrome.Chrome('C:\\Users\\admin\\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
outpot , name, CLOSE = '' , [], 'close'
while outpot != CLOSE:
    outpot = input('Enter title to send ')
    name.append(outpot)
name.remove(CLOSE)
msg = input('Enter message:\n')
input('Enter anything after scan QR code')
for index in name:
    print(f'send to {index} msg send {msg}')
    user = driver.find_element_by_xpath(f'//span[@title=\'{index}\']')
    user.click()
    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
print('Done !')