from datetime import datetime

class User():
    def __init__(self, name):
        self.name = name
        self.session_start = datetime.now()
        print('Session starts at %s, user named: %s' % (self.session_start, self.name))

    def how_long(self):
        session_end = datetime.now()
        session_time = session_end - self.session_start
        print(session_time)

    def register(self, password):
        
