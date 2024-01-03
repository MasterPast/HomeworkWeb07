from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

# marks = Table(
#     "marks",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("mark", Integer, nullable=False),
#     Column("date_mark", DateTime, nullable=False),
#     Column("subject_id", Integer, ForeignKey("subjects.id", ondelete="CASCADE")),
#     Column("student_id", Integer, ForeignKey("students.id", ondelete="CASCADE")),
# )

class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(10), nullable=False)
 
class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_name = Column(String(50), nullable=False)
    student_address = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey(Groups.id, ondelete="CASCADE"))

class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(50), nullable=False)

class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teachers.id, ondelete="CASCADE"))

class Marks(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    mark = Column(Integer, nullable=False)
    date_mark = Column(DateTime, nullable=False)
    subject_id = Column(Integer, ForeignKey(Subjects.id, ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey(Students.id, ondelete="CASCADE"))    