from abc import ABC, abstractmethod
import re

class Person(ABC):
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.location = ""

        self.phn_re = re.compile(r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$')
        self.email_re = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')

    @abstractmethod
    def login():
        """"
            This is the method for login.
        """
    
    def logout(self):
        return