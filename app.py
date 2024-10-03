from flask import Flask, render_template, redirect, url_for, request, flash, session, make_response
import re, json, hashlib, os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secret'
app.permanent_session_lifetime = timedelta(seconds=60)
@app.route("/")
def homepage():
    return render_template ("homepage.html",user = "")