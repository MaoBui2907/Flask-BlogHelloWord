from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("mysql://root:root@localhost/BlogVer1?charset=utf8")
base = declarative_base(bind=engine)


class DANHMUC(base):
    __tablename__ = 'DANHMUC'
    MaMuc = Column(NCHAR(5), primary_key=True)
    MaCha = Column(NCHAR(5), nullable=False)
    TenMuc = Column(NVARCHAR(500), nullable=False)
    SoBai = Column(Integer, nullable=False)


class BAIVIET(base):
    __tablename__ = 'BAIVIET'
    MaBai = Column(Integer, primary_key=True, autoincrement=True)
    MaMuc = Column(NCHAR(5), ForeignKey(DANHMUC.MaMuc), nullable=False)
    MoTa = Column(NVARCHAR(300), nullable=False)
    NoiDung = Column(NVARCHAR(1000), nullable=False)
    DANHMUC = relationship('DANHMUC', backref='DANHMUC')


base.metadata.create_all(engine)
