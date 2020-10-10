from persons import Persons
from datetime import datetime


class Tutors(Persons):
    def working_year(self, joined):
        year = datetime.now().year - joined
        return f'I have been working for the university for {year} years, I am {self.age} y.o.'
