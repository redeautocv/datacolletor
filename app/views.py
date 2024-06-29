from flask import Blueprint , render_template
from flask import Flask

views= Blueprint('views',__name__)
@views.route("/")
def home():
    return "fffff"