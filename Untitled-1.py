import requests
import telegram
import time
from bs4 import BeautifulSoup

bot = telegram.Bot(token = '1426984672:AAGe3XoDWRfApd62Fd_POFuvT4iBNIRro-A')


num = 18552


while True :
    time.sleep(10)
    request = requests.get('https://www.scnu.ac.kr/SCNU/na/ntt/selectNttList.do?mi=1196&bbsId=1074')
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('td > a')
    del titles[0]
    del titles[1:]
    if int(soup.find_all(class_ = 'BD_tm_none')[9].text) > num: #글번호가 최신이면                    
        for title in titles:  
            bot.sendMessage(chat_id = '-430078681', text = f"{title.text.strip()}\n\nhttps://www.scnu.ac.kr{title.attrs['href']}")  
        num += 1
    





