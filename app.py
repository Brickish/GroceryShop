from flask import Flask, render_template, redirect, url_for, request, flash, session, make_response
import re, json, hashlib, os
from datetime import timedelta
import database

app = Flask(__name__)
app.secret_key = 'secret'
app.permanent_session_lifetime = timedelta(seconds=60)
@app.route("/")
def homepage():
    return render_template ("homepage.html",user = "")
@app.route("/login")
def login():
    return render_template ("login.html",user = "")
@app.route("/register")
def register():
    return render_template ("validation.html",user = "")
@app.route("/verify", methods=["POST"])
def verify():
    username = request.form.get("username")
    password = request.form.get("password")
    confirmpassword = request.form.get("confirmpassword")
    if password == confirmpassword:
        database.newuser(username, password) 
        return render_template ("login.html",user = "")
    else:
        return render_template ("validation.html",user = "")
