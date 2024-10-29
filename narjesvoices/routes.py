from flask import render_template, url_for, redirect, flash
from narjesvoices import app, db, bcrypt
from narjesvoices.forms import RegistrationForm, LoginForm
from narjesvoices.models import User, Post


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',)




@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)