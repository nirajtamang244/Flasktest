import os
from flask import Flask, jsonify
import pandas as pd




anything= Flask(__name__)

# Load dataset
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
@anything.route("/")
def you():
    return f"Dataset Columns:{data.columns}"

filter_data= data.head(10)

@anything.route("/iris", methods= ['GET'])
def add_data():
    return jsonify(filter_data.to_dict(orient="records"))

@anything.route("/species/<name>", methods= ["GET"])
def gerSpecies(name):
    moreF= data[data["species"]==name]
    return jsonify(moreF.to_dict(orient= "records"))

@anything.route("/sepal")
def getsort():
    sort= data.sort_values(by="sepal_length",ascending=True)
    return f"this is {sort}"


if __name__==   "__main__":
    port = int(os.environ.get("PORT", 5000))
    anything.run(host="0.0.0.0", port=port, debug=True)
