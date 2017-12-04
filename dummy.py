from sqlalchemy.orm import sessionmaker
from tabledef import *
from sqlalchemy import create_engine
engine = create_engine('mysql:///root:root@localhost/BlogVer1?charset=utf8')

session = sessionmaker(bind=engine)
s = session()

s.add_all([
    DANHMUC(MaMuc='PY', MaCha=null, TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='DJ_PY', MaCha='PY', TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='FL_PY', MaCha='PY', TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='OT_PY', MaCha='PY', TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='JS', MaCha=null, TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='JQ_JS', MaCha='JS', TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='OT_JS', MaCha='JS', TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='FE', MaCha=null, TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='OUT', MaCha=null, TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='LAM', MaCha='OUT', TenMuc='Python', SoBai=0),
    DANHMUC(MaMuc='HOC', MaCha='OUT', TenMuc='Python', SoBai=0)
])
s.commit()
s.close()

