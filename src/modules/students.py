from persons import Persons
from datetime import datetime


class Students(Persons):
    def study_year(self, joined):
        year = datetime.now().year - joined
        return f'I am on the {year} year of study, I am {self.age} y.o.'
