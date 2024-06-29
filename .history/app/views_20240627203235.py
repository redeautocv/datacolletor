from flask import Blueprint , render_template
from flask import Flask

views= Blueprint('views',__name__)
@views.route("/s")
def home():
    return "fffff"