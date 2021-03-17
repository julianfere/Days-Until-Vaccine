import gkeepapi
import datetime
import os
import time
from datetime import date
from dotenv import load_dotenv

load_dotenv()


def get_ini_date():
    ini_date = os.getenv('INI_DATE').split('/')
    ini_date = list(map(int,ini_date))
    return date(ini_date[0],ini_date[1],ini_date[2])

EMAIL    = os.getenv('EMAIL')
TOKEN    = os.getenv('TOKEN')
INI_DATE = get_ini_date()

offset    = -datetime.timedelta(hours=3)
tzone     = datetime.timezone(offset=offset,name='utc-3')
currentDT = datetime.datetime.now(tz=tzone)

KEEP = gkeepapi.Keep()


KEEP.resume(EMAIL, TOKEN)

def act_note():
    gnote = KEEP.find(labels = [KEEP.findLabel('Days-Until-Vaccine')])
    for note in gnote:
        nota = note
    act = str(currentDT.day)+'/'+str(currentDT.month)+'/'+str(currentDT.year)
    nota.title = 'Days Until Vaccine'
    nota.text = f'Inicio: 15/3/2020 \nActual: {act}\nDias: {abs(date(currentDT.year,currentDT.month,currentDT.day)-INI_DATE).days}'
    KEEP.sync()
    
act_note()
print('\033[92m'+'Days Until Vaccine: Status Online'+'\033[0m')
act = datetime.datetime.now(tz=tzone).day
while True:
    currentDT = datetime.datetime.now(tz=tzone)
    if act != currentDT.day:
        print('Date changed',act)
        act_note()
        act = date.today().day
    time.sleep(6300)
    print('Date not changed: ',currentDT.day,currentDT.month,currentDT.year)

    



