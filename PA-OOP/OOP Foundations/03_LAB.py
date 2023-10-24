class MobilePhone():
    def __init__(self, number: str):
        self.number = number

    def turn_on(self):
        print(f'mobile phone {self.number} is turned on')
    
    def turn_off(self):
        print('mobile phone is turned off')
    
    def call(self, number:str):
        print(f'calling {number}')
    

phone1 = MobilePhone('673486640')
phone2 = MobilePhone('655050623')
phone1.turn_on()
phone1.call(677666343)
phone1.turn_off()