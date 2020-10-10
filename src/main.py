import logging
from students import Students
from tutors import Tutors


logging.basicConfig(level=logging.DEBUG, filename='../log/university.log', filemode='w')
logging.info(dir())


def run():
    student = Students('../configs/students.json')
    logging.info('Students:')
    logging.info(student.greet())
    logging.info(student.study_year(2015))

    tutor = Tutors('../configs/tutors.json')
    logging.info('Tutors:')
    logging.info(tutor.greet())
    logging.info(tutor.working_year(1999))


if __name__ == '__main__':
    run()
