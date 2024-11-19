import random
import string
from datetime import datetime

class Main_Base:
    def __init__(self, length):
        self._length = length
        self._characters = string.digits

    def _time_function(self):
        current_time = datetime.now()
        year = current_time.year
        month = current_time.month
        day = current_time.day
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        random_time = year + month + day + hour + minute + second
        random.seed(random_time)
        time_encryption = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        return time_encryption

    def generate_password(self):
        self._set_case_options()
        time_encryption = self._time_function()

        password = ''.join(random.choice(self._characters) for _ in range(self._length - 5))
        return password + time_encryption

class S_P_G(Main_Base):
    def __init__(self, length, Options):
        super().__init__(length)
        self.Options = Options

    def generate_password(self):
        self._set_case_options()
        self._time_function()

        password = ''.join(random.choice(self._characters) for _ in range(self._length))
        return password

    def _set_case_options(self):
        if self.Options == 'lower':
            self._characters += string.ascii_lowercase
        elif self.Options == 'upper':
            self._characters += string.ascii_uppercase
        elif self.Options == 'both':
            self._characters += string.ascii_letters
