class  DateTimeError(Exception):
    def __init__(self,component,mistake,message):
        self.component = component
        self.mistake = mistake
        self.message = message


    def __str__(self):
        return f'Invalid value: {self.mistake} for {self.component}. It should be {self.message}'


class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def validation(self):
        if not (0 < self.year <=9999):
            raise DateTimeError("year",self.year,"between 0 and 9999")
        if not (0 < self.month <= 12):
            raise DateTimeError("month",self.month,'between 1 and 12')
        if not (0 < self.day <= 31):
            raise DateTimeError("day",self.day,'between 1 and 31')


    def date(self):
        return f'{self.year}/{self.month}/{self.day}'

date = Date(2016,10,11)



class DateTime(Date):
    def __init__(self,year,month,day,hour,minute,second):
        super().__init__(year,month,day)
        self.hour = hour
        self.minute = minute
        self.second = second
        self.validation()


    def validation(self):
        super().validation()
        if not(0 < self.hour <= 23):
            raise DateTimeError("hour",self.hour,'between 0 and 23')
        if not(0 < self.minute <= 59):
            raise DateTimeError('minute',self.minute,'between 0 and 59')
        if not(0 <self.second <= 59):
            raise DateTimeError('second',self.second,'between 0 and 59')

    def date(self):
        return super().date()+f'\n{self.hour}:{self.minute}:{self.second}'

datetime = DateTime(2015,12,12,23,66,11)
print(datetime.date())