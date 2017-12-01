from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('mysql:///root:root@localhost/BlogVer1?charset=utf8')

session = sessionmaker(bind=engine)
s = session()

s.close()

