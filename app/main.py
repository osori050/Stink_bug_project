
from flask import Flask
import os
from sqldatabase import SQLDatabase       

# Set Vars for Formatting
start_str = """{"type": "FeatureCollection", "features": """
end_str = "}"

db = SQLDatabase(host='34.27.219.64', user='postgres', password='student', database='lab1', port='5432')

# Set Up Flask App
app = Flask(__name__)

# Define Routes
@app.route("/")
def home():
    return "GIS 5572: Stinkbug project (Diego & Erik)"


@app.route("/stinkbug_prediction")
def temperature_predictive_analysis():

    # Make Connection
    db.connect()

    # Query
    q = "SELECT JSON_AGG(ST_AsGeoJSON(cities)) FROM cities;"

    # Formatting
    q_out = str(db.query(q)[0][0]).replace("'", "")

    # Close Connection
    db.close()

    # Return GeoJSON Result
    return start_str + q_out + end_str


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


