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

@app.route("/mun", methods=['GET'])
def list_muns():
    page = request.args.get('page', 1, type=int)
    results = Municipality.query.order_by(Municipality.mun_name.asc()).paginate(page=page, per_page=45)
    return render_template('list_mun.html', muns=results)

