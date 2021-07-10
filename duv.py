import gkeepapi
import datetime
import os
import time
from datetime import date

class DaysUntilVaccine:
    OFFSET    = -datetime.timedelta(hours=3)
    TIME_ZONE = datetime.timezone(offset=OFFSET, name='utc-3')
    EMAIL     = os.getenv('EMAIL')
    TOKEN     = os.getenv('TOKEN')
    KEEP      = gkeepapi.Keep()

    def __init__(self):
        self.ini_date    = self._get_ini_date()
        self.actual_date = datetime.datetime.now(tz=self.TIME_ZONE).date()
        self.KEEP.resume(self.EMAIL, self.TOKEN)

    def update_note(self):
        note = self.KEEP.find(labels = [self.KEEP.findLabel('Days-Until-Vaccine')]).__next__()
        act  = self._format_date_string(self.actual_date)
        ini  = self._format_date_string(self.ini_date)
        note.title = 'Days Until Vaccine'
        note.text = f'Inicio: {ini} \nActual: {act}\nDias: {self._calculate_days(self.actual_date)}'
        self.update_date()
        self.KEEP.sync()

    def update_date(self):
        self.actual_date = datetime.datetime.now(tz=self.TIME_ZONE)
    
    def formated_date(self):
        return self._format_date_string(self.ini_date)

    # Private

    def _get_ini_date(self):
        ini_date = os.getenv('INI_DATE').split('/')
        ini_date = list(map(int,ini_date))
        return date(ini_date[0],ini_date[1],ini_date[2])

    def _current_day(self):
        return datetime.datetime.now(tz=self.TIME_ZONE)

    def _format_date_string(self,date):
        return f'{date.day}/{date.month}/{date.year}'
    
    def _calculate_days(self,date):
        return abs(date.date() - self.ini_date).days


DUV = DaysUntilVaccine()

print('\033[92m'+'Days Until Vaccine: Status Online'+'\033[0m')

DUV.update_date()
DUV.update_note()

act = datetime.datetime.now(tz=DaysUntilVaccine.TIME_ZONE).day

while True:
    if act != DUV.actual_date.day:
        print('Date changed',act)
        DUV.update_note()
        act = date.today().day
    time.sleep(6300)
    print(f'Date not changed: {DUV.formated_date}')

        

