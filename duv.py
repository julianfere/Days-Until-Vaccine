import gkeepapi
import datetime
from datetime import date
import time
import os

absolute_path = os.path.join(os.path.dirname(__file__))

offset = -datetime.timedelta(hours=3)
tzone = datetime.timezone(offset=offset,name='utc-3')
currentDT = datetime.datetime.now(tz=tzone)

INI_DATE = date(2020,3,15)

with open(os.path.join(absolute_path,'token.txt'),'r') as t:
    info = t.readlines()
keep = gkeepapi.Keep()
success = keep.login(info[0],info[1])  

def act_note():
    gnote = keep.find(labels = [keep.findLabel('Days-Until-Vaccine')])
    for note in gnote:
        nota = note
    act = str(currentDT.day)+'/'+str(currentDT.month)+'/'+str(currentDT.year)
    nota.text = f'Inicio: 15/3/2020 \nActual: {act}\nDias: {abs(date(currentDT.year,currentDT.month,currentDT.day)-INI_DATE).days}'
    keep.sync()
    


act = date.today().day
while True:
    if act != date.today().day:
        print('Cambio de dia')
        act_note()
        act = date.today().day
    time.sleep(3600)

    



