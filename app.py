from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import pandas as pd

app = Flask(__name__)

headings = ("Name", "Role", "Salary")
data = np.array((
    ("Rolf", "Software Engineer", "50k"),
    ("Amy", "Software Engineer", "30k"),
    ("Bob", "Software Engineer", "60k"),
))


@app.route("/")
def table():
    return render_template("./index.html", table_heading=headings, data=data)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        perc1 = int(request.form['perc1'])
        perc2 = int(request.form['perc2'])
        perc3 = int(request.form['perc3'])
        return redirect(url_for("user", perc1=perc1, perc2=perc2, perc3=perc3))
    else:
        return render_template("./login.html")    



@app.route("/<perc1>,<perc2>,<perc3>")
def user(perc1, perc2, perc3):
    return f"<h1>{int(perc1)}, {int(perc2)}, {int(perc3)}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

