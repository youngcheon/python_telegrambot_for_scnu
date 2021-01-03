import requests
import telegram
import time
from bs4 import BeautifulSoup

bot = telegram.Bot(token = '1426984672:AAGe3XoDWRfApd62Fd_POFuvT4iBNIRro-A')

lastest_num = 0

while True :
    request = requests.get('https://www.scnu.ac.kr/SCNU/na/ntt/selectNttList.do?mi=1196&bbsId=1074')
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('td > a')
    post_num = int(soup.find_all(class_ = 'BD_tm_none')[9].text)        
    if lastest_num != post_num:
        lastest_num = post_num          
        # bot.sendMessage(chat_id = '-430078681', text = f"{titles[1].text.strip()}\n\nhttps://www.scnu.ac.kr{titles[0].attrs['href']}")  
        bot.sendMessage(chat_id = '1497406622', text = f"{titles[1].text.strip()}\n\nhttps://www.scnu.ac.kr{titles[0].attrs['href']}")  
        
    time.sleep(10)
    





