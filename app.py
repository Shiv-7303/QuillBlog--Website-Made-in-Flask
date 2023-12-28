from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/quillblog"
db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(30), nullable=False)
    Email = db.Column(db.String(30), nullable=False)
    Message = db.Column(db.String(200), nullable=False)


@app.route("/")
def home():
    return render_template("home.html", home=True)


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        entry = Contact(Name=name, Email=email, Message=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html", msg=True)


if __name__ == "__main__":
    app.run(debug=True)
