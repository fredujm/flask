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

@app.route("/region/<int:region_id>", methods=['GET'])
def getRegion(region_id):
    results = Department.query.filter(Department.region_id == region_id).all()
    print(len(results))
    return render_template('region.html', depts=results)

@app.route("/dept/<string:dept_id>", methods=['GET'])
def getDept(dept_id):
    page = request.args.get('page', 1, type=int)
    dept = Department.query.filter(Department.dept_id == dept_id).first()
    results = Municipality.query.filter(Municipality.dept_id == dept_id).paginate(page=page, per_page=45)
    return render_template('dept.html', dept=dept, municipalities=results)

@app.route("/mun/<string:mun_id>", methods=['GET'])
def getMunicipality(mun_id):
    result = Municipality.query.filter(Municipality.mun_id == mun_id).first()
    return render_template('municipality.html', municipality=result)

    