import faker
from connect_db import session
from models import Groups, Marks, Students, Subjects, Teachers
from random import randint

NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_TEACHERS = randint(3, 5)
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_MARKS_ON_SUBJECT = randint(10, 20)

fake_data = faker.Faker(locale="uk_UA")

if __name__ == "__main__":

    for _ in range(NUMBER_TEACHERS):
        teacher = Teachers(teacher_name=fake_data.name().upper())
        session.add(teacher)

    for _ in range(NUMBER_SUBJECTS):
        subject = Subjects(
                            subject_name=fake_data.job(),
                            teacher_id=randint(1, NUMBER_TEACHERS)
                            )
        session.add(subject)

    for _ in range(NUMBER_GROUPS):
        gr_name = f"UNV-G{_+1}"
        group = Groups(group_name=gr_name)
        session.add(group)
    
    for _ in range(NUMBER_STUDENTS):
        student = Students(
                            student_name=fake_data.name(),
                            student_address=fake_data.address(),
                            group_id = randint(1, NUMBER_GROUPS)
                            )
        session.add(student)

    for _ in range(NUMBER_MARKS_ON_SUBJECT * NUMBER_STUDENTS):
        mark = Marks(
            mark=randint(1, 5),
            date_mark=fake_data.date_between(start_date='-7d', end_date='today'),
            subject_id=randint(1, NUMBER_SUBJECTS),
            student_id=randint(1, NUMBER_STUDENTS)
                    )
        session.add(mark)

    session.commit()