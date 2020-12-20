import gkeepapi
import datetime
from datetime import date
import time
import os
import keyring

absolute_path = os.path.join(os.path.dirname(__file__))

offset = -datetime.timedelta(hours=3)
tzone = datetime.timezone(offset=offset,name='utc-3')
currentDT = datetime.datetime.now(tz=tzone)

INI_DATE = date(2020,3,15)

keep = gkeepapi.Keep()
# success = keep.login('julianferegotti96@gmail.com','hicqmjycpjyldnbs')
# token = keep.getMasterToken()
# with open('token.txt','w') as out:
#     out.write(token)
# keyring.set_password('google-keep-token', 'julianferegotti96@gmail.com', token)
with open(os.path.join(absolute_path,'token.txt'),'r') as t:
    token = t.read()
keep.resume('julianferegotti96@gmail.com', token)
    



def act_note():
    gnote = keep.find(labels = [keep.findLabel('Days-Until-Vaccine')])
    for note in gnote:
        nota = note
    act = str(currentDT.day)+'/'+str(currentDT.month)+'/'+str(currentDT.year)
    nota.title = 'Days Until Vaccine'
    nota.text = f'Inicio: 15/3/2020 \nActual: {act}\nDias: {abs(date(currentDT.year,currentDT.month,currentDT.day)-INI_DATE).days}'
    keep.sync()
    
act_note()
print('\033[92m'+'Days Until Vaccine: Status Online'+'\033[0m')
act = date.today().day
while True:
    if act != date.today().day:
        print('Cambio de dia')
        act_note()
        act = date.today().day
    time.sleep(3600)

    



