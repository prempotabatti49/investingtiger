from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import pandas as pd
from investment_sip import *

app = Flask(__name__)

headings = ("Name", "Role", "Salary")
data = np.array((
    ("Rolf", "Software Engineer", "50k"),
    ("Amy", "Software Engineer", "30k"),
    ("Bob", "Software Engineer", "60k"),
))


@app.route("/login")
def table():
    return render_template("./index.html", table_heading=headings, data=data)

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        start_sip = int(request.form['start_sip'])
        total_years = int(request.form['total_years'])
        roi_list = [float(request.form[f'return{i+1}']) for i in range(3)]
        yearly_raise_list = [float(request.form[f'incr{i+1}']) for i in range(2)]
        investing_data = calculate_sip_returns(start_sip, total_years, roi_list, yearly_raise_list)
        cols = investing_data.columns
        return render_template("./result.html", investing_data=list(investing_data.itertuples(index=False)), cols=cols)
        # return redirect(url_for("user", investing_data=investing_data, cols=cols))
    else:
        return render_template("./sip.html")


@app.route("/magic/<cols>/<investing_data>")
def user(investing_data, cols):
    # return render_template("result.html", investing_data=request.args.get('investing_data'), cols=request.args.get('cols'))
    return render_template("./result.html", investing_data=list(investing_data.itertuples(index=False)), cols=cols)


if __name__ == "__main__":
    app.run(debug=True)

