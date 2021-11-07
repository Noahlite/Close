import sqlalchemy as sqlalchemy
from flask import Flask, render_template, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap




app = Flask(__name__)
app.secret_key = "helloworld"
Bootstrap(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///post.db'
# db = SQLAlchemy(app)

class Form(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Login')


# class Blog_post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False )
#     content = db.Column(db.Text, nullable=False)
#     author = db.Column(db.String(30), nullable=False, default='N/A' )
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'BlogPost {self.id}'

@app.route('/login', methods=['POST','GET'])
def login():
    login_form = Form()
    login_form.validate_on_submit()

    return render_template('login.html', form=login_form)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/download')
def download():
    return send_from_directory(directory='static', filename='veil/view-player.exe')

if __name__ == "__main__":
    app.run(debug=True)