from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
'''
1.定义作者类（id，作者姓名，作者所写的书籍）
2.定义书籍类（id，书名，书籍的作者）
'''

#设置连接数据
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:20110923@127.0.0.1:3306/test27'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

#实例化SQLAlchemy对象
db = SQLAlchemy(app)


#定义模型类-作者
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    author_book = db.relationship('Book',backref='author')
    def __repr__(self):
        return 'Author:%s' %self.name

#定义模型类-书名
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))
    def __str__(self):
        return 'Book:%s,%s'%(self.info,self.lead)

@app.route('/',methods=['GET','POST'])
def index():
    author = Author.query.all()
    book = Book.query.all()
    return render_template('..Books_Manage.html',author=author,book=book)

if __name__ == '__main__':

    # au1 = Author(name='老王')
    # au2 = Author(name='老尹')
    # au3 = Author(name='老刘')
    # # 把数据提交给用户会话
    # db.session.add_all([au1, au2, au3])
    # # 提交会话
    # db.session.commit()
    # bk1 = Book(name='老王回忆录', author_id=au1.id)
    # bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    # bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    # bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    # bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # # 把数据提交给用户会话
    # db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # # 提交会话varchar(30) character set utf8
    # db.session.commit()

    app.run(debug=True)