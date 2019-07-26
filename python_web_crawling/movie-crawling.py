import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

bot = telegram.Bot(token = '817607042:AAGzH2kmTkeea_z0Gn96G99L1cgVaCgyjG0')

_date = datetime.datetime.date(datetime.datetime.today())
# _date = (_date).text.replace('-', '' )
print(_date)
url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=05,207&amp;theatercode=0160&amp;date=' + str(_date)
print(url)

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    # imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        # bot.sendMessage(chat_id='373207487', text=title + ' IMAX 예매가 열렸습니다.')
        print(title + ' IMAX 예매가 열렸습니다.')
        # sched.pause()
    else:
    #     bot.sendMessage(chat_id='373207487', text='IMAX 예매가 아직 열리지 않았습니다.')
        print('IMAX 예매가 아직 열리지 않았습니다.')



# sched = BlockingScheduler()
# sched.add_job(job_function, 'interval', seconds=30)
# sched.start()


