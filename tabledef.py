from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base

engine = create_engine("mysql://root:root@localhost/BlogVer1?charset=utf8")
base = automap_base()

base.prepare(engine, reflect=True)

DANHMUC = base.classes.DANHMUC
BAIVIET = base.classes.BAIVIET
