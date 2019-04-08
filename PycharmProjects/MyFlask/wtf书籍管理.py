from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key="abbc45646656165asdsfsdgsdf"
'''
1.定义作者类（id，作者姓名，作者所写的书籍）
2.定义书籍类（id，书名，书籍的作者）
3.在添加数据时要进行try和db.session.rollback()
4.append_form.author.data取表单中的author数据
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

#创建表单类，用来添加信息
class Append(FlaskForm):
    author = StringField("作者：",validators=[DataRequired()])
    book = StringField("书籍：",validators=[DataRequired()])
    submit = SubmitField('添加')

@app.route('/', methods=['get', 'post'])
def index():
    #初始化表单
    append_form = Append()
    authors= Author.query.all()

    if request.method == 'POST':
        #post表示添加 当作者不存在时添加作者和书籍，当作这存在时直接添加书籍
        if append_form.validate_on_submit():
            #验证都通过
            author_name = append_form.author.data
            book_name = append_form.book.data
            # 判断数据是否存在
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                try:
                    # 先添加作者
                    author = Author(name=author_name)
                    db.session.add(author)
                    db.session.commit()
                    # 再添加书籍
                    book = Book(name=book_name, author_id=author.id)
                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    print(e)
                    flash("数据添加错误")
            else:
                book_names = [book.name for book in author.author_book]
                if book_name in book_names:
                    flash('该作者已存在相同的书名')
                else:
                    try:
                        book = Book(name=book_name, author_id=author.id)
                        db.session.add(book)
                        db.session.commit()
                    except Exception as e:
                        db.session.rollback()
                        print(e)
                        flash('数据添加错误')
        else:
            flash('数据输入有问题')
        authors = Author.query.all()
        books = Book.query.all()
    return render_template('test2.html',authors=authors,form=append_form)
# 删除作者
@app.route('/delete_author/<int:author_id>')
def delete_author(author_id):
    author = Author.query.get(author_id)
    if not author:
        flash('数据不存在')
    else:
        try:
            Book.query.filter_by(author_id=author_id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            flash('操作数据库失败')

    return redirect(url_for('index'))


# 删除书籍
@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        flash('数据不存在')
    else:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            flash('操作数据库失败')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)