from connect_db import session
from models import Groups, Marks, Students, Subjects, Teachers
from sqlalchemy import func, desc

def choose_subject():
    subjects = session.query(Subjects.id, Subjects.subject_name).select_from(Subjects).order_by(Subjects.id).all()
    print_table(subjects)
    result = int(input('Input the subject >>> '))-1
    return subjects[result][1]

def choose_teacher():
    teachers = session.query(Teachers.id, Teachers.teacher_name).select_from(Teachers).order_by(Teachers.id).all()
    print_table(teachers)
    result = int(input('Input the teacher >>> '))-1
    return teachers[result][1]

def print_table(table):
    for row in table:
        print(row)

def select_1():
    result = session.query(Students.student_name, func.round(func.avg(Marks.mark), 2).label('avg_mark'))\
        .select_from(Marks).join(Students).group_by(Students.student_name).order_by(desc('avg_mark')).limit(5).all()
    return result

def select_2():
    subject_name = choose_subject()
# SELECT s.student_name, s2.subject_name, AVG(m.mark) FROM marks AS m
# FULL JOIN students AS s ON m.student_id = s.id
# FULL JOIN subjects AS s2 ON m.subject_id = s2.id
# WHERE s2.subject_name = '{}'
# GROUP BY s2.subject_name, s.student_name ORDER BY AVG(m.mark) DESC LIMIT 1;
    result = session.query(Students.student_name, Subjects.subject_name, func.avg(Marks.mark).label('avg_mark'))\
        .select_from(Marks).join(Students).join(Subjects).filter(Subjects.subject_name == subject_name)\
        .group_by(Subjects.subject_name).group_by(Students.student_name).order_by(desc('avg_mark')).limit(1).all()
    return result

def select_3():
    subject_name = choose_subject()
# SELECT g.group_name, s2.subject_name, ROUND(AVG(m.mark), 3) FROM marks AS m
# FULL JOIN students AS s ON m.student_id = s.id
# FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
# FULL JOIN groups AS g ON s.group_id = g.id 
# WHERE s2.subject_name = '{}'
# GROUP BY g.group_name;
    result = session.query(Groups.group_name, Subjects.subject_name, func.round(func.avg(Marks.mark), 3).label('avg_mark'))\
        .select_from(Marks).join(Students).join(Subjects).join(Groups).filter(Subjects.subject_name == subject_name)\
        .group_by(Groups.group_name).all()
    return result

def select_4():
    # SELECT ROUND(AVG(mark),3) FROM marks;
    result = session.query(func.round(func.avg(Marks.mark), 3)).select_from(Marks).all()
    return result[0][0]

def select_5():
    teacher_name = choose_teacher()
# SELECT t.teacher_name, s.subject_name FROM subjects AS s
# FULL JOIN teachers AS t ON s.teacher_id = t.id
# WHERE t.teacher_name = '{}'
# ORDER BY s.subject_name;
    result = session.query(Teachers.teacher_name, Subjects.subject_name).select_from(Subjects).join(Teachers)\
        .filter(Teachers.teacher_name == teacher_name).order_by(Subjects.subject_name).all()
    return result



if __name__ == '__main__':

    print(select_5())
