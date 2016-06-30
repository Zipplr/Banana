from datetime import datetime, date, time
from time import sleep as wait

class Timer():
    """
    Timer - reminder. Remind you some deal
    with indetifier return identifier(int)
    version 0.1 from 29.06.16
    """
    def __init__(self):
        self.session_start = datetime.now()
        print('Session starts at %s' % (self.session_start))

    def alarm(self, time_point, identifier):
        trigger = True
        while trigger:
            if datetime.now() > time_point:
                print('ALARM: %s || %s' % (identifier, datetime.now()))
                trigger = False
                return identifier
            else:
                print('%s ||| %s' % (identifier, datetime.now()))
            wait(30)
    
        
        
