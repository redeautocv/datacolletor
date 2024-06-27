from flask import Blueprint , render_template
from flask import Flask

views= Blueprint('views',__name__)
xx=10
@views.route("/s")
def home():
    return "fffff"