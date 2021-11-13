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


#READ ONE
@app.route("/ninjas/<int:ninja_id>")
def display_one_ninja(ninja_id):
    return render_template("one_ninja.html", ninja = Ninja.get_one_ninja({"id": ninja_id}))


#UPDATE - render
@app.route("/ninjas/<int:ninja_id>/edit_ninja")
def edit_ninja_form(ninja_id):
    return render_template("edit_ninja.html", ninja = Ninja.get_one_ninja({"id": ninja_id}))


#UPDATE - post
@app.route("/ninjas/<int:ninja_id>/update", methods = ["POST"])
def update_ninja(ninja_id):
    print(request.form)
    data = {
        **request.form,
        "id": ninja_id
    }
    Ninja.update(data)

    return redirect(f"/ninjas/{ninja_id}")


#DELETE
@app.route("/ninjas/<int:ninja_id>/delete_ninja")
def delete_dojo(ninja_id):
    Ninja.delete({"id": ninja_id})

    return redirect("/")

