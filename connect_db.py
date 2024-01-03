from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///univer_base.db")
Session = sessionmaker(bind=engine)
session = Session()
