# Import necessary modules
from flask import Flask, render_template, session, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail, Message
from datetime import datetime

with open("config.json") as file:
    params = json.load(file)["params"]

local_server = True
# Create Flask app instance
app = Flask(__name__)
app.secret_key = "personal"

# Provide the parameters
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_PASSWORD"] = params["gmail_password"]
app.config["MAIL_USERNAME"] = params["gmail_user"]
# Initialize the Flask Mail
mail = Mail(app)
mail.init_app(app)
# Configure the database URI
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["local_uri"]
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_uri"]

# Create a SQLAlchemy instance
db = SQLAlchemy(app)


# Define the Contact model
class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(30), nullable=False)
    Email = db.Column(db.String(30), nullable=False)
    Message = db.Column(db.String(200), nullable=False)


class Post(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(30), nullable=False)
    sub_title = db.Column(db.String(100), nullable=False)
    Content = db.Column(db.String(200), nullable=False)
    img_file = db.Column(db.String(50), nullable=True)
    Date = db.Column(nullable=True)


# Define the home route
@app.route("/")
def home():
    post = Post.query.filter_by().all()
    return render_template("home.html", home=True, params=params, posts=post)


# Define the login route
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" in session and session["user"] == params["uname"]:
        post = Post.query.all()

        return render_template("success.html", params=params, posts=post)
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("password")
        if username != params["uname"] or password != params["password"]:
            flash("Invalid Email or Password")
            return render_template("login.html", params=params)

        else:
            session["user"] = username
            post = Post.query.all()
            return render_template("success.html", params=params, posts=post)
    return render_template("login.html", params=params)


# Define the post route
@app.route("/post/<string:post_slug>")
def post(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    return render_template("post.html", params=params, post=post)


# Define the about route
@app.route("/about")
def about():
    return render_template("about.html", params=params)


# Define the contact route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get the form data
        name = request.form.get("name")
        contact_email = request.form.get("email")
        contact_message = request.form.get("message")
        # Create a new entry in the database
        entry = Contact(Name=name, Email=contact_email, Message=contact_message)
        db.session.add(entry)
        db.session.commit()
        # Send an email to the user
        msg = Message(
            subject="New Message from QuillBlog",
            sender=contact_email,
            recipients=[params["gmail_user"]],
            body=f"Message from QuillBlog\n From: {contact_email}\n Message: {contact_message}",
        )
        mail.send(msg)
        return redirect(url_for("contact"))
    return render_template("contact.html", params=params)


@app.route("/edit/<string:post_sno>", methods=["GET", "POST"])
def edit(post_sno):
    if "user" in session and session["user"] == params["uname"]:
        if request.method == "POST":
            Title = request.form.get("title")
            sub_title = request.form.get("sub_title")
            Content = request.form.get("content")
            img_file = request.form.get("img_file")
            post = Post.query.filter_by(sno = post_sno).first()
    return render_template("edit.html", params=params, )


# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
