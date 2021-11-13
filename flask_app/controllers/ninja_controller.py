from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



#CREATE - render new ninja form
@app.route("/ninjas/new")
def new_ninja():
    return render_template("new_ninja.html", all_dojos = Dojo.get_all())


#CREATE - POST
@app.route("/ninjas/create", methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)

    return redirect("/")


