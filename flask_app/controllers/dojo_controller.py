from flask import render_template, redirect, request


from flask_app import app
from flask_app.models.dojo import Dojo


#READ MANY
@app.route("/")
def index():
    return redirect("/dojos")


@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = dojos)



#CREATE - POST
@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    Dojo.create(request.form)

    return redirect("/dojos")


#READ ONE
@app.route("/dojos/<int:dojo_id>")
def display_dojo(dojo_id):
    return render_template("dojos_show.html", dojo = Dojo.get_one_dojo({'id': dojo_id}))

#DELETE
@app.route("/dojos/<int:dojo_id>/delete")
def delete_dojo(dojo_id):
    Dojo.delete({"id": dojo_id})

    return redirect("/")
