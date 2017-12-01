from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dummy import *

engine = create_engine('mysql://root:root@localhost/BlogVer1?charset=utf8')
app = Flask(__name__, static_url_path='/static')

session = sessionmaker(bind=engine)
s = session()


@app.template_filter('con')
def con_filter(MaCha):
    return s.query(DANHMUC).filter(DANHMUC.MaCha == MaCha)


@app.route('/')
def index():
    parent = s.query(DANHMUC).filter(DANHMUC.MaCha.is_(None)).all()
    # id_parent = s.query(DANHMUC.MaMuc).filter(DANHMUC.MaCha.is_(None)).all()

    context = {
        'parent': parent,
        # "id_parent": id_parent
    }
    return render_template("index.html", context=context)


if __name__ == '__main__':
    app.run(debug=True)
