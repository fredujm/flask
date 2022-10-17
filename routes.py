from flask import render_template, request
from app_coll import app, db
from app_coll.models import Region, Department, Municipality

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/region", methods=['GET'])
def list_regions():
    regions = Region.query.all()
    return render_template('list_regions.html', regions=regions)
    