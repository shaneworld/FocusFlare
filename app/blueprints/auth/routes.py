from flask import redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from app.blueprints.auth import auth
from app.models import User
from .forms import LoginForm, RegisterForm
from app import db, bcrypt

@auth.route("/register", methods=["GET", "POST"])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for("basic.home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            form.email.errors.append('邮箱已被注册')
            return render_template("register.html", form=form)
        else:
            pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=pw_hash)
            db.session.add(user)
            db.session.commit()

            # login_user(user)

            return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for("basic.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("basic.home"))
        else:
            form.password.errors.append('邮箱或密码不正确。')
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
