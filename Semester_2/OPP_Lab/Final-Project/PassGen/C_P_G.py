import random
import string
from S_P_G import S_P_G

# Encapsulation + Inheritance
class C_P_G(S_P_G):
    def __init__(self, length, Options, chars):
        super().__init__(length, Options)
        self.chars = chars

    def generate_password(self):
        super()._set_case_options()
        if self.chars:
            self._characters += string.punctuation

        self._time_function()
        
        password = ''.join(random.choice(self._characters) for _ in range(self._length))
        return password