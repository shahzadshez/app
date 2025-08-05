import os
from flask import Flask, request, render_template, redirect, url_for
from utils import get_countries, get_index_year, generate_chart


app = Flask(__name__)
STATIC_FOLDER = "static"
os.makedirs(STATIC_FOLDER, exist_ok=True)

@app.route("/")
def index():
    chart1_filter = request.args.get("chart1_filter", "Country1")
    print(chart1_filter)
    filters = get_countries()
    return render_template("index.html", chart1_filter=chart1_filter, filters=filters)

@app.route("/chart1-data")
def chart1_data():
    filter_val = request.args.get("filter", "Country1")

    # Example data based on filter
    data_map = get_index_year()
    data = data_map.get(filter_val, data_map["Country1"])

    # Generate chart
    generate_chart(data)

    return redirect(url_for("index", chart1_filter=filter_val))

if __name__ == "__main__":
    app.run(debug=True)
