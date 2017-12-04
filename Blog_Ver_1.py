from flask import Flask
from flask import render_template, request, redirect
from dummy import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

engine = create_engine('mysql://root:root@localhost/BlogVer1?charset=utf8')
app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'admin2101'
session = sessionmaker(bind=engine)
s = session()

admin = Admin(app)

admin.add_view(ModelView(BAIVIET, s))


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
