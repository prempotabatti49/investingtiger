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
        investing_data_ = calculate_sip_returns(start_sip, total_years, roi_list, yearly_raise_list)
        cols_ = investing_data_.columns.tolist()
        color_palette = ["gainsboro", "lightblue", "gold", "darkorange", "crimson", "maroon"]
        # data=[
        #     ("01-01-2020", 1597),
        #     ("02-01-2020", 1456),
        #     ("03-01-2020", 1908),
        #     ("04-01-2020", 896)
        # ]
        labels = [f"{i+1}" for i in range(total_years)]
        # labels = [row[0] for row in data]
        # values = [row[1] for row in data]
        return render_template(
            "./result.html", 
            investing_data=list(investing_data_.itertuples(index=False)), 
            cols=cols_,
            labels=labels,
            values1=investing_data_[cols_[0]].tolist(),
            values2=investing_data_[cols_[1]].tolist(),
            values3=investing_data_[cols_[2]].tolist(),
            values4=investing_data_[cols_[3]].tolist(),
            values5=investing_data_[cols_[4]].tolist(),
            values6=investing_data_[cols_[5]].tolist(),
            color_palette=color_palette
        )
        # return redirect(url_for("user", investing_data=investing_data, cols=cols))
    else:
        return render_template("./sip.html")


@app.route("/magic/<cols>/<investing_data>")
def user(investing_data, cols):
    # return render_template("result.html", investing_data=request.args.get('investing_data'), cols=request.args.get('cols'))
    return render_template("./result.html", investing_data=list(investing_data.itertuples(index=False)), cols=cols)


if __name__ == "__main__":
    app.run(debug=True)

